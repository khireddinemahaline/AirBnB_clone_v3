#!/usr/bin/python3
"""return hello HBNB using flask"""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
