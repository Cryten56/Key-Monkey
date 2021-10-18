from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from flask_login import login_required, current_user
from sqlalchemy.sql.functions import user
from werkzeug.utils import redirect
from .models import User, Note, Word, UserWords
from flask_login import login_required, current_user
from . import db
import json
import os
import random

views = Blueprint('views', __name__)


    
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        listOfWords = []
        sentence = ""
        for i in range(5):
            inte = random.randint(1, 5)
            word = Word.query.filter_by(id=inte).first()
            listOfWords.append(word.data)
        for word in listOfWords: 
            sentence += str(word) + " "
        return render_template("home.html", user=current_user, sentence=sentence)

    return render_template("home.html", user=current_user)



