# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicialización de SQLAlchemy y LoginManager fuera de la función create_app()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    # Asociar db y login_manager con la aplicación Flask
    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    from app_flask.routes.main import main
    from app_flask.routes.auth import auth
    from app_flask.routes.books import books
    from app_flask.routes.dashboard import dashboard
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(books)
    app.register_blueprint(dashboard)

    return app
