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
    merchant_name = request.form['merchant']
    tag = request.form['tag']
    merchant = merchant_repository.select_by_name(merchant_name)
    if merchant is None:
        merchant = Merchant(merchant_name)
        merchant_repository.save(merchant)
    transaction = Transaction(amount, merchant, tag)
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

# Edit transaction
@transaction_blueprint.route("/transactions/<id>/edit", methods=['GET'])
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("/transactions/edit.html", transaction = transaction)

# Update transaction
@transaction_blueprint.route("/transactions/<id>", methods=['POST'])
def update_transaction(id):
    amount = request.form['amount']
    merchant_name = request.form['merchant']
    tag = request.form['tag']
    merchant = merchant_repository.select_by_name(merchant_name)
    if merchant is None:
        merchant = Merchant(merchant_name)
        merchant_repository.save(merchant)
    transaction = Transaction(amount, merchant, tag, id)
    transaction_repository.update(transaction)
    return redirect('/transactions')