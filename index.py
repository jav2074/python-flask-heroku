from flask import Flask, render_template, request, redirect, url_for, flash

# -------------------------------------------------------------------------------
# DB
# -------------------------------------------------------------------------------
import sqlite3

# connection dir property
db_name = 'database.db'
# db_name = 'src/database.db'       # LOCAL

# Function to Execute Database Querys
def run_query(query, parameters = ()):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)   # result = 
        # result = cursor.fetchall()          # convierte el resultset en un Array
        conn.commit()
    return result

# Get Products from Database
def get_products():
    # getting data
    query = 'SELECT * FROM product ORDER BY id ASC'
    db_rows = run_query(query)
    return db_rows
# delete_products(id)
def delete_products(id):
    query = 'DELETE FROM product WHERE id = ?'
    result = run_query(query, (id, ))    #  
    return result
# -------------------------------------------------------------------------------


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'    # para flash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/db')
def db():
    result = get_products()
    return render_template('db.html', data = result)

@app.route('/delete/<string:id>')
def db_delete(id):
    result = delete_products(id)
    flash(f"Se ha borrado correctamente el registro id: {id}")
    # flash("Se ha borrado correctamente el registro id: ")
    return redirect(url_for('db'))

if __name__ == '__main__':
    app.run(debug=True)     # Modo debug 