import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "d76a649f80e4441cb4a09aff3e662e81"

    def config_db(app, env):
        if env == "dev":
            app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:proglove@localhost/BinventorDB"
            app.debug = True
        else:
            # production database
            app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://zgbechbatizsrw:ea0e4d4658ec1d7a94c31311d537a639aec2034b61af9710f301bdc9d23c6035@ec2-54-221-238-248.compute-1.amazonaws.com:5432/dathk3a9fhh79g"
            app.debug = False

        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
