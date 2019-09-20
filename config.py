import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "d76a649f80e4441cb4a09aff3e662e81"

    def config_db(app, env):
        if env == "dev":
            app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:proglove@localhost/BinventorDB"
            app.debug = True
        else:
            # TODO: production database
            app.config["SQLALCHEMY_DATABASE_URI"] = ""
            app.debug = False

        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
