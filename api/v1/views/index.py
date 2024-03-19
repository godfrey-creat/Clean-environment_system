#!/usr/bin/python3
"""
This module contains endpoint(route) status of the API
"""
from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Function that returns a JSON status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    """
    Retrieving the number of each objects by type
    """
    return jsonify({"companies": storage.count("Company"),
                    "waste_types": storage.count("Waste_type"),
                    "clients": storage.count("Client"),
                    "bookings": storage.count("Booking")})
