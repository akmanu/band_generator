'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request
from application import app
from random import randint
import requests
import words

@app.route('/', methods = ["POST"])
def generate_band_info():
	band = request.get_json()

	pretentiousness = band['pretentiousness']
	if pretentiousness > 50:
		if randint(0,1) == 0:
			band_name = words.accent_random_vowel(band['name'])
			band['name'] = band_name

		#if math.floor((len(band['name']) + len(band['genre'])) % 3) == 0:
		#	band['name'] = accent_random_vowel(band['name'])

	members = []
	gender = ["male", "female"]
	for _ in range(0, band['number of members']):
		member_gender = gender[randint(0,1)]
		member_name = f"{words.get_name('forename', member_gender, pretentiousness)} {words.get_name('surname', member_gender, pretentiousness)}"
		members.append(member_name)

	members = {"members" : members}
	band.update(members)

	requests.post("localhost:5001", json = band)
