#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file
from views import app_views


#app.template_folder = 'Medical_Record/web_pages'

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/home', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - returns home page
    """
    return render_template("home.html")


@app_views.route('/signup', strict_slashes=False)
def sign_up() -> str:
    """ GET /api/v1/stats
    Return:
      - returns signup page
    """
    return render_template("signin_up.html")

@app_views.route('/way', strict_slashes=False)
def waypage():
    """returns way page"""
    return render_template("way.html")


@app_views.route("/gpt", strict_slashes=False)
def gpt():
    """test page"""
    return render_template("gpt.html")


@app_views.route("/temp", strict_slashes=False)
def templatess():
    """test temp page"""
    return render_template("temp.html")


@app_views.route("/dyn/<dynamic>", strict_slashes= False)
def dyn(dynamic):
    """temolates templates"""
    temp = f"tests/{dynamic}.html"
    return render_template(temp)

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """test error 401"""
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """test error 403"""
    abort(403)
