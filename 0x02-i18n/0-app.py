#!/usr/bin/env python3
"""
This module sets up a basic Flask app with a
single / route
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    This function returns Hello World as a header
    """
    return render_template('0-index.html')
