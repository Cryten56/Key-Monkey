from operator import index, le
from flask import Blueprint, render_template, request, redirect, session
from flask.helpers import url_for
from .models import *
from flask_login import login_required, current_user
from . import db
import random
from sqlalchemy.sql.expression import func
import json
from .models import *
import time
from sqlalchemy import *
import functools

views = Blueprint('views', __name__) # creates a blueprint named  views

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        listOfWordTuples = db.session.query(Word.data).order_by(func.random()).limit(1).all() # Returns a list of 20 words [('word',), ('word2,',),"('word3',)]
        listOfWordsJSON = json.dumps(list(map(lambda word: word[0], listOfWordTuples))) # Returns a list of 20 words as JSON string '["word", "word2", "word3"]'
        return render_template("home.html", user=current_user, sentence=listOfWordsJSON)
    elif request.method == 'POST': 
        data = request.form['theData'] 
        print(data)
        data = json.loads(data)
        newTest = Test(userId = current_user.id, unixTime=int(time.time()), testTime=data['testTime'], speed=int(round(data['testSpeed'], 0)), rawSpeed = int(round(data['testRawSpeed'], 0)), accuracy= int(round(data['testAcc'], 0)))
        a =list(map(lambda x: print(x[0]), enumerate(data['processedTest'])))
        listOfSqlalchemyTestWords =list(map(lambda x: convert_processed_test(x[0], x[1]), enumerate(data['processedTest'])))
        newTest.testWord.extend(listOfSqlalchemyTestWords)
        db.session.add(newTest) 
        db.session.commit()
        session['testData'] = data
        return redirect(url_for('views.results'))

    return render_template("home.html", user=current_user)

@views.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    return render_template("results.html", user=current_user, testData = session['testData'])

def convert_processed_test(index, wordData):
    IdofWord= select(Word.id).where(Word.data == f"{wordData['word']}")
    testWordObject = TestWord(wordId = IdofWord, time = wordData['wordTime'], wordNum = (index+1), incorrectWord = wordData['incorrectWord'], typedWord = wordData['typedWord'], wordCorrect = wordData['wordCorrect'])  
    print(type(wordData['wordSpeed']))
    if not(wordData['wordSpeed'] is None):
        testWordObject.speed = int(round(wordData['wordSpeed'], 0))
    listOfSqlalchemyLetterData = list(map(lambda x: convert_processed_letter(x[0], x[1]), enumerate(wordData['letters'])))
    testWordObject.testWordLetter.extend(listOfSqlalchemyLetterData)
    return testWordObject


def convert_processed_letter(index, letterData):
    # if letterData['time']:
    testWordLetterObject = TestWordLetter(charNum=(index+1), correctCharacter = letterData['correctLetter'], type=letterData['type'], incorrectChar = letterData['incorrectLetter'])
    if "time" in letterData:
        testWordLetterObject.time = letterData['time']
    if "typedLetter" in letterData:
        testWordLetterObject.typedChar = letterData['typedLetter']
    if not(letterData['speed'] is None):
        testWordLetterObject.speed=int(round(letterData['speed'], 0))
    return testWordLetterObject