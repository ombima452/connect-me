from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField,PasswordField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    pass