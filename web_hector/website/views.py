from flask import Blueprint,render_template, request
from werkzeug.security import generate_password_hash
from .models import Usuario
from ..instance import db

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
                new_user = Usuario(name=name, 
                                    password=generate_password_hash(contrasena1, 
                                    method='sha256'), 
                                    dni=generate_password_hash(dni, 
                                    method='sha256'),
                                    telefono= telefono,
                                    email=generate_password_hash(email, 
                                    method='sha256'),
                                    surname=surname)
                db.session.add(new_user)
                db.session.commit()
        
    return render_template("signup.html")

