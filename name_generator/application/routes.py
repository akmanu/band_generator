'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request
from application import app, words
from random import randint
import requests

@app.route('/service2', methods = ["GET"])
def generate_band_info():
    # Generate Band Name
    if randint(0,1) == 0:
        band_name = f"{words.get_adjective('band')} {words.get_noun('band')}"
    else:
        band_name = f"The {words.get_adjective('band')} {words.get_noun('band')}"

    if randint(0,1) == 0 and band_name != "Fish":
        band_name = band_name + "s"

    # Generate Genre
    if randint(0,1) == 0:
        genre = f"{words.get_adjective('genre')} {words.get_noun('genre')}"
        if randint(0,5) == 0:
            genre = f"{genre}-{words.get_noun('genre')}"
        else:
            genre = f"{words.get_noun('genre')} {words.get_noun('genre')}"

    band = { "name" : band_name, "genre" : genre }

    requests.post("http://localhost:5003", json = band)
    print("Band info sent to service 3")

    return "Request received"

@app.route('/service2/health-check', methods = ['GET'])
def health_check(): 
    return f"{words.get_adjective('band')} {words.get_noun('band')}"
