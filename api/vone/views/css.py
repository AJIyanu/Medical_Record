#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file
from views import app_views


@app_views.route('/static/css/<style>', methods=['GET'], strict_slashes=False)
def css_file(style):
    """sends css file"""
    return send_file(f"../../web_pages/static/css/{style}.css")


@app_views.route("/<user>/static/css/<dashcss>", strict_slashes=False)
def tempcss(user, dashcss):
    """tests template css"""
    return send_file(f"../../web_pages/static/css/{dashcss}.css")


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
