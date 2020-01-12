'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request, jsonify
from application import app
from random import randint
import requests

@app.route('/service3/get_package', methods = ["GET"])
def generate_band_info():
    app.logger.info(f"Package request received")

    weighted_max = [5] * 20 + [10] * 4 + [20] * 1

    num_of_members = randint(2, weighted_max[randint(0, len(weighted_max)-1)])
    popularity = randint(1, 101)
    pretentiousness = randint(1, 101)

    stats = { "number of members" : num_of_members,
    		"popularity" : popularity,
            "pretentiousness" : pretentiousness }

    app.logger.info(f"Package sent to service 4 \n Contents: {stats}")
    return jsonify(stats)

@app.route('/service3/health-check', methods = ['GET'])
def health_check():
    return "OK"

@app.route('/service3/coveragereport')
def coverage_report():
    return render_template('coverage.html', title = 'Coverage Report')
