'''
Main flask file to be run to start the app
Requires environment variables to be set in order to run
'''
from flask import Flask, render_template
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('MYSQL_SECRETKEY')

from application import routes
