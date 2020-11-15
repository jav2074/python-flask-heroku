from __init__ import create_app
from flask import render_template, request, redirect, url_for, flash, jsonify
from bd import *

# -------------------------------------------------------------------------------
app = create_app('default') 
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# API
# -------------------------------------------------------------------------------
@app.route("/api/get_my_ip", methods=["GET"])
def api_get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route("/api/get_products", methods=["GET"])
def api_get_products():
    cursor = get_products()
    result = bd_result_to_json(cursor)
    return jsonify({'products': result}), 200

@app.route('/api/get_product/<string:id>', methods=["GET"])
def api_get_product(id):
    cursor = get_product(id)
    result = bd_result_to_json(cursor)
    return jsonify({'product': result}), 200

@app.route('/api/post_product', methods = ['POST'])
def api_post_product():
    if(request.method == 'POST'):
        # print(request.json)
        # print(request)
        posted_data = request.get_json()
        print(posted_data)
        id = posted_data['id']
        # id = request.json['id'] #request.form['id']
        # id = request.args.get('id', '')
        cursor = get_product(id)
        result = bd_result_to_json(cursor)
    return jsonify({'product': result}), 200
# -------------------------------------------------------------------------------



# -------------------------------------------------------------------------------
# WEB
# -------------------------------------------------------------------------------
@app.route('/')
def home():
    return render_template('home.html', db_dir=db_dir)

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
# -------------------------------------------------------------------------------



# -------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()
# -------------------------------------------------------------------------------