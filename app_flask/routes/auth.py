from flask import Blueprint, request, render_template, jsonify, redirect, url_for, make_response
from flask_login import login_user, login_required, logout_user
from app_flask.models.user import User, db

auth = Blueprint('auth', __name__, template_folder='../templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET': 
        return render_template('auth/signup.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=password)
        existingUser = User.query.filter_by(username=username).first()

        if existingUser:
            return jsonify({'error': 'El usuario ya existe'}), 400
        
        if User.query.count() == 0: 
            user.is_special = True

        db.session.add(user)
        db.session.commit()

        login_user(user)
        return jsonify({'success': True}), 200  # Devuelve una respuesta JSON de éxito
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET': 
        return render_template('auth/login.html')
    else: 
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if not user or not user.password == password: 
            return jsonify({'error': 'Usuario o contraseña incorrectos'}), 400

        login_user(user)
        return jsonify({'success': True}), 200  # Devuelve una respuesta JSON de éxito
        
@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
