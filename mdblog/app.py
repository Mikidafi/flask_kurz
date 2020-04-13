from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@app.route("/about/")
def view_about():
    return render_template("about.jinja")

@app.route("/articles/")
def view_articles():
    return render_template("articles.jinja")

@app.route("/admin/")
def view_admin():
    return render_template("admin.jinja")


    
