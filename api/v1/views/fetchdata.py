#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file
from sqlalchemy.orm.exc import NoResultFound
from views import app_views
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_jwt_extended import get_jwt, create_refresh_token

@app_views.route("/id_from_nin/<nin>", methods=['GET'])
@jwt_required()
def nin(nin):
    """returns user id based on nin"""
    from models.base_person import Person
    try:
        user = Person.user_by_nin(nin)
    except ValueError as msg:
        return jsonify(error=msg), 401
    except NoResultFound:
        return jsonify(error="user does not exist"), 401
    return jsonify(user=user.get('id'))


@app_views.route("/user_from_nin/<nin>", methods=['GET'])
@jwt_required()
def user_nin(nin):
    """returns user data from on nin"""
    from models.base_person import Person
    try:
        user = Person.user_by_nin(nin)
    except ValueError as msg:
        return jsonify(error=msg), 401
    except NoResultFound:
        return jsonify(error="user does not exist"), 401
    staff_id = get_jwt_identity()
    return jsonify(patient_data=user, staff_id=staff_id)
