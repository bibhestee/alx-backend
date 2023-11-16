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


def get_user(login_as: str) -> dict:
    """ get user """
    users = {1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
             2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
             3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
             4: {"name": "Teletubby", "locale": None,
                 "timezone": "Europe/London"}, }
    if login_as:
        return users.get(int(login_as))
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


@babel.localeselector
def get_locale():
    """ get locale """
    locale = request.args.get('locale', False)
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """ before request """
    id = request.args.get('login_as')
    g.user = get_user(id)


@app.route('/')
def home():
    """ Homepage """
    return render_template('5-index.html', user=g.user)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000)
