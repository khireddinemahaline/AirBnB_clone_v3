#!/usr/bin/env python3
"""the app using flask to run on the:
    host = 0.0.0.0
    port= 50000
    """
from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def handle(code):
    """close the storage at the end of req"""
    storage.close()


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5000)
