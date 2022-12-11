from flask import Flask
from os import path
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import flask_login


db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hector'

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=5)
    
    db.init_app(app)


    from .views import views
    from .auth import auth 
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()

    
        print('Created Database!')

