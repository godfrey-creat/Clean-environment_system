#!/usr/bin/python3
"""script that starts a flask web app"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_mazingira():
    """Print Web"""
    return 'Hello MAZINGIRA!'

@app.route('/mazingira')
def mazingira():
    """Print Web"""
    return 'MAZINGIRA'

if __name__ == '__main__':
    app.run(debug= True)
    app.run(host='0.0.0.0', port=5000)
