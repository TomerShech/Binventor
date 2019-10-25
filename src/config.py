import json

with open("config.json") as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config.get("SECRET_KEY")
    GMAIL_USERNAME = config.get("GMAIL_USERNAME")

    def __init__(self, app):
       self.app = app

    def config_db(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"] = config.get("DB_DEV_URI")
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    def config_mail(self):
        self.app.config["MAIL_SERVER"] = "smtp.gmail.com"
        self.app.config["MAIL_PORT"] = 587
        self.app.config["MAIL_USE_TLS"] = True
        self.app.config["MAIL_USE_SSL"] = False
        self.app.config["MAIL_USERNAME"] = config.get("GMAIL_USERNAME")
        self.app.config["MAIL_PASSWORD"] = config.get("GMAIL_PASSWORD")
        self.app.config["MAIL_DEFAULT_SENDER"] = config.get("GMAIL_USERNAME")
        self.app.config["MAIL_ASCII_ATTACHMENTS"] = False
