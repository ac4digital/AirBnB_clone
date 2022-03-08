#!/usr/bin/python
""" Class User"""


from models.base_model import BaseModel


class User(BaseModel):
    """ Representation of a User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initializes user """
        super().__init__(*args, **kwargs)
