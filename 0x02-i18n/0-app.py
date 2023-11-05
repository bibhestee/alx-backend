"""
Python flask web application module
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """ Homepage """
    return render_template('0-index.html')
