from app_flask import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    cover_photo = db.Column(db.String(255))  # URL de la foto de portada
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=False)
    user = db.relationship('User', backref=db.backref('books', lazy=True))
