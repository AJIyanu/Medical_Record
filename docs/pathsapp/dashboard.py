from pathsapp import app_views
from flask import render_template
from flask_login import login_required

@app_views.route('/dashboard/<user>', methods=['GET'])
@login_required
def dashboard(user):
    """returns the sign in page"""
    return render_template("{}_dashboard.html".format(user))
