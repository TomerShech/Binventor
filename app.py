from flask import Flask, render_template, request, redirect, url_for, flash, Markup
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime, timedelta
from shortuuid import ShortUUID
from config import Config
from form import ContactForm
from by_extension import should_use_ext

app = Flask(__name__)
app.jinja_env.globals.update(replace=datetime.replace)

con = Config(app)
app.config.from_object(Config)
con.config_db()
con.config_mail()

mail = Mail(app)
db = SQLAlchemy(app)


class Binventordb(db.Model):
    __tablename__ = "pastes"

    pid = db.Column(db.Integer, primary_key=True)  # paste's id
    pname = db.Column(db.String(100), nullable=False)  # paste's name (title)
    # paste's body (actual pasted code)
    pbody = db.Column(db.String(40000), nullable=False)
    random_uuid = db.Column(db.String(8), nullable=False)  # paste's url id
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)  # paste creation UTC date
    delete_at = db.Column(db.DateTime, nullable=False)


def generate_id():
    return ShortUUID().random(length=8)


def delete_expired():
    db.session.query(Binventordb).filter(datetime.utcnow() >
                                         Binventordb.delete_at).delete(synchronize_session=False)


def get_recent_pastes():
    def future(mins): return datetime.utcnow() + timedelta(minutes=mins)
    return Binventordb.query.filter((Binventordb.delete_at < future(10)) | (Binventordb.delete_at < future(60)) | (Binventordb.delete_at < future(1440))).all()[::-1]


@app.route("/")
def index():
    return render_template("index.html", is_index=True, needs_ta=True)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        paste_body = request.form["paste_body"]
        paste_name = "nameless" if not request.form["paste_name"].strip(
        ) else request.form["paste_name"]
        random_uuid = generate_id()
        expiration_time = request.form["expiration"]

        try:
            expiration_time = int(request.form["expiration"])
        except ValueError:
            return redirect(url_for("index"))

        if expiration_time not in (10, 60, 1440, 10080, 43800):
            return redirect(url_for("index"))

        delete_at = datetime.utcnow() + timedelta(minutes=expiration_time)

        delete_expired()
        if Binventordb.query.filter(Binventordb.random_uuid == random_uuid).count():
            while random_uuid == generate_id():
                random_uuid = generate_id()
        data = Binventordb(pname=paste_name, pbody=paste_body,
                           random_uuid=random_uuid, delete_at=delete_at)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for("paste", puuid=random_uuid))


@app.route("/<puuid>", methods=["GET", "POST"])
def paste(puuid):
    delete_expired()
    c = Binventordb.query.filter_by(random_uuid=puuid).first_or_404()
    if should_use_ext(c.pname, c.pbody):
        ext = c.pname.split(".")[1]
        if ext == "txt":
            return render_template("paste.html", pbody=c.pbody, markup="plaintext", title=c.pname, is_footer=True)
        else:
            return render_template("paste.html", pbody=c.pbody, markup=ext, title=c.pname, is_footer=True)
    return render_template("paste.html", pbody=c.pbody, title=c.pname, is_footer=True)


@app.route("/about")
def about():
    return render_template("about.html", title="About", is_footer=True)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    person_name = form.name.data

    if form.validate_on_submit():
        msg_body = f"<b>Name:</b> {person_name}<br /><b>Email:</b> {form.email.data}<br /><b>Message:</b> {form.message.data}"
        msg = Message(f"New email from {person_name}", recipients=[
                      Config.GMAIL_USERNAME], html=msg_body)
        mail.send(msg)
        flash(Markup('<i class="icon-ok"></i> Your email has been sent successfully! Thank you for contacting me'), "msg success-msg")
        return redirect(url_for("contact"))
    return render_template("contact.html", title="Contact", form=form, is_footer=True)


@app.route("/recent")
def all():
    delete_expired()
    return render_template("recent_pastes.html", title="Latest Pastes", recent_pastes=get_recent_pastes(), now=datetime.utcnow(), is_footer=True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="404 Not Found"), 404


if __name__ == "__main__":
    app.run()
