# -------------------------------------------------------------------------------
# DB
# -------------------------------------------------------------------------------
import sqlite3
from config import config
from index import app

db_dir = app.config['DB_DIR']

# -------------------------------------------------------------------------------
# Function to Execute Database Querys
def run_query(query, parameters = ()):
    with sqlite3.connect(db_dir) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters) 
        conn.commit()
    return result
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------
def bd_result_to_json(cursor):
    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()] 
    if (len(result) == 1): result = result[0]
    return result
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# QUERIES
# -------------------------------------------------------------------------------
# Get Products from Database
def get_products():
    # getting data
    query = 'SELECT * FROM product ORDER BY id ASC'
    result = run_query(query)
    return result

# Get One Product from Database
def get_product(id):
    query = 'SELECT * FROM product WHERE id = ?'
    result = run_query(query, (id, ))    #  
    return result

# update_products
def update_products(id, name, price):
    query = 'UPDATE product SET name = ?, price = ? WHERE id = ?'
    parameters = (name, price, id)
    result = run_query(query, parameters) 
    return result

# insert_product
def insert_product(name, price):
    query = 'INSERT INTO product VALUES(NULL, ?, ?)'
    parameters = (name, price)
    result = run_query(query, parameters) 
    return result

# delete_products
def delete_product(id):
    query = 'DELETE FROM product WHERE id = ?'
    result = run_query(query, (id, ))    #  
    return result
# -------------------------------------------------------------------------------