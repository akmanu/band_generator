'''
Provides web forms built using WTForms.
Basic user sign up form has been provided for reference.
'''
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, FloatField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application import db, bcrypt

class GenerateBandButton(FlaskForm):
    submit = SubmitField('Generate Band')
