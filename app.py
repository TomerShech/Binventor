from flask import Flask, render_template, request
#from uuid import uuid4

app = Flask(__name__)

#ext = str(uuid4())[0:5]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/p/<randid>", methods=["POST"])
def submit(randid):
    if request.method == "POST":
        paste_body = request.form["paste_body"]
        paste_name = "Nameless" if request.form["paste_name"] == "" else request.form["paste_name"]
        expiration_time = request.form["expiration"]
        return render_template("paste.html", title=paste_name, paste_body=paste_body, randid=randid)


if __name__ == "__main__":
    app.debug = True
    app.run()
