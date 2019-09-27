
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,TextAreaField,RadioField
from wtforms.validators import Required
from wtforms import ValidationError

class PostForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    age = StringField('Age', validators = [Required()])
    gender = RadioField('Gender',choices=[('Male','Male'),('Female','Female')])
    description = TextAreaField('Write more information',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name =StringField('Name',validators=[Required()])
    number = StringField('Your Number',validators=[Required()])
    comment = TextAreaField('Enter a good description', validators=[Required()])
    Submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

