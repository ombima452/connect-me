from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message

@auth.route('/my_account',methods = ['GET','POST'])
def my_account():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        user=User(email = registration_form.email.data,username=registration_form.username.data,password = registration_form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message('You are  welcome to connect_me.','email/welcome_user',user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form=registration_form)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
    return render_template('auth/login.html',login_form = login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))