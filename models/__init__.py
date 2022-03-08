#!/usr/bin/python3
""" Module that imports FileStorage from the file_store """


import imp
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
