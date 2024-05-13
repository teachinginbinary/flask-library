from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='../templates')  # Asegúrate de especificar el directorio de templates si es necesario

@main.route('/')
def home():
    return render_template('auth/home.html') # app_flask/templates/auth/home.html
