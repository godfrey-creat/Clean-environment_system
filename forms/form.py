from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

class CompanyRegistrationForm(FlaskForm):
    companyname = StringField('Company Name', validators=[DataRequired()])
    waste_type_choices = [
        ('1', 'Liquid Waste'),
        ('2', 'Solid Rubbish'),
        ('3', 'Organic Waste'),
        ('4', 'Recyclable Rubbish'),
        ('5', 'Hazardous Waste'),
        ('6', 'Industrial Waste'),
        ('7', 'Electronic Waste'),
        ('8', 'Construction Waste')
    ]
    waste_type = SelectField('Waste Type', choices=waste_type_choices, validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_no = StringField('Phone No', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class ClientRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    login_as_choices = [
        ('company', 'Company'),
        ('client', 'Client')
    ]
    login_as = SelectField('Login As', choices=login_as_choices, validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
