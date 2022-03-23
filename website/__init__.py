from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy() #creates the sqlalchemy object
DATABASENAME = "KeyMonkeyDatabase.db" 

def setup():
    app = Flask(__name__) #creates the flask object
    app.config['SECRET_KEY'] = 'dev' #Setting config settings for the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASENAME}' #stores the location of the db in the flask config
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    db.init_app(app) #initialsing the app

    
    from .views import views #importing the views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #settings routes for the views
    app.register_blueprint(auth, url_prefix='/')

    from . import models #importing the database structure 

    initDB(app) #Running my create databse function and passing in the app object
    
    login_manager = LoginManager()   # creating the login manager object  
    
    @login_manager.user_loader
    def login_user(id):
        return models.User.query.get(int(id))

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' #Telling the the object where the login page is



    return app

def initDB(app):
    if not path.exists('website/' + DATABASENAME): #If there is no db already
        db.create_all(app=app) #create db
        import100words(db, app) # populate db


def import100words(db, app): # A simple to populate the db with some words to test with
    from . import models
    from . import data
    for each in data.a:
        with app.app_context():
            db.session.add(models.Word(data=each))
            db.session.commit()