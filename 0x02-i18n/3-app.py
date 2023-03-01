#!/usr/bin/env python3
"""
This module contains:
    - a get_locale function with the localeselector
      decorator
    - request.accept_languages to determine the best match
      without supported languages
"""
from flask_babel import Babel, gettext
from flask import Flask, render_template, request


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


@babel.localeselector
def get_locale():
    """
    This function determines the best match with
    supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    This is a view function that renders the 3-index.html
    template
    """
    return render_template('3-index.html')
