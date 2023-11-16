#!/usr/bin/env python3
"""
Python flask web application module
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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


@app.route('/')
def home():
    """ Homepage """
    return render_template('1-index.html')
