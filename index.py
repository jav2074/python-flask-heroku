from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# -------------------------------------------------------------------------------
# DB
# -------------------------------------------------------------------------------
import sqlite3

# connection dir property
db_name = 'h_database.db'             # HEROKU

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


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'    # para flash

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/db')
def db():
    result = get_products()
    return render_template('db.html', data = result)

@app.route('/edit/<string:id>')
def db_edit(id):
    result = get_product(id)
    return render_template('update.html', data = result)
@app.route('/update/<string:id>', methods = ['POST'])
def db_update(id):
    if(request.method == 'POST'):
        name = request.form['name']
        price = request.form['price']
        result = update_products(id, name, price)
        flash(f"Se ha actualizado correctamente el registro id: {id} - name: {name} - price: {price}")
    return redirect(url_for('db'))

@app.route('/new')
def db_new():
    return render_template('insert.html')
@app.route('/insert', methods = ['POST'])
def db_insert():
    if(request.method == 'POST'):
        name = request.form['name']
        price = request.form['price']
        result = insert_product(name, price)
        flash(f"Se ha creardo correctamente el registro name: {name} - price: {price}")
    return redirect(url_for('db'))

@app.route('/del/<string:id>')
def db_del(id):
    result = get_product(id)
    return render_template('delete.html', data = result)
@app.route('/delete/<string:id>', methods = ['POST'])
def db_delete(id):
    if(request.method == 'POST'):
        result = delete_product(id)
        flash(f"Se ha borrado correctamente el registro id: {id}")
    return redirect(url_for('db'))


if __name__ == '__main__':
    app.run(debug=True)     # Modo debug 
