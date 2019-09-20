from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired("Your name is required!")])
    email = EmailField("Email", validators=[InputRequired("Your email is required!"), Email("Please enter a valid email address")])
    message = TextAreaField("Message", validators=[InputRequired("Where is your message?")])
    submit = SubmitField("Send")
