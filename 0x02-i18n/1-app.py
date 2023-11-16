#!/usr/bin/env python3
"""
Python flask web application module
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config:
    """
        Config - configure babel class
    """
    LANGUAGES = ['en', 'fr']


@babel.localeselector
def get_locale():
    """ get locale """
    return request.accept_languages.best_match(Config.LANGUAGES)



@app.route('/')
def home():
    """ Homepage """
    return render_template('1-index.html')
