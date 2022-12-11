from .. import db 
from ..models import Usuario
from werkzeug.security import generate_password_hash
from flask_login import login_user


def insert_user( name, contrasena, dni, telefono, email, surname):
    """
    def 
        método para insertar un nuevo usuario en la tabla user
    INPUTS
        name -> string \n
        contrasena -> string \n
        dni ->string \n
        telefono -> integer \n
        email -> string \n
        surname ->string \n
    OUTPUTS
        suscessfull -> true \n
        wrong -> false 
    """
    try:
        new_user = Usuario(name=name, 
                            password=generate_password_hash(contrasena, 
                            method='sha256'), 
                            dni=generate_password_hash(dni, 
                            method='sha256'),
                            telefono= telefono,
                            email=email, 
                            surname=surname)
        db.session.add(new_user)
        db.session.commit()
        
        return new_user
    except:
        return False

def get_check_email(email):
    """
    def 
        método para comprobar que no exista un mismo usuario con el mismo email
    INPUTS
        email -> string \n
    OUTPUTS
        suscessfull -> true \n
        wrong -> false 
    """
    try:
        output_email =  Usuario.query.with_entities(Usuario.email).filter_by(email = email)
        if len([x for x in output_email]) > 0: 
            return False
        else: 
            return True
    except:
        return False