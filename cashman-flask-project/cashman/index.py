
from flask import Flask, jsonify, request

from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    auth = request.headers.get("custom", None)
    if( auth is None):
        print( "No custopm header")
    else:
        print( "Custom header is auth=="  + auth)

    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

@app.route("/")
def hello_world():
    return "Hello, World!"
