from flask import Blueprint,render_template, request, flash 
from bbdd import get_check_email, insert_user 
from flask_login import current_user
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

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
            if get_check_email(email):
                insert_user(name, contrasena1, dni, telefono, email, surname)
                flash('Logged in successfully!', category='success')
                return render_template("signup.html", User_register=current_user)

        
    return render_template("signup.html")

