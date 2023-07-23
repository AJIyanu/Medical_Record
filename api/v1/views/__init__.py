#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from views.login import *
from views.vitalsign import *
from views.forms import *
from views.fetchdata import *
# from views.signinout import *
# from views.docdashboard import *
# from views.patdashboard import *
# from views.register import *
# #from users import *
# #from session_auth import *
