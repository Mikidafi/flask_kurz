from flask import Flask
from flask import render_template
from flask import request
from .database import articles
from flask import redirect
from flask import url_for
from flask import session

app = Flask(__name__)
app.secret_key = b'\x8b\xef\xa1\xb3\xbfu}\x1et~kM\xcb*\xbc\xd5S\x0e\x8d\x86\r\x90\xfa\xb0'

@app.route("/")
def view_welcome_page():
    return render_template("welcome_page.jinja")

@app.route("/about/")
def view_about():
    return render_template("about.jinja")

@app.route("/articles/")
def view_articles():
    return render_template("articles.jinja", articles=articles.items())

@app.route("/admin/")
def view_admin():
	if "logged" not in session:
		return redirect(url_for("view_login"))
	return render_template("admin.jinja")



@app.route("/articles/<int:art_id>")
def view_article(art_id):
    article = articles.get(art_id)
    if article :
        return render_template("article.jinja", article=article)
    return render_template("article_not_found.jinja", art_id=art_id)

@app.route("/login/", methods=["POST"])
def login_user():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		if username == "admin" and password == "admin":
			session["logged"] = True
			return redirect(url_for("view_admin"))
		else:
			return redirect(url_for("view_login"))

@app.route("/login/", methods=["GET"])
def view_login():
	return render_template("login.jinja")

@app.route("/logout/", methods=["POST"])
def logout_user():
	session.pop("logged")
	return redirect(url_for("view_welcome_page"))









