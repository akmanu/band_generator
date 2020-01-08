'''
Python file that handles hyperlink routing within the site
'''
from flask import render_template, redirect, url_for, request, jsonify
from application import app, words
from random import randint
import requests

@app.route('/service4', methods = ["GET", "POST"])
def generate_band_info():
    app.logger.info(f"Request received from service 1")

    response_service2 = requests.get("http://name_generator:5002/service2")
    band = response_service2.json()
    app.logger.info(f"Package received from service 2 \n Contents: {band}")
    
    reponse_service3 = requests.get("http://stats_generator:5003/service3")
    stats = response_service3.json()
    app.logger.info(f"Package received from service 3 \n Contents: {stats}")
    
    band.update(stats)
    app.logger.info(f"Band: {band}")
    
    '''
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
    '''
    return jsonify(band)

@app.route('/service4/health-check', methods = ['GET'])
def health_check():
    return f"{words.get_name('forename', 'male', 60)} {words.get_name('forename', 'female', 60)}"
