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


@app_views.route('/<root>', strict_slashes=False)
def rootpages(root) -> str:
    """ GET /<root>
    Return:
      - returns root pages
    """
    return render_template(f"{root}.html")

@app_views.route('/favicon.ico', strict_slashes=False)
def favicon():
    """return favicon"""
    return send_file("../../web_pages/static/images/favicon.ico")


@app_views.route("/dyn/<dynamic>", strict_slashes=False)
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
