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

# Deletes all merchants from the database
def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

# Deletes a merchant from the database by id
def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# Updates a merchant in the database
def update(merchant):
    sql = "UPDATE merchants SET name = %s WHERE id = %s"
    values = [merchant.name, merchant.id]
    run_sql(sql, values)

# Selects all merchants from the database
def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['name'], row['id'])
        merchants.append(merchant)
    return merchants

# Selects a merchant from the database by id
def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        merchant = Merchant(result['name'], result['id'])
    return merchant

# Selects a merchant from the database by name
def select_by_name(name):
    sql = "SELECT * FROM merchants WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)
    if result:
        return Merchant(result[0]['name'], result[0]['id'])
    return None