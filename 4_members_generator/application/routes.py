'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request, jsonify
from application import app, words
from random import randint
import requests
    
@app.route('/service4/get_package', methods = ["GET"])
def generate_band_info():
    app.logger.info(f"Request received from service 1")
    
    service2_response = requests.get("http://name_generator:5000/service2/get_package")
    service3_response = requests.get("http://stats_generator:5000/service3/get_package")
    band = service2_response.json()
    app.logger.info(f"Package received from service 2 \n Contents: {band}")
    stats = service3_response.json()
    app.logger.info(f"Package received from service 3 \n Contents: {stats}")
    
    band.update(stats)
    app.logger.info(f"Band: {band}")
    
    pretentiousness = band['pretentiousness']
    if pretentiousness > 50:
        if randint(0,1) == 0:
            band_name = words.accent_random_vowel(band['name'])
            band['name'] = band_name

    members = []
    gender = ["male", "female"]
    for _ in range(0, band['number of members']):
        member_gender = gender[randint(0,1)]
        if randint(0,2) == 0:
            member_name = f"{words.get_name(member_gender, pretentiousness)} {words.get_name('surname', pretentiousness)}-{words.get_name('surname', pretentiousness)}"
        else:
            member_name = f"{words.get_name(member_gender, pretentiousness)} {words.get_name('surname', pretentiousness)}"
        members.append(member_name)

    members = {"members" : members}
    band.update(members)

    app.logger.info(f"Package sent to service 1 \n Contents: {band}")
    
    return jsonify(band)

@app.route('/service4/health-check', methods = ['GET'])
def health_check():
    return f"{words.get_name('male', 60)} {words.get_name('female', 60)}"

@app.route('/service4/coveragereport')
def coverage_report():
    return render_template('coverage.html', title = 'Coverage Report')
