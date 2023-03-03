#!/usr/bin/env python3
"""
This module contains:
    - a get_locale function with the localeselector
      decorator
    - request.accept_languages to determine the best match
      without supported languages
    - a way to force a particular locale by passing the
      locale=fr parameter to your app’s URLs.
    - a get_user function that returns a user dictionary
      or None if the ID cannot be found or if
     login_as was not passed
    - a before_request function uses get_user to find
      a user and set it as a global on g.user
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


app = Flask(__name__)
babel = Babel(app)
users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


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
    locale = request.args.get("locale")

    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    This method renders the 5-index.html template
    """
    return render_template('5-index.html')


def get_user():
    """
    This function returns a user dictionary
    or None if the ID cannot be found or if
    login_as was not passed
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    This method uses get_user to find
    a user and set it as a global on
    g.user
    """
    g.user = get_user()
