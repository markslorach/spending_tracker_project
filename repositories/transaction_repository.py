from db.run_sql import run_sql

from models.merchant import Merchant
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository

# Saves a transaction to the database
def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag) VALUES (%s, %s, %s) RETURNING *"
    values = [transaction.amount, transaction.merchant.id, transaction.tag]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

# Selects all transactions from the database
def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['amount'], merchant, row['tag'], row['id'])
        transactions.append(transaction)
    return transactions