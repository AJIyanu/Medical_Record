#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


from models.engine.dbstorage import DBStorage

storage = DBStorage()
storage.reload()
