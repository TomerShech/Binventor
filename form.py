from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email
from string import ascii_uppercase, digits


# class PasswordValidator:
#     def __init__(self, message=None):
#         self.message = message

#     # called when a class instance (object) is called
#     def __call__(password, message):
#         if len(password) < 8:
#             message = "Password is too short, must be 8 characters or more!"
#         elif not any(char in password for char in digits):
#             message = "You must include at least one number in your password"
#         elif not any(char in password for char in ascii_uppercase):
#             message = "You must include at least one UPPERCASE LETTER in your password"
#         elif password.isspace():
#             message = "Password cannot contain only whitespace characters"

#         return message


class Base(FlaskForm):
    email = EmailField("Email", validators=[InputRequired("Your email is required!"), Email("Please enter a valid email address")], render_kw={"placeholder": "Your email here..."})

class ContactForm(Base):
    name = StringField("Name", validators=[InputRequired("Your name is required!")], render_kw={"placeholder": "Your name here..."})
    message = TextAreaField("Message", validators=[InputRequired("Where is your message?")], render_kw={"placeholder": "Your message here..."})
    submit = SubmitField("Send")

class SignUpForm(Base):
    username = StringField("Username", validators=[InputRequired("Where is your username?")])
    password = PasswordField("Password", validators=[InputRequired("Where is your password?")])
    submit = SubmitField("Sign Up!")
