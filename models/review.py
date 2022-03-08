#!/usr/bin/python
""" Class Review """


from models.base_model import BaseModel


class Review(BaseModel):
    """ Representation of a Review """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initializes Review """

        super().__init__(*args, **kwargs)
