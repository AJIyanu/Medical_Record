#!/usr/bin python3
"""
section loads local json object and returns json data
"""
from pathsapp import app_views
from flask import render_template, request, redirect, jsonify
import json


@app_views.route('/states', methods=['GET'])
def statesobj():
    """returns list of states object"""
    with open("states.json", "r") as file:
        all_states = json.loads(file.read())
    states = [state['states']['name'] for state in all_states ]
    return jsonify(states)


@app_views.route('/lga/<state>', methods=['GET'])
def lgaobj(state):
    """returns list of lga onject according to state"""
    with open("states.json", "r") as file:
        all_states = json.loads(file.read())
    for states in all_states:
        if state == states['states']['name']:
            lga = [lga['name'] for lga in states['states']['locals'] ]
    return jsonify(lga)
