#!/usr/bin/env python3
"""
This module contains:
    - instantiation of the Babel object in my app
    - Configuration of available languages in our app
      by creating a Config class
"""
from flask_babel import Babel
from flask import Flask


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    This class configures available languages in
    our app
    """
    LANGUAGES = ["en", "fr"]
    babel.BABEL_DEFAULT_LOCALE = "en"
    babel.BABEL_DEFAULT_TIMEZONE = "UTC"
