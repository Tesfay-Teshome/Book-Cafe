from flask import Blueprint,render_template,request,flash,url_for,redirect
from ..extentions import db
from bookcafe.model.users import User
from flask_login import current_user, login_required
from bookcafe.model.books import Book
from bookcafe.model.categories import Category



view = Blueprint('view', __name__)

# @view.route('/')
# @login_required
# def index():
#     return render_template('index.html', user=current_user)

@view.route('/books', methods=['GET','POST'])
def books():
    if request.method == 'GET':
        all_book = Book.query.order_by(Book.id)

        return render_template("books.html", user=current_user, all_book=all_book)
    return render_template('books.html', user=current_user)

@view.route('/addbooks', methods=['GET','POST'])
def addbooks():
    categories = Category.query.all()
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        category_id = request.form.get('cat')
        description = request.form.get('description')
        new_book = Book( title = title, author = author, description= description, category = category_id)
        db.session.add(new_book)
        db.session.commit()
        flash('added successfull', category='success')
        return redirect(url_for('view.books',user=current_user))


    return render_template('addbooks.html', categories=categories, user=current_user)

@view.route('/book/<string:id>', methods=['GET','POST'])
def single_book(id):
    if request.method == 'GET':
        single_book = Book.query.filter_by(id=id).first()
        return render_template("book.html", user=current_user, book=single_book)
