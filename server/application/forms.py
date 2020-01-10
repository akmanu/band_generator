'''
Provides web forms built using WTForms.
Basic user sign up form has been provided for reference.
'''
from flask_wtf import FlaskForm
from wtforms import SubmitField

class GenerateBandButton(FlaskForm):
    submit = SubmitField('Generate Band')
