# Doing __init__ becomes a python package
    # This means by default, if we import the name of the folder, it'll run everything in the __init__.py file
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # --> __name__ represents name of file ran
    app.config['SECRET_KEY'] = 'random ass string' # Secret key for our developer side
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')  # url_prefix makes it so everything has to be prefixed. If we had auth.route('hello'), we'd access that route by /auth/hello
    app.register_blueprint(auth, url_prefix = '/') 

    from .models import User, Note  # Make sure it defines our classes first, before we create our databases

    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app = app)   # Need to make sure app is the correct one --> SQLALCHEMY_DATABASE_URI...
        print('Created Database!')
