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
    test = db.relationship("Test", backref="user")


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    dateTime = db.Column(db.DateTime(timezone=True), default=func.now())
    unixTime = db.Column(db.Integer)
    testTime = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    rawSpeed = db.Column(db.Integer)
    accuracy = db.Column(db.Integer)
    testWordLetters = db.relationship("TestWord", back_populates="test")
    

class TestWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    testId = db.Column(db.ForeignKey('test.id'))
    wordId = db.Column(db.ForeignKey('word.id'))
    time = db.Column(db.Integer)
    wordNum = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    incorrectWord = db.Column(db.String(21))
    typedWord = db.Column(db.String(21))
    wordCorrect = db.Column(db.Boolean)
    testWordLetter = db.relationship("TestWordLetter", back_populates="tests")
    test = db.relationship("Test", back_populates="testWordLetters")


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
    tests = db.relationship("TestWord", back_populates="testWordLetter")



    
    

    

