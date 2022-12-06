from flask import Blueprint,render_template


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/signup' , methods=['POST', 'GET'])
def signup():
    return render_template("signup.html")

