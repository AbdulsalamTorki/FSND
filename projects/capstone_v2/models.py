from sqlalchemy import Column, String, create_engine, Integer, Date
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):
  __tablename__ = 'People'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}


'''
Person
Have title and release year
'''
class Movie(db.Model):
  __tablename__ = 'Movie'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(Date)

  def __init__(self, title, release_date=""):
    self.title = name
    self.release_date = release_date

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'catchphrase': self.release_date}


'''
Person
Have title and release year
'''
class Actor(db.Model):
  __tablename__ = 'Actor'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  gender = Column(String)
  age = Column(String)

  def __init__(self, gender,name, age=""):
    self.name = name
    self.gender = gender
    self.age = age

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'gender': self.gender,
      'catchphrase': self.age}