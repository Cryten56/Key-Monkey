from cgi import test
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
        listOfWordTuples = db.session.query(Word.data).order_by(func.random()).limit(25).all() # Returns a list of 20 words [('word',), ('word2,',),"('word3',)]
        listOfWordsJSON = json.dumps(list(map(lambda word: word[0], listOfWordTuples))) # Returns a list of 20 words as JSON string '["word", "word2", "word3"]'
        return render_template("home.html", user=current_user, sentence=listOfWordsJSON)
    elif request.method == 'POST': 
        data = request.form['theData'] 
        data = json.loads(data)
        newTest = Test(userId = current_user.id, unixTime=int(time.time()), testTime=data['testTime'], speed=int(round(data['testSpeed'], 0)), rawSpeed = int(round(data['testRawSpeed'], 0)), accuracy= int(round(data['testAcc'], 0)))
        listOfSqlalchemyTestWords = list(map(lambda x: convert_processed_test(x[0], x[1]), enumerate(data['processedTest'])))
        newTest.testWordLetters.extend(listOfSqlalchemyTestWords)
        db.session.add(newTest) 
        db.session.commit()
        session['testId'] = newTest.id
        return redirect(url_for('views.results'))

    return render_template("home.html", user=current_user)

@views.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    testId = session['testId']
    wordsResults = db.session.query(TestWord).filter(TestWord.testId == int(testId)).order_by(TestWord.wordNum).all()
    wordsResults = list(map(query_object_to_dict, wordsResults))
   
    wordsResults = list(map(add_correct_word, wordsResults))
    wordLetters = [None] * len(wordsResults)
    for word in wordsResults:
        lettersinWord = db.session.query(TestWordLetter).filter(TestWordLetter.testWordId == int(word['id'])).order_by(TestWordLetter.charNum).all()
        lettersinWord = list(map(query_object_to_dict, lettersinWord))
        wordLetters[word['wordNum']-1] = lettersinWord
    testData = list(map(lambda words, letters: {'wordData': words, 'letterdata': letters}, wordsResults, wordLetters))
    testStats = db.session.query(Test).filter(Test.id == int(testId)).first()
    testStats = testStats.__dict__
    del testStats['_sa_instance_state']
    del testStats['dateTime']
    testData = {'wordStats': testData, 'testStats': testStats}
    testData = json.dumps(testData)
    return render_template("results.html", user=current_user, results=testData)

@views.route('/results', methods=['GET', 'POST'])
@login_required
def test_setup():
    pass
    
def query_object_to_dict(queryobject):
       toDict = queryobject.__dict__
       del toDict['_sa_instance_state']
       return  toDict

def add_correct_word(theDict):
    correctWord = db.session.query(Word.data).filter(Word.id==theDict['wordId']).first()
    theDict['correctWord'] = correctWord[0]
    return theDict

def convert_processed_test(index, wordData):
    IdofWord= select(Word.id).where(Word.data == f"{wordData['word']}").scalar_subquery()
    testWordObject = TestWord(wordId = IdofWord, time = wordData['wordTime'], wordNum = (index+1), incorrectWord = wordData['incorrectWord'], typedWord = wordData['typedWord'], wordCorrect = wordData['wordCorrect'])  
    if not(wordData['wordSpeed'] is None):
        testWordObject.speed = int(round(wordData['wordSpeed'], 0))
    listOfSqlalchemyLetterData = list(map(lambda x: convert_processed_letter(x[0], x[1]), enumerate(wordData['letters'])))
    testWordObject.testWordLetter.extend(listOfSqlalchemyLetterData)
    return testWordObject


def convert_processed_letter(index, letterData):
    testWordLetterObject = TestWordLetter(charNum=(index+1), type=letterData['type'], incorrectChar = letterData['incorrectLetter'])
    if "time" in letterData:
        testWordLetterObject.time = letterData['time']
    if "typedLetter" in letterData:
        testWordLetterObject.typedChar = letterData['typedLetter']
    if not(letterData['speed'] is None):
        testWordLetterObject.speed = int(round(letterData['speed'], 0))
    if "correctLetter" in letterData:
        testWordLetterObject.correctCharacter = letterData['correctLetter']
    return testWordLetterObject
