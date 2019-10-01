from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length

class Base(FlaskForm):
    email = EmailField("Email", validators=[InputRequired("Your email is required!"), Email("Please enter a valid email address")], render_kw={"placeholder": "Your email here..."})

class ContactForm(Base):
    name = StringField("Name", validators=[InputRequired("Your name is required!")], render_kw={"placeholder": "Your name here..."})
    message = TextAreaField("Message", validators=[InputRequired("Where is your message?"), Length(5, 1000)], render_kw={"placeholder": "Your message here..."})
    submit = SubmitField("Send")

class SignUpForm(Base):
    username = StringField("Username", validators=[InputRequired("Where is your username?"), Length(3, 15)], render_kw={"placeholder": "Create a nice username..."})
    password = PasswordField("Password", validators=[InputRequired("Where is your password?")], render_kw={"placeholder": "Create a strong password!"})
    submit = SubmitField("Sign Up!")
