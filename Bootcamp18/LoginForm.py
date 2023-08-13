from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField

from wtforms.validators import DataRequired

class Lf (FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    password_again = PasswordField("repeat pass", validators=[DataRequired()])
    remember_me = BooleanField("remember me")
    submit = SubmitField("registration")
