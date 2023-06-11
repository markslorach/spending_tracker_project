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

# Deletes all transactions from the database
def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

# Deletes a transaction from the database by id
def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Updates a transaction in the database
def update(transaction):
    sql = "UPDATE transactions SET (amount, merchant_id, tag) = (%s, %s, %s) WHERE id = %s"
    values = [transaction.amount, transaction.merchant.id, transaction.tag, transaction.id]
    run_sql(sql, values)

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

# Selects a transaction from the database by id
def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        transaction = Transaction(result['amount'], merchant, result['tag'], result['id'])
    return transaction

# Calculates total transactions
def total_amount():
    total = 0
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        total += row['amount']
    return total