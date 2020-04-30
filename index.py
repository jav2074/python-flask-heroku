from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/db')
def db():
    return render_template('db.html')

if __name__ == '__main__':
    app.run(debug=True)     # Modo debug 