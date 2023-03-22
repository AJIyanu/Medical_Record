#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__)

from views.index import *
from views.css import *
from views.images import *
from views.js import *
#from users import *
#from session_auth import *
