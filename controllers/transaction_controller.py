from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository


transaction_blueprint = Blueprint("transaction", __name__)

# Show all transactions and total transaction amount
@transaction_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = transaction_repository.total_amount()
    return render_template("transactions/index.html", transactions = transactions, total = total)

# Create new transaction
@transaction_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    amount = request.form['amount']
    merchant_name = request.form['merchant']
    date = request.form['date']
    tag = request.form['tag']
    merchant = merchant_repository.select_by_name(merchant_name)
    if merchant is None:
        merchant = Merchant(merchant_name)
        merchant_repository.save(merchant)
    transaction = Transaction(amount, merchant, date, tag)
    transaction_repository.save(transaction)
    return redirect('/transactions')

# Show transaction
@transaction_blueprint.route("/transactions/<id>", methods=['GET'])
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("/transactions/show.html", transaction = transaction)

# Delete transaction
@transaction_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')

# Update transaction
@transaction_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    amount = request.form['amount']
    merchant_name = request.form['merchant']
    date = request.form['date']
    tag = request.form['tag']
    merchant = merchant_repository.select_by_name(merchant_name)
    if merchant is None:
        merchant = Merchant(merchant_name)
        merchant_repository.save(merchant)
    transaction = Transaction(amount, merchant, date, tag, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')

# Sort transactions by month
@transaction_blueprint.route("/transactions/filter", methods=['POST'])
def sort_by_month():
    selected_month = request.form['filter']
    month_name = datetime.strptime(selected_month, "%m").strftime("%B")
    transactions = transaction_repository.select_by_month(selected_month)
    total = transaction_repository.total_amount_of_month(selected_month)
    return render_template("transactions/index.html", transactions=transactions, total=total, selected_month=month_name)