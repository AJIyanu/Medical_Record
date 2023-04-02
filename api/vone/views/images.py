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


@app_views.route('/images/appointment', methods=['GET'], strict_slashes=False)
def appointment_file():
    """sends css file"""
    return send_file("../../web_pages/static/images/book appointment.jpg")


@app_views.route('/<user>/images/dyn/<dynamic>', methods=['GET'], strict_slashes=False)
def dynamicjpg(user, dynamic):
    """sends css file"""
    jpg = f"../../web_pages/static/images/{dynamic}.jpg"
    png = f"../../web_pages/static/images/{dynamic}.png"
    try:
        return send_file(jpg)
    except Exception:
        return send_file(png)
