from os import environ

class Config:
    SECRET_KEY = environ.get("SECRET_KEY")

    def __init__(self, app):
       self.app = app

    def config_db(self, env):
        if env == "dev":
            self.app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
            self.app.debug = True
        elif env == "prod":
            # production database
            self.app.config["SQLALCHEMY_DATABASE_URI"] = ""
            self.app.debug = False
        else:
            print("The argument should be either 'dev' for development or 'prod' for production")

        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    def config_mail(self):
        self.app.config["MAIL_SERVER"] = "smtp.gmail.com"
        self.app.config["MAIL_PORT"] = 587
        self.app.config["MAIL_USE_TLS"] = True 
        self.app.config["MAIL_USE_SSL"] = False
        self.app.config["MAIL_USERNAME"] = environ.get("GMAIL_USERNAME")
        self.app.config["MAIL_PASSWORD"] = environ.get("GMAIL_PASSWORD")
        self.app.config["MAIL_DEFAULT_SENDER"] = environ.get("GMAIL_USERNAME")
        self.app.config["MAIL_ASCII_ATTACHMENTS"] = False
