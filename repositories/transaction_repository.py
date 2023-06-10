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