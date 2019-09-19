def config(app, env):
	if env == "dev":
		app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:proglove@localhost/BinventorDB"
		app.debug = True
	else:
		app.config["SQLALCHEMY_DATABASE_URI"] = "" # production database
		app.debug = False

	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
