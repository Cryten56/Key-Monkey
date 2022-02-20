from flask import Blueprint, request, flash, redirect, url_for
from flask.templating import render_template
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])  # associates the URL with the login() function
def login():
    if request.method == 'POST': 
        # A post request takes data from the site to the server
        # It occurs 
        email = request.form.get('email') # retrieves the text from the form
        password = request.form.get('password1')

        user = User.query.filter_by(email=email).first() # Retrieves that user from the database, using email
        if user:
            if check_password_hash(user.password, password): 
                # Checks the password is the same as the on in the 
                #database
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) # Logs the user in, keeps them logged in between sessions 
                return redirect(url_for('views.home')) # Takes them to the home page
            else:
                flash('Incorrect password, try again.', category='error') 
                # If the password is wrong the flashed messages
                # are shown to the user
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user) 
    # If the request method is get, it renders the login page and 
    # and passes the user object
@auth.route('/logout')
@login_required # You have to be logged in the access this page
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            newUser=User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256')) 
            #encrypts password with sha256
            db.session.add(newUser) # Add the user to the db
            db.session.commit()
            flash('Account created!.', category='success')
            login_user(newUser)
            return redirect(url_for('auth.login'))


    return render_template("sign_up.html", user=current_user)