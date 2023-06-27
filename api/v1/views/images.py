#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file
from views import app_views


@app_views.route('/images/<img>', methods=['GET'], strict_slashes=False)
def image_file(img):
    """sends css file"""
    try:
        return send_file(f"../../web_pages/static/images/{img}.png")
    except FileNotFoundError:
        return send_file(f"../../web_pages/static/images/{img}.jpg")


@app_views.route('/<user>/images/dyn/<dynamic>', methods=['GET'], strict_slashes=False)
def dynamicjpg(user, dynamic):
    """sends css file"""
    jpg = f"../../web_pages/static/images/{dynamic}.jpg"
    png = f"../../web_pages/static/images/{dynamic}.png"
    try:
        return send_file(jpg)
    except Exception:
        return send_file(png)
