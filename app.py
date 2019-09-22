from os import environ
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from sqlalchemy.sql import func
from datetime import datetime
from uuid import uuid4
from config import Config
from form import ContactForm

app = Flask(__name__)

con = Config(app)

app.config.from_object(Config)
con.config_db("dev")
con.config_mail()

mail = Mail(app)

DB = SQLAlchemy(app)

class BinventorDB(DB.Model):
    __tablename__ = "pastes"

    pid = DB.Column(DB.Integer, primary_key=True)  # paste id
    pname = DB.Column(DB.String(100), nullable=False)  # paste name (title)
    # paste body (actual pasted code)
    pbody = DB.Column(DB.String(40000), nullable=False)
    # paste expiration time (in minutes)
    pexr = DB.Column(DB.Integer, nullable=False)
    random_uuid = DB.Column(DB.String(8), nullable=False)
    created_at = DB.Column(DB.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, pname, pbody, pexr, random_uuid, created_at=created_at):
        self.pname = pname
        self.pbody = pbody
        self.pexr = pexr
        self.random_uuid = random_uuid


def generate_id(length):
    return str(uuid4().hex)[:length]


def delete_expired():
    DB.session.query(BinventorDB).filter((BinventorDB.created_at + func.make_interval(0, 0, 0, 0, 0, BinventorDB.pexr))
    < datetime.utcnow()).delete(synchronize_session=False)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        paste_body = request.form["paste_body"]
        paste_name = "nameless" if not request.form["paste_name"].strip() else request.form["paste_name"]
        expiration_time = request.form["expiration"]
        random_uuid = generate_id(8)

        if not DB.session.query(BinventorDB).filter(BinventorDB.random_uuid == random_uuid).count():
            delete_expired()
            data = BinventorDB(paste_name, paste_body, expiration_time, random_uuid)
            DB.session.add(data)
            DB.session.commit()
            return redirect(url_for("paste", puuid=random_uuid))
        return redirect(url_for("index"))


@app.route("/<puuid>", methods=["GET", "POST"])
def paste(puuid):
    delete_expired()
    c = BinventorDB.query.filter_by(random_uuid=puuid).first_or_404()
    return render_template("paste.html", pbody=c.pbody, title=c.pname, is_paste=True)


@app.route("/about")
def about():
    return render_template("about.html", title="About", is_about=True)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        msg_body = "A person named {0}\nsent you: {1}".format(form.name.data, form.message.data)
        msg = Message("New email from {0}".format(form.name.data), recipients=[environ.get("GMAIL_USERNAME")], body=msg_body)
        mail.send(msg)
        return redirect(url_for("index"))
    return render_template("contact.html", title="Contact", form=ContactForm())


@app.route("/recent")
def recent():
    delete_expired()
    ptuple = tuple(DB.session.query(BinventorDB).all())[::-1]
    return render_template("recent.html", title="Recent Pastes", ptuple=ptuple, now=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="404 Not Found"), 404


if __name__ == "__main__":
    app.run()
