#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__)

from views.login import *
from views.vitalsign import *
# from views.images import *
# from views.js import *
# from views.signinout import *
# from views.docdashboard import *
# from views.patdashboard import *
# from views.register import *
# #from users import *
# #from session_auth import *
