#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file
from views import app_views


@app_views.route('/images/mylogo', methods=['GET'], strict_slashes=False)
def image_file():
    """sends css file"""
    return send_file("../../web_pages/static/images/my logo.png")


@app_views.route('/images/stethoscope', methods=['GET'], strict_slashes=False)
def stethoscope_fileII():
    """sends steth file"""
    return send_file("../../web_pages/static/images/stethoscope.png")


@app_views.route('/images/patient', methods=['GET'], strict_slashes=False)
def patient_file():
    """sends patient file"""
    return send_file("../../web_pages/static/images/patient.png")


@app_views.route('/images/homepage', methods=['GET'], strict_slashes=False)
def homepage_file():
    """sends homepage file"""
    return send_file("../../web_pages/static/images/homepage.jpg")
