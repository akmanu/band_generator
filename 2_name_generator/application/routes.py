'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request, jsonify
from application import app, words
from random import randint
import requests

@app.route('/service2/get_package', methods = ["GET"])
def generate_band_info():
    app.logger.info("Package request received")
	# Generate Band Name
    if randint(0,1) == 0:
        band_name = f"{words.get_word('adjective', 'band')} {words.get_word('noun','band')}"
    else:
        band_name = f"The {words.get_word('adjective', 'band')} {words.get_word('noun', 'band')}"

    if randint(0,1) == 0 and band_name != "Fish":
        band_name = band_name + "s"

    # Generate Genre
    if randint(0,1) == 0:
        genre = f"{words.get_word('adjective', 'genre')} {words.get_word('noun', 'genre')}"
        if randint(0,5) == 0:
            genre = f"{genre}-{words.get_word('noun', 'genre')}"
    else:
        genre = f"{words.get_word('noun', 'genre')} {words.get_word('noun', 'genre')}"

    band = { "name" : band_name, "genre" : genre }

    app.logger.info(f"Package sent to service 4 \n Contents: {band}")
    return jsonify(band)

@app.route('/service2/health-check', methods = ['GET'])
def health_check(): 
    return f"{words.get_word('adjective','band')} {words.get_word('noun', 'band')}"

@app.route('/service2/coveragereport')
def coverage_report():
    return render_template('coverage.html', title = 'Coverage Report')
