#!/usr/bin/python3
"""
route to api/v1/status
using the app_views Blueprint
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False)
def return_ok():
    """return status code whene succsess"""
    return jsonify({"status": "OK"})
