from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@app.route("/about/")
def view_about():
    return render_template("about.jinja")

