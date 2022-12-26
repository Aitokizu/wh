from app import app, db
from flask import render_template, request, redirect, url_for
from models import User


@app.route('/')
def hello_world():  # put application's code here
   return 'Hello World!'


@app.route('/create', methods=['GET', 'POST'])
def create_user():
   if request.method == 'POST':
       user = User(
           rating_book_number=request.form['rating_book_number'],
           last_name=request.form['last_name'],
           name=request.form['name'],
           patronymic=request.form['patronymic'],
           age=request.form['age'],
           faculty=request.form['faculty'],
           course=request.form['course'])

       user_test = User.query.filter_by(rating_book_number=user.rating_book_number).first()
       if user_test is None:
           db.session.add(user)
           db.session.commit()

       result = db.engine.execute('SELECT * FROM user').all()
   return render_template('/create.html', result=' ||| '.join(str(i) for i in result))
