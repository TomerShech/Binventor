from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from uuid import uuid4

app = Flask(__name__)

#ext = str(uuid4())[0:5]

ENV = "dev"

if ENV == "dev":  # development database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:proglove@localhost/QPastesDB"
    app.debug = True
else:  # production database
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
    app.debug = False

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DB = SQLAlchemy(app)


class QPastesDB(DB.Model):
    __tablename__ = "pastes"
    pid = DB.Column(DB.Integer, primary_key=True)  # paste id
    pname = DB.Column(DB.String(100), nullable=False)  # paste name (title)
    # paste body (actual pasted code)
    pbody = DB.Column(DB.String(35000), nullable=False)
    # paste expiration time (in minutes)
    pexr = DB.Column(DB.Integer, nullable=False)
    created_at = DB.Column(DB.DateTime, nullable=False,
                           default=datetime.utcnow)

    def __init__(self, pname, pbody, pexr, created_at=created_at):
        self.pname = pname
        self.pbody = pbody
        self.pexr = pexr


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/paste", methods=["POST"])
def submit():
    if request.method == "POST":
        paste_body = request.form["paste_body"]
        paste_name = "Nameless" if not request.form["paste_name"].strip() else request.form["paste_name"]
        expiration_time = request.form["expiration"]

        data = QPastesDB(paste_name, paste_body, expiration_time)
        DB.session.add(data)
        DB.session.commit()

        return render_template("paste.html", title=paste_name, paste_body=paste_body, paste=True)

if __name__ == "__main__":
    app.run()
