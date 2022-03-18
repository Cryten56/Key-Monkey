from flask import Blueprint, render_template, request, redirect, session
from flask.helpers import url_for
from flask_login import login_required, current_user
from .models import *
from flask_login import login_required, current_user
from . import db
import random
from sqlalchemy.sql.expression import func
import json

views = Blueprint('views', __name__) # creates a blueprint named  views

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        listOfWordTuples = db.session.query(Word.data).order_by(func.random()).limit(10).all() # Returns a list of 20 words [('word',), ('word2,',),"('word3',)]
        listOfWordsJSON = json.dumps(list(map(lambda word: word[0], listOfWordTuples))) # Returns a list of 20 words as JSON string '["word", "word2", "word3"]'
        return render_template("home.html", user=current_user, sentence=listOfWordsJSON)
    elif request.method == 'POST':
        wordsData = request.form['theData'] 
        data = json.loads(wordsData)
        
        session['testData'] = wordsData
        return redirect(url_for('views.results'))

    return render_template("home.html", user=current_user)

@views.route('/results', methods=['GET', 'POST'])
@login_required
def results():

    return render_template("results.html", user=current_user, testData = session['testData'])


