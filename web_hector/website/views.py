from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import  check_password_hash
from .bbdd import bbdd as db
from .models import Usuario
from werkzeug.security import generate_password_hash
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", User_register=current_user)

@views.route('/signup' , methods=['POST', 'GET'])
def signup(): 
    if request.method == 'POST':
        name= request.form.get('Name')
        contrasena1= request.form.get('contrasena1')
        contrasena2= request.form.get('contrasena2')
        dni= request.form.get('dni')
        surname= request.form.get('Surname')
        telefono= request.form.get('telefono')
        email= request.form.get('email')
        if(contrasena1 == contrasena2): 
            if db.get_check_email(email):
                new_user = db.insert_user(name, contrasena1, dni, telefono, email, surname)
                login_user(new_user, remember=True)
                flash('Logged in successfully!', category='success')
                return render_template("signup.html", User_register=current_user)
    return render_template("signup.html", User_register=current_user)

@views.route('/login' , methods=['POST', 'GET'])
def login(): 
    if request.method == 'POST':
        email= request.form.get('email')
        contrasena1= request.form.get('contrasena1')
        user = Usuario.query.filter_by(email=email).first()
        if not current_user.is_active:
            if user:
                if check_password_hash(user.password, contrasena1):
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    session.permanent = True
                    return render_template("home.html", User_register=current_user)
    return render_template("login.html", User_register=current_user)

@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@views.route('/ejemplares')
def ejemplares():
    return render_template("ejemplares.html", User_register=current_user)


