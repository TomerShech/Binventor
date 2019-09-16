from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from uuid import uuid4

app = Flask(__name__)

ENV = "dev"

if ENV == "dev":  # development database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:proglove@localhost/BinventorDB"
    # app.debug = True
else:  # production database
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
    # app.debug = False

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DB = SQLAlchemy(app)


class BinventorDB(DB.Model):
    __tablename__ = "pastes"

    pid = DB.Column(DB.Integer, primary_key=True)  # paste id
    pname = DB.Column(DB.String(100), nullable=False)  # paste name (title)
    # paste body (actual pasted code)
    pbody = DB.Column(DB.String(35000), nullable=False)
    # paste expiration time (in minutes)
    pexr = DB.Column(DB.Integer, nullable=False)
    random_uuid = DB.Column(DB.String(12), nullable=False)
    created_at = DB.Column(DB.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, pname, pbody, pexr, random_uuid, created_at=created_at):
        self.pname = pname
        self.pbody = pbody
        self.pexr = pexr
        self.random_uuid = random_uuid


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        paste_body = request.form["paste_body"]
        paste_name = "nameless" if not request.form["paste_name"].strip() else request.form["paste_name"]
        expiration_time = request.form["expiration"]
        random_uuid = str(uuid4().hex)[:12]

        if not DB.session.query(BinventorDB).filter(BinventorDB.random_uuid == random_uuid).count():
            data = BinventorDB(paste_name, paste_body, expiration_time, random_uuid)
            DB.session.add(data)
            DB.session.commit()
            return redirect(url_for("paste", puuid=random_uuid, pbody=paste_body))
        else:
            return redirect(url_for("index"))


@app.route("/<puuid>", methods=["GET", "POST"])
def paste(puuid):
    return render_template("paste.html", pbody=BinventorDB.pbody)


# @app.route('/user/<username>')
# def show_user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('show_user.html', user=user)

if __name__ == "__main__":
    app.debug = True
    app.run()
