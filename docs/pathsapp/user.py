#!/usr/bin/env python3
"""
User module to manage login permission
"""


from flask_login import UserMixin

class User(UserMixin):
    """user class"""

    def __init__(self, **attr) -> None:
        """
        creates temp User for flask Login
        """
        for key in attr:
            setattr(self, key, attr[key])

    def setme(self, key, value):
        """sets other attributes"""
        self.__setattr__(key, value)

    def to_dict(self):
        """returns a dict, no access_token"""
        me = self.__dict__
        me.pop("access_token")
        return me
