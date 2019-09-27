from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Password',validators = [Required(),EqualTo('password_confirm',message = 'Password doesnot match')])
    password_confirm = PasswordField('Confirm Passwords',validators=[Required()])
    Submit = SubmitField('Sign up')

    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('That email exists')
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That name exists')

class LoginForm(FlaskForm):
    email=StringField('Enter your email',validators=[Required(),Email()])
    username = StringField('Your UserName',validators=[Required()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')