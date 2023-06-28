#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from views import app_views
from models.loginauth import PersonAuth
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
