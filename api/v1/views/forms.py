#!/usr/bin/env python3
""" Module of Index views
"""
from views import app_views
from datetime import datetime
import json
from flask import render_template, request, redirect, jsonify

@app_views.route("/vitalsign", methods=["POST"])
def vitalsign():
    """returns vitalsign"""
    details = request.json
    from views.register_function import new_vitalsign
    status = new_vitalsign(**details)
    return jsonify(status=status)

@app_views.route("/casefile", methods=['POST'])
def casefile():
    """saves casefile and return status"""
    return jsonify({"pass": "not yet implemented"})


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
