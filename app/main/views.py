from flask_login import login_required,current_user
from flask import redirect,render_template,url_for
from . import main
from .. import db

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('home.html')