#!/usr/bin/env python3
"""
Route module for web pages
"""
from os import getenv
from pathsapp import app_views
from flask import Flask, jsonify, abort, request
import os


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'roseismysecretkey'


@app.before_request
def handle_before():
    """handles stuff before request is made"""
    pass


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """handling unauthorized shits"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """authorized but not aloowed"""
    return jsonify({"error": "Forbidden"}), 403

if __name__ == "__main__":
    host = getenv("WEBDOC_HOST", "0.0.0.0")
    port = getenv("WEBDOC_PORT", "5001")
    app.run(host=host, port=port, debug=True)
