from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

income = []

expenses = []

@app.get("/")
def read_root(request: Request):
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
    income.append({"income_amount": amount, "income_source_name": income_source_name.strip().upper()})
    return RedirectResponse(url="/", status_code=303)

@app.post("/add-expense")
def add_expense(expense_category: str = Form(...), expense_amount: float = Form(...)):
    expenses.append({"expense_amount": expense_amount, "expense_category": expense_category.strip().upper()})
    return RedirectResponse(url="/", status_code=303)