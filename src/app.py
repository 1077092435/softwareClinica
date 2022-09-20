
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

from config import config

# MODELOS
from models.ModelUser import ModelUser

# ENTITIES
from models.entities.User import User

app = Flask(__name__)

db = MySQL(app)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['email'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('home'))
            else:
                flash("Password invalido")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

    
@app.route('/administrador')
def home():
    return render_template('administrador/administrador.html')


@app.route('/gestionarCitas')
def gestionarCitas():
    return render_template('medico/gestionarCitas.html')

@app.route('/historiaClinica')
def historiaClinica():
    return render_template('medico/historiaClinica.html')

@app.route('/gestionPacientes')
def gestionPacientes():
    return render_template('administrador/gestionPacientes.html')

@app.route('/gestionMedicos')
def gestionMedicos():
    return render_template('administrador/gestionMedicos.html')

@app.route('/gestionCitas')
def gestionCitas():
    return render_template('administrador/gestionCitas.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()