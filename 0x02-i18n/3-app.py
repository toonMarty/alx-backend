#!/usr/bin/env python3
"""
This module contains:
    - the gettext function to parameterize templates

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
    Determines the best match with supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    This method renders the 3-index.html template
    """
    return render_template('3-index.html')
