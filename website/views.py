# Store roots of where the users can go to (login page, etc anything user can navigate to) 
from flask import Blueprint, render_template # Blueprints just means bunch of URLS

views = Blueprint('views', __name__)

@views.route('/')    # Decorator defined with roots and whatever's inside home will run
def home():
    return render_template("home.html")