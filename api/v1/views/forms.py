#!/usr/bin/env python3
""" Module of Index views
"""
from views import app_views
from datetime import datetime
from flask_jwt_extended import jwt_required
from flask import render_template, request, redirect, jsonify

@app_views.route("/vitalsign", methods=["POST"])
@jwt_required()
def vitalsign():
    """returns vitalsign"""
    details = request.json
    from views.register_function import new_vitalsign
    status = new_vitalsign(**details)
    if "error" in status:
        return jsonify(status=status), 400
    return jsonify(status=status), 200

@app_views.route("/casefile", methods=['POST'])
@jwt_required()
def casefile():
    """saves casefile and return status"""
    details = request.json
    from views.register_function import new_casefile
    status = new_casefile(**details)
    if "error" in status:
        return jsonify(status=status), 400
    return jsonify(status=status), 200


@app_views.route("/signup", methods=["POST"])
def register():
    user_data = request.json
    user_data["dob"] = datetime.strptime(user_data['dob'], "%Y-%m-%d")
    if user_data['user'] == "doctor":
        from views.register_function import register_doctor
        status = register_doctor(**user_data)
    if user_data["user"] == "nurse":
        from views.register_function import register_nurse
        status = register_nurse(**user_data)
    if user_data["user"] == "null":
        from views.register_function import register_patient
        status = register_patient(**user_data)
    return jsonify(status=status)
