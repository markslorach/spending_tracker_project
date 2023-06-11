from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository


transaction_blueprint = Blueprint("transaction", __name__)

# Show list of transactions
@transaction_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)

# Create new transaction
@transaction_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    amount = request.form['amount']
    merchant_id = request.form['merchant_id']
    tag = request.form['tag']
    merchant = merchant_repository.select(merchant_id)
    transaction = Transaction(amount, merchant, tag)
    transaction_repository.save(transaction)
    return redirect('/transactions')

# Show transaction info
@transaction_blueprint.route("/transactions/<id>", methods=['GET'])
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("/transactions/show.html", transaction = transaction)


