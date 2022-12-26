from app import db


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
   rating_book_number = db.Column(db.Integer, nullable=False)
   last_name = db.Column(db.String(80), nullable=False)
   name = db.Column(db.String(80), nullable=False)
   patronymic = db.Column(db.String(80), nullable=False)
   age = db.Column(db.Integer, nullable=False)
   faculty = db.Column(db.String(80), nullable=False)
   course = db.Column(db.Integer, nullable=False)

   def __repr__(self):
       return '<User %r>' % self.username
