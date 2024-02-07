#!/usr/bin/python3
"""script that starts a flask web app"""
from flask import Flask,render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_mazingira():
    """Print Web"""
    return 'Hello MAZINGIRA!'

@app.route('/test')
def hello():
    """Print Web"""
    return render_template('index.html') 

@app.route('/test_home', methods=['GET', 'POST'])
def test_home():
    """Print Web"""
    peter='opere'
    return render_template('test.html',peter=peter)       

@app.route('/mazingira')
def mazingira():
    """Print Web"""
    return 'MAZINGIRA'

if __name__ == '__main__':
    app.run(debug= True)
    app.run(host='0.0.0.0', port=5000)
