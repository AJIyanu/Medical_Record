#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file
from views import app_views


@app_views.route('/static/js/signin', methods=['GET'], strict_slashes=False)
def sign_in():
    """sends js signin file"""
    return send_file("../../web_pages/static/js/sign_in.js")


@app_views.route('/doctor/static/js/temp', methods=['GET'], strict_slashes=False)
def temps():
    """sends js temp file"""
    return send_file("../../web_pages/static/js/temp.js")


@app_views.route('/dyn/js/<dynamic>', methods=['GET'], strict_slashes=False)
def script(dynamic):
    """sends js temp file"""
    return send_file(f"../../web_pages/tests/{dynamic}.js")


"""
@app_views.route('/images/stethoscope', methods=['GET'], strict_slashes=False)
def stethoscope_fileII():
    ""sends steth file""
    return send_file("../../web_pages/static/images/stethoscope.png")


@app_views.route('/images/patient', methods=['GET'], strict_slashes=False)
def patient_file():
    ""sends patient file""
    return send_file("../../web_pages/static/images/patient.png")


@app_views.route('/images/homepage', methods=['GET'], strict_slashes=False)
def homepage_file():
    ""sends homepage file""
    return send_file("../../web_pages/static/images/homepage.jpg")

"""
