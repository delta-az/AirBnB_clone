#!/usr/bin/python3
"""Defines the state model"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
