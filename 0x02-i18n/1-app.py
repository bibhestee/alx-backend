#!/usr/bin/env python3
"""
Python flask web application module
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)

# configure flask-babel default locale and timezone
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

# initialize flask-babel
babel = Babel(app)


class Config:
    """
        Config - configure babel class
    """
    LANGUAGES = ['en', 'fr']


@app.route('/')
def home():
    """ Homepage """
    return render_template('1-index.html')
