'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request
from application import app, words
from random import randint
import requests

@app.route('/service4', methods = ["GET"])
def generate_band_info():
    app.logger.info(f"Request received from service 1")

	band = requests.post("http://name_generator:5002/service2")
	app.logger.info(f"Package received from service 2 \n Contents: {band}")
	stats = requests.post("http://stats_generator:5003/service3")
	app.logger.info(f"Package received from service 3 \n Contents: {stats}")
	band.update(stats)

    pretentiousness = band['pretentiousness']
    if pretentiousness > 50:
        if randint(0,1) == 0:
            band_name = words.accent_random_vowel(band['name'])
            band['name'] = band_name

    members = []
    gender = ["male", "female"]
    for _ in range(0, band['number of members']):
        member_gender = gender[randint(0,1)]
        member_name = f"{words.get_name('forename', member_gender, pretentiousness)} {words.get_name('surname', member_gender, pretentiousness)}"
        members.append(member_name)

    members = {"members" : members}
    band.update(members)

    app.logger.info(f"Package sent to service 1 \n Contents: {band}")

	return band

@app.route('/service4/health-check', methods = ['GET'])
def health_check():
    return f"{words.get_name('forename', 'male', 60)} {words.get_name('forename', 'female', 60)}"
