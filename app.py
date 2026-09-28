from flask import Flask, request, render_template, redirect, url_for
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )
            file.save(filepath)
            return redirect(url_for("upload_file"))
    return render_template("upload.html")

@app.route("/command", methods=["GET", "POST"])
def command():
    result = ""
    if request.method == "POST":
        host = request.form["host"]
        command = f"ping -c 1 {host}"
        result = subprocess.getoutput(command)
    return render_template("command.html", result=result)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
