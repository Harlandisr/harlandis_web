from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/signin')
def home():
    return "<h1>tEST</h1>"