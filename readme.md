https://www.youtube.com/watch?v=fxavwHPJ36o

Aprende a crear un sitio web completamente desde cero utilizando Python (python3), y Flask (framework de aplicaciones web). Este ejemplo plantea la creación de un sitio con una navegación dinamica de manera similar como se haría con PHP.
Ademas terminaremos desplegando nuestra aplicación en un servicio de la nube llamado Heroku.

CÓDIGO FINAL:
https://github.com/FaztWeb/python-flask-first-website
https://github.com/FaztWeb/flask-crud-contacts-app


…or create a new repository on the command line
echo "# python-flask-website-heroku" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/jav2074/python-flask-website-heroku.git
git push -u origin master

…or push an existing repository from the command line
git remote add origin https://github.com/jav2074/python-flask-website-heroku.git
git push -u origin master



git remote -v
git remote rename <old> <new>
git remote rename https://github.com/jav2074/python-flask-website.git origin https://github.com/jav2074/python-flask-website-heroku.git
git remote rename origin https://github.com/jav2074/python-flask-website-heroku.git

git remote rm https://github.com/jav2074/python-flask-website.git
//para eliminar una URL remota de tu repositorio.




https://flask.palletsprojects.com/en/1.1.x/installation/#installation
<!-- Instalacion -->
pip install flask


https://virtualenv.pypa.io/en/latest/installation.html
<!-- Entorno Virtual -->
<!-- Instalacion -->
pip install virtualenv
<!-- Ejecucion -->
python -m venv venv
<!-- Ejecucion -->
cd venv/Scripts
activate.bat
deactivate.bat
python --version
pip --version
<!-- Instalacion de FLASK en mi Entorno Virtual -->
pip install flask
<!-- Ejecucion -->
python ../../src/index.py

<!-- HEROKU -->
requirements.txt
    <!-- copiado de https://github.com/FaztWeb/python-flask-first-website/blob/master/requirements.txt -->
    pip freeze > ../../src/requirements.txt
runtime.txt
    <!-- https://devcenter.heroku.com/articles/python-runtimes -->
    python --version
Procfile
<!-- complemento para HEROKU -->
https://gunicorn.org/
<!-- Instalacion -->
pip install gunicorn

<!-- Repositorio de GIT -->
<!-- dentro de 'src' -->
git init
git add README.md
git status
git commit -m "first commit"
git remote add origin https://github.com/jav2074/python-flask-heroku.git
git push -u origin master