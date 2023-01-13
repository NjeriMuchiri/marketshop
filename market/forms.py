from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,InputRequired

class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=2, max=30),InputRequired()])
    email_address = StringField(label='Email Address', validators=[Email(),InputRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6),InputRequired()])
    password2 = PasswordField(label='Confirm password',validators=[EqualTo('password1'),InputRequired()])
    submit = SubmitField(label='Create Account')