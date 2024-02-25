#!/usr/bin/python3
"""script that starts a flask web app"""
from flask import Flask,render_template, request

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/company_registration', methods=['POST'])
def company_registration():
    if request.method == 'POST':
        #Handle form submission here.
        #Access form data using request.form.dictionary
        companyname = request.form['companyname']
        waste_type = request.form['waste_type']
        location = request.form['location']
        email = request.form['email']
        phone_no = request.form['phone_no']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        return "Company registered successfully"
    else:
        #Handle other HTTP methods if needed
        return "Method not Allowed!"

@app.route('/client_registration', methods=['POST'])
def client_registration():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_passwprd = request.form['confirm_password']
        return render_template('company_reg.html')

@app.route('/test_home', methods=['GET', 'POST'])
def test_home():
    """Print Web"""

if __name__ == '__main__':
    app.run(debug= True)
    app.run(host='0.0.0.0', port=5000)
