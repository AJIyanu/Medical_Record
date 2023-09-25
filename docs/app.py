#!/usr/bin/env python3
"""
application to render webpages
"""
from os import getenv
import platform
from datetime import timedelta, datetime, timezone


from pageviews import app_view
from flask import Flask, jsonify, render_template, request, send_file
from jinja2.exceptions import TemplateNotFound
from flask_jwt_extended import (JWTManager, get_jwt, get_jwt_identity,
                                create_access_token, set_access_cookies)
from flask_jwt_extended.exceptions import JWTDecodeError, NoAuthorizationError
from jwt.exceptions import InvalidTokenError #NoTokenError


from models import storage

app = Flask(__name__)
app.register_blueprint(app_view)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'roseismysecretkey'
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=2)
app.config['JWT_SECRET_KEY'] = 'roseismysecretekey'
jwt = JWTManager(app)


@app.errorhandler(NoAuthorizationError)
def handle_no_token_error(error):
    """no token error"""
    response = {
        'error': 'NoTokenError',
        'message': 'No JWT token provided.'
    }
    return jsonify(response), 401


@app.after_request
def refresh_expiring_jwts(response):
    """refreshes the jwt token in the browser"""
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            # this wont work because former expiry was added to new
            access_token = create_access_token(identity=get_jwt_identity(),
                                               additional_claims=get_jwt())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


@app.errorhandler(JWTDecodeError)
def handle_jwt_decode_error(error):
    """jwt decode error"""
    response = {
        'error': 'JWTDecodeError',
        'message': 'Failed to decode JWT token.'
    }
    return jsonify(response), 401


@app.errorhandler(InvalidTokenError)
def handle_invalid_token_error(error):
    """invalid token error"""
    response = {
        'error': 'InvalidTokenError',
        'message': 'Invalid access token.'
    }
    return jsonify(response), 401


@app.before_request
def handle_before():
    """handles stuff before request is made"""
    csrf = request.form.get("csrf_token")
    if csrf:
        request.headers['X-CSRF-Token'] = csrf
    # print(request.cookies, request.headers)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

@app.errorhandler(401)
def not_authorized(error) -> str:
    """handling unauthorized shits"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """authorized but not aloowed"""
    return jsonify({"error": "Forbidden"}), 403


@app.route("/", methods=["GET"])
def index():
    """returns the index page"""
    try:
        return render_template(f"index_{platform.system()}.html")
    except TemplateNotFound:
        return f"create a symlink for {platform.system()}"

@app.route("/favicon.ico", methods=["GET"])
def favicon():
    """returns the favicon"""
    return send_file("favicon_light.ico")

@jwt.expired_token_loader
def get_reauthorization(ejwt_header, ejwt_data):
    """return to sign in page for signin"""
    return render_template("signin.html")


if __name__ == "__main__":
    with app.test_request_context():
        print(app.url_map)
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
