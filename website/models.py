from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(21))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    test = db.relationship("Test")

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    dateTime = db. Column(db.DateTime(timezone=True), default=func.now())
    testTime = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    rawSpeed = db.Column(db.Integer)
    accuracy = db.Column(db.Integer)
    testWord = db.relationship("TestWord")
    

class TestWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    testId = db.Column(db.Integer, db.ForeignKey('test.id'))
    wordId = db.Column(db.ForeignKey('word.id'))
    time = db.Column(db.Integer)
    wordNum = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    correct = db.Column(db.Boolean)
    incorrectWord = db.Column(db.String)
    typedWord = db.Column(db.String(21))
    testWordLetter = db.relationship("TestWordLetter")

class TestWordLetter(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    testWordId = db.Column(db.Integer, db.ForeignKey('test_word.id'))
    charNum = db.Column(db.Integer)
    correctCharacter = db.Column(db.String(1))
    time= db.Column(db.Integer)
    speed = db.Column(db.Integer)
    type = db.Column(db.String(10))
    typedChar = db.Column(db.String(1))
    incorrectChar = db.Column(db.String(1))  



    
    

    

