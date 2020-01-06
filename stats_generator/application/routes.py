'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request
from application import app
from random import randint
import requests

@app.route('/servce3', methods = ["POST"])
def generate_band_info():
    band = request.get_json()
	app.logger.info(f"Package received \n Contents: {band}")

    weighted_max = [5] * 20 + [10] * 4 + [20] * 1

    num_of_members = randint(2, weighted_max[randint(0, len(weighted_max)-1)])
    popularity = randint(1, 101)
    pretentiousness = randint(1, 101)

    stats = { "number of members" : num_of_members,
    		"popularity" : popularity,
                "pretentiousness" : pretentiousness }

    band.update(stats)

    requests.post("http://localhost:5004/service4", json = band)
    app.logger.info(f"Package sent to service 4 \n Contents: {band}")

@app.route('/service3/health-check', methods = ['GET'])
def health_check():
    return "OK"
