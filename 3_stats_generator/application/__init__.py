'''
Main flask file to be run to start the app
Requires environment variables to be set in order to run
'''
from flask import Flask, render_template

app = Flask(__name__)

from application import routes
