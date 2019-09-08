from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        paste_body = request.form["paste_body"]
        paste_name = request.form["paste_name"]
        expiration_time = request.form["expiration"]
        print(paste_body, paste_name, expiration_time)
        return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
