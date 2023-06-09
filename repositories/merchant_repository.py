from db.run_sql import run_sql

from models.merchant import Merchant
from models.transaction import Transaction

# Saves a merchant to the database
def save(merchant):
    sql = "INSERT INTO merchants (name) VALUES (%s) RETURNING *"
    values = [merchant.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant
    
    