from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class JarForm(FlaskForm):
    name = StringField('Jar Name', validators=[DataRequired()])
    allocated = FloatField('Initial Amount', validators=[DataRequired()])
    submit = SubmitField('Create Jar')

class TransactionForm(FlaskForm):
    jar = SelectField('Select Jar', coerce=int)
    amount = FloatField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    type = SelectField('Type', choices=[('expense', 'Expense'), ('income', 'Income')])
    submit = SubmitField('Add Transaction')
