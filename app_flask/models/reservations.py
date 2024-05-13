from app_flask import db

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('reservations', lazy=True))
    book = db.relationship('Book', backref=db.backref('reservations', lazy=True))

