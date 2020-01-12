'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request
from application import app
from application.forms import GenerateBandButton
from os import getenv
import requests

# Route to home page
@app.route("/home", methods = ["GET", "POST"])
def home():
	build_id = getenv("BUILD_ID")
	# button to generate a random number
	generate_band = GenerateBandButton()
	
	if request.method == "GET":
		band = {"name" : "",
			"genre" : "",
			"number of members" : "",
			"popularity" : "",
			"pretentiousness" : "",
			"members" : [""]}

	# send request to name_generator to begin generating when button is pressed
	if generate_band.is_submitted():
		response = requests.get("http://members_generator:5000/service4/get_package")
		band = response.json()
		app.logger.info(f"Package requested")

	return render_template("index.html", title = "Home", band = band, generate_band = generate_band)

@app.route("/home/health-check", methods=["GET"])
def health_check():
        return "OK"

@app.route('/home/coveragereport')
def coverage_report():
    return render_template('coverage.html', title = 'Coverage Report')
