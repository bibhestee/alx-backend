#!/usr/bin/env python3
"""
Python flask web application module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale_with_priority():
    """ get locale with priority """
    if request.args.get('locale'):
        # locale from url parameters
        return request.args.get('locale')
    elif g.user.locale:
        # locale from user settings
        return g.user.locale
    elif request.locale:
        # locale from request header
        return request.locale
    else:
        # use default
        return None


def get_user():
    """ get user """
    users = {1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
             2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
             3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
             4: {"name": "Teletubby", "locale": None,
                 "timezone": "Europe/London"}, }
    # get user id
    try:
        id = int(request.args.get('login_as'))
        return users.get(id, None)
    except Exception:
        return None


class Config:
    """
        Config - configure babel class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request():
    """ before request """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ get locale """
    locale = get_locale_with_priority()
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """ Homepage """
    return render_template('6-index.html')
