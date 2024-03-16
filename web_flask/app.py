#!/usr/bin/python3
"""A script that initializes a flask application"""
from flask import Flask


app = Flask(__name__)
@app.route('/')
def index():
    return 'Financial clarity at your fingertips!'


if __name__ == '__main__':
    app.run(debug=True)
