from . import db # We access our db in  __init__.py
from flask_login import UserMixin # Gives our user object some things specific things (Just a module that helps us log users in)
from sqlalchemy.sql import func 

class Note(db.Model):
    # Blueprint. All notes need to look like this (consistency)
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now()) # Automatically add date for us using func, which will get whatever time it is (from sqlalchemly.sql)

    # db.ForeignKey --> one user has many nodes. Must pass valid id of existing user to this column
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # Need to match id parameter of db.Integer



class User(db.Model, UserMixin):
    # Blueprint. All users need to look like this (consistency)
    id = db.Column(db.Integer, primary_key = True)   # primary_key is unique indentifer so not everyone has the same ID
    email = db.Column(db.String(150), unique = True) # No user can have the same email as the one that already exists
    password = db.Column(db.string(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')        # Everytime we create a Note, we add Note_ID. List that stores all different notes. Can access all Notes from User (Reference name of class)

