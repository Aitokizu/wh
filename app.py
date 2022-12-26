from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iu4.sqlite'
db = SQLAlchemy(app)

from routes import *
from models import User


with app.app_context():
   db.create_all()

if __name__ == '__main__':
   app.run()
