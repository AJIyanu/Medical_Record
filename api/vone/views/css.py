#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file
from views import app_views


@app_views.route('/static/css/home', methods=['GET'], strict_slashes=False)
def css_file():
    """sends css file"""
    return send_file("../../web_pages/static/css/home.css")


@app_views.route("/static/css/signin_up", methods=["GET"], strict_slashes=False)
def signup_css():
    """sign up css"""
    return send_file("../../web_pages/static/css/signin_up.css")


@app_views.route("/static/css/way", methods=["GET"], strict_slashes=False)
def way_css():
    """way css"""
    return send_file("../../web_pages/static/css/way.css")


@app_views.route("/static/css/header", methods=["GET"], strict_slashes=False)
def header_css():
    """header css"""
    return send_file("../../web_pages/static/css/Header.css")


@app_views.route("/static/css/main", methods=["GET"], strict_slashes=False)
def main_css():
    """main css"""
    return send_file("../../web_pages/static/css/main.css")


@app_views.route("/static/css/gpt", strict_slashes=False)
def gptcss():
    """gpt css"""
    return send_file("../../web_pages/static/css/gpt.css")


@app_views.route("/<user>/static/css/temp", strict_slashes=False)
def tempcss(user):
    """tests template css"""
    return send_file("../../web_pages/static/css/temp.css")


@app_views.route("/<user>/static/css/dyn/<dynamic>", strict_slashes=False)
def dynamiccss(user, dynamic):
    """tests template css"""
    css = f"../../web_pages/static/css/{dynamic}.css"
    return send_file(css)


@app_views.route("/dyn/css/<dynamic>", strict_slashes=False)
def dyncss(dynamic):
    """tests template css"""
    css = f"../../web_pages/tests/{dynamic}.css"
    return send_file(css)
