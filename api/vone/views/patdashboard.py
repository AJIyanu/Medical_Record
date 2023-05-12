#!/usr/bin/env python3
""" Module of Index views
"""
from flask import abort, render_template, request
from views import app_views
from views.signinout import auth


@app_views.route('/patient/<userid>', methods=['GET'], strict_slashes=False)
def patdashboard(userid):
    """loads doctor dashbord"""
    res = request
    cookie = str(res.cookies.get("session_id")).split('.')[0]
    email = str(res.cookies.get("email"))
    if not auth.validate_login(email, cookie):
        abort(403)
    patient = auth.get_staff(userid)
    return render_template("patient.html", **patient)
