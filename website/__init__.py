from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy() #creates the sqlalchemy object
DB_NAME = "database.db" 

def create_app():
    app = Flask(__name__) #creates the flask object
    app.config['SECRET_KEY'] = 'dev' #Setting config settings for the app
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #stores the location of the db in the flask config
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    db.init_app(app) #initialsing the app

    
    from .views import views #importing the views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #settings routes for the views
    app.register_blueprint(auth, url_prefix='/')

    from . import models #importing the database structure 

    create_database(app) #Running my create databse function and passing in the app object

    login_manager = LoginManager()   # creating the login manager object
    login_manager.login_view = 'auth.login' #Telling the the object where the login page is
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME): #If there is no db already
        db.create_all(app=app) #create db
        import100words(db, app) # populate db
        print('Created Database!')

def import100words(db, app): # A simple to populate the db with some words to test with
    from . import models
    from . import data
    for each in data.a:
        with app.app_context():
            db.session.add(models.Word(data=each))
            db.session.commit()