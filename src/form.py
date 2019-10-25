from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired("Your name is required!")], render_kw={"placeholder": "Your name here..."})
    email = EmailField("Email", validators=[InputRequired("Your email is required!"), Email("Please enter a valid email address")], render_kw={"placeholder": "Your email here..."})
    message = TextAreaField("Message", validators=[InputRequired("Where is your message?"), Length(5, 1000)], render_kw={"placeholder": "Your message here..."})
    submit = SubmitField("Send")

class PasteForm(FlaskForm):
    password = PasswordField("Paste Password", validators=[InputRequired("Where is the password?"), Length(6, 16)])
    submit = SubmitField("Let me in!")
