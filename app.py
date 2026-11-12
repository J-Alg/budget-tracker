from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
from pathlib import Path

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def save_data(data, filename="data.json", file_dir="assets"):
    file_path = Path(file_dir) / filename
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_data(filename="data.json", file_dir="assets"):
    file_path = Path(file_dir) / filename
    if not file_path.exists():
        return {"income": [], "expenses": []}
    with file_path.open("r") as f:
        return json.load(f)

@app.get("/")
def read_root(request: Request):
    data = load_data()
    income = data["income"]
    expenses = data["expenses"]
    income_sum = sum([i.get("income_amount", 0) for i in income])
    expenses_sum = sum([e.get("expense_amount", 0) for e in expenses])
    balance = income_sum - expenses_sum

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "message": "Hello, World!",
            "income_list": income,
            "expenses_list": expenses,
            "income_sum": income_sum,
            "expenses_sum": expenses_sum,
            "balance": balance
        })

@app.post("/add-income")
def add_income(income_source_name: str = Form(...), amount: float = Form(...)):
    data = load_data()
    data["income"].append({"income_amount": amount, "income_source_name": income_source_name.strip().upper()})
    save_data(data)
    return RedirectResponse(url="/", status_code=303)

@app.post("/add-expense")
def add_expense(expense_category: str = Form(...), expense_amount: float = Form(...)):
    data = load_data()
    data["expenses"].append({"expense_amount": expense_amount, "expense_category": expense_category.strip().upper()})
    save_data(data)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete-income/{item_index}")
def delete_income(item_index: int):
    data = load_data()
    if 0 <= item_index < len(data["income"]):
        del data["income"][item_index]
        save_data(data)
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete-expense/{item_index}")
def delete_expense(item_index: int):
    data = load_data()
    if 0 <= item_index < len(data["expenses"]):
        del data["expenses"][item_index]
        save_data(data)
    return RedirectResponse(url="/", status_code=303)
