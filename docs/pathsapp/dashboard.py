from pathsapp import app_views
from flask import render_template

@app_views.route('/dashboard/<user>', methods=['GET'])
def dashboard(user):
    """returns the sign in page"""
    return render_template("{}_dashboard.html".format(user))
