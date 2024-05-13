from flask import Blueprint, redirect, url_for, render_template, Response
from flask_login import login_required, current_user
from app_flask.models.book import Book
from app_flask.models.reservations import Reservation
from app_flask.utils.create_pdf import create_pdf
from app_flask import db

dashboard = Blueprint('dashboard', __name__, template_folder='../templates')

@dashboard.route('/reserve_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def reserve_book(book_id):
    book = Book.query.get_or_404(book_id)
    existing_reservation = Reservation.query.filter_by(user_id=current_user.id).first()
    if existing_reservation:
        return redirect(url_for('dashboard.my_dashboard', error='Ya has reservado un libro. No puedes reservar más de un libro.'))
    reservation = Reservation(user_id=current_user.id, book_id=book.id)
    db.session.add(reservation)
    db.session.commit()
    return redirect(url_for('dashboard.my_dashboard'))

@dashboard.route('/delete-reservation/<int:reservation_id>', methods=['GET', 'POST'])
@login_required
def delete_reservation(reservation_id):
    # Buscar la reserva por su ID
    reservation = Reservation.query.get_or_404(reservation_id)
    
    # Verificar si la reserva pertenece al usuario actual
    if reservation.user_id!= current_user.id:
        return redirect(url_for('main.home', error='No tienes permiso para eliminar esta reserva.'))

    # Eliminar la reserva de la base de datos
    db.session.delete(reservation)
    db.session.commit()

    # Redirigir al usuario a la página principal
    return redirect(url_for('main.home'))

@dashboard.route('/dashboard', methods=['GET', 'POST'])
@login_required
def my_dashboard(): 
    reservations = Reservation.query.filter_by(user_id=current_user.id).all()
    # Obtiene los libros correspondientes a las reservaciones
    books = [reservation.book for reservation in reservations]
    return render_template('dashboard/dashboard.html', books=books)

@dashboard.route('/download_book/<int:book_id>', methods=['GET', 'POST'])
@login_required
def download_book(book_id):
    book = Book.query.get_or_404(book_id)
    pdf_buffer = create_pdf(book)
    response = Response(pdf_buffer.getvalue(), mimetype='application/pdf')
    response.headers.set('Content-Disposition', f'attachment; filename={book.name}.pdf')
    return response