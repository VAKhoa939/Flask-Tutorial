from flask import Flask, redirect, url_for, render_template, request, session, Response, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "tutorial"
app.permanent_session_lifetime = timedelta(hours=12)

@app.route("/")
def home() -> str:
  #return "Hello! This is the main page <h1>HELLO</h1>"
  return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login() -> Response | str:
  if "name" in session:
    flash("Already logged in!", "info")
    return redirect(url_for("user"))
  
  if request.method == "GET":
    return render_template("login.html")
  
  name: str = request.form["name"]
  #return redirect(url_for("user", name = name))
  session["name"] = name
  session.permanent = True
  flash("Logged in successfully!", "info")
  return redirect(url_for("user"))

@app.route("/logout")
def logout() -> Response:
  if "name" in session:
    session.pop("name")
    flash("You have been logged out!", "info")
  return redirect(url_for("login"))

#@app.route("/<name>")
#def user(name: str) -> str:
#  #return f"Hello {name}!"
#  print(name)
#  return render_template("hello.html", name=name)

@app.route("/user")
def user() -> str | Response:
  if "name" in session:
    return render_template("hello.html", name = session["name"])
  else:
    return redirect(url_for("login"))

@app.route("/admin")
def admin() -> Response:
  return redirect(url_for("home"))

if __name__ == "__main__":
  app.run(debug=True)