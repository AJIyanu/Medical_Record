from pathsapp import app_views
from flask import render_template

@app_views.route('/signin', methods=['GET'])
def signinup():
    """returns the sign in page"""
    return render_template("signin.html")
