from pathsapp import app_views
from flask import render_template, request, redirect, url_for
import base64

@app_views.route('/dashboard/<user>', methods=['GET'])
def dashboard(user):
    """returns the sign in page"""
    if request.cookies.get('nin'):
        nin = request.cookies.get('nin')
        nin = base64.b64decode(nin).decode('utf-8')
        print(nin)
        return render_template("{}_dashboard.html".format(user), nin=nin)
    return redirect(url_for("app_views.login"))
