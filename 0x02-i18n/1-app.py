#!/usr/bin/env python3
"""
This module contains:
    - instantiation of the Babel object in my app
    - Configuration of available languages in our app
      by creating a Config class
"""
from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    This class configures available languages in
    our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """
    This method renders the 1-index.html template
    """
    return render_template('1-index.html')
