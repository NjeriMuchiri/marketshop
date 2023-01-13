from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms import Length,EqualTo

class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=Length(min=2, max=30))
    email_address = StringField(label='Email Address')
    password1 = PasswordField(label='Password', validators=Length(min=6))
    password2 = PasswordField(label='Confirm password',validators=EqualTo('password1'))
    submit = SubmitField(label='Create Account')