'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request
from application import app
from application.forms import GenerateBandButton
import requests

# Route to home page
@app.route("/server", methods = ["GET", "POST"])
def home():
	# button to generate a random number
	generate_band = GenerateBandButton()

	if request.method == "POST":
		band = request.get_json()
		#return redirect(url_for("home"))
	else:
		band = {"name" : "",
			"genre" : "",
			"number of members" : None,
			"popularity" : None,
			"pretentiousness" : None,
			"members" : [""]}

	# send request to name_generator to begin generating when button is pressed
	if generate_band.is_submitted():
		requests.get("http://localhost:5002/")
		print("Package requested")

	return render_template("index.html", title = "Home", band = band, generate_band = generate_band)

@app.route("/server/health-check", methods=["GET"])
def health_check():
    return "OK"
