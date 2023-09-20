#!/usr/bin/python3
"""
all routes added here and functions imported here
"""

from importlib import import_module
from flask import Blueprint

app_view = Blueprint("app_view", __name__)

from .pages import *
