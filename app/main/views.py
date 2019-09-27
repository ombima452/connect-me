from flask_login import login_required,current_user
from . import main
from app.models import Post,Comments
from . forms import PostForm,CommentForm
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from .forms import UpdateProfile
from .. import db,photos


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('home.html')
