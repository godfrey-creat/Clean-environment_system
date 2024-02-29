#!/usr/bin/python3
'''Contains a Flask web application API.'''

import os
from flask import Flask, jsonify
from flask_cors import CORS

# from api.v1.views import app_views
from flask import Flask,render_template,redirect,url_for,request
from forms.form import LoginForm, CompanyRegistrationForm,ClientRegistrationForm
from models.models import User, Company,db
from flask_bcrypt import bcrypt 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_login import login_user, current_user, login_required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Clean_env_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clean_env1.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Initialising SQLAlchemy with Flask App
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # Try loading the user from both User and Company models
    user = User.query.get(int(user_id))
    if user is None:
        user = Company.query.get(int(user_id))
    return user

""" Creating Database with App Context"""
def create_db():
    with app.app_context():
        db.create_all()
 

@app.errorhandler(404)
def error_404(error):
    '''Handles the 404 HTTP error code.'''
    return jsonify(error="Not found"), 404

@app.errorhandler(400)
def error_400(error):
    '''Handles the 400 HTTP error code'''
    msg = 'Bad request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        msg = error.description
    return jsonify(error= msg), 400

@app.route('/')
def index():
    """Print Web"""
    return render_template('landing_page/index.html')      

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        login_as = form.login_as.data
        password = form.password.data
        companies = Company.query.all()
        if login_as == 'company':
            company = Company.query.filter_by(email=email).first()
            if not company:
                return render_template('forms/login.html', form=form,msg='The email entered is not associate to any company')
            if company and bcrypt.check_password_hash(company.password, password):
                # Authentication successful, redirect to dashboard or company-specific route
                return render_template('home.html',companies=companies)
            else:
                return render_template('forms/login.html', form=form,msg='Invalid credentials')
        elif login_as == 'client':
            user = User.query.filter_by(email=email).first()
            if not user:
                return render_template('forms/login.html', form=form,msg='Invalid credentials')
            if user and bcrypt.check_password_hash(user.password, password):
                # Authentication successful, redirect to dashboard or client-specific route
                return render_template('home.html',companies=companies,test='peter')
            else:
                return render_template('forms/login.html', form=form,msg='Invalid credentials')
    return render_template('forms/login.html', form=form)

@app.route('/Company_registration', methods=['GET', 'POST'])
def Company_registration():
    form = CompanyRegistrationForm()
    print('form avaailable')
    if request.method == 'POST':
        companyname = form.companyname.data
        waste_type = form.waste_type.data
        location = form.location.data
        email = form.email.data
        phone_no = form.phone_no.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        companies= Company.query.filter_by(email=email).first()
        if companies:
            return render_template('forms/company_reg.html', form=form, msg='Company already registered')
        if password != confirm_password:
            return render_template('forms/company_reg.html', form=form, msg='Password does not match')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_company = Company(
            companyname=companyname,
            waste_type=waste_type,
            location=location,
            email=email,
            phone_no=phone_no,
            password=hashed_password
        )

        db.session.add(new_company)
        db.session.commit()

        return redirect(url_for('login_route'))

    return render_template('forms/company_reg.html', form=form)

@app.route('/client_registration', methods=['GET', 'POST'])
def client_registration():
    form = ClientRegistrationForm()
    print('form avaailble')
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        confirm_password=form.confirm_password.data
        clients= User.query.filter_by(email=email).first()
        if clients:
            return render_template('forms/client_reg.html', form=form, msg='Email already exist')
        if password != confirm_password:
            return render_template('forms/client_reg.html', form=form, msg='Password does not match')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_client = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('login_route',msg='Registration successful, continue to log in'))

    return render_template('forms/client_reg.html', form=form)


@app.route('/booking', methods=['GET', 'POST'])
# @login_required
def booking():
    companies= Company.query.all()
    return render_template('home.html',companies=companies)
# if __name__ == '__main__':
#     db.create_all()
