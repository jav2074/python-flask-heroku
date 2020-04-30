from flask import Flask, render_template

# -------------------------------------------------------------------------------
# DB
# -------------------------------------------------------------------------------
import sqlite3

# connection dir property
# db_name = 'database.db'
db_name = 'src/database.db'

# Function to Execute Database Querys
def run_query(query, parameters = ()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result

# Get Products from Database
def get_products():
    # getting data
    query = 'SELECT * FROM product ORDER BY name DESC'
    db_rows = run_query(query)
    # filling data
    for row in db_rows:
        print(row)

# -------------------------------------------------------------------------------


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/db')
def db():
    get_products()
    return render_template('db.html')

if __name__ == '__main__':
    # application = Product(app)
    app.run(debug=True)     # Modo debug 