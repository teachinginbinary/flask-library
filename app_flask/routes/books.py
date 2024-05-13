from flask import Blueprint, render_template, redirect, url_for, request
from app_flask.models.book import Book
from app_flask import db
from flask_login import login_required, login_required, current_user

books = Blueprint('books', __name__, template_folder='../templates')

@books.route('/books', methods=['GET', 'POST'])
@login_required
def all_books(): 
    return render_template('books/books.html', books=Book.query.all())

@books.route('/create-books', methods=['GET', 'POST'])
@login_required
def create_books():
    if not current_user.is_special: 
        return redirect(url_for('main.home', error='Login with a Admin Account'))
    if request.method == 'GET': 
        return render_template('books/create-books.html')
    else: 
        name = request.form.get('name')
        description = request.form.get('description')
        text = request.form.get('text') 
        cover_photo = request.form.get('cover_photo')
        book = Book(name=name, description=description, text=text, cover_photo=cover_photo, user_id=current_user.id) 
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books.all_books'))

@books.route('/delete-book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    if not current_user.is_special: 
        return redirect(url_for('main.home', error='Login with a Admin Account'))
    else: 
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('books.all_books'))
