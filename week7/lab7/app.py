"""
This application serves pages that can be used to illustrate some of the
places I have travelled to.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)

# TODO: Change this to a file
app.secret_key = "changeToFile"

#Uncomment the below line to not have to check a file for the secret
#key. Secret ket normally stored in a file that is not uploaded to github
#app.secret_key = "changeToFile"

@app.route('/')
def index():
    """Serves the homepage"""
    now = datetime.now()
    nowstr = now.strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", nowstr=nowstr)

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login_name = request.form["nm"]
        session["login_name"] = login_name
        return redirect(url_for("user"))
    else:
        if "login_name" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("login_name", None)
    return redirect(url_for("login"))

@app.route('/user')
def user():
    if "login_name" in session:
        login_name = session["login_name"]
        return f"<h1>{login_name}</h1>"
    else:
        return redirect(url_for("login"))

@app.route('/kualalumpur')
def kualalumpur():
    """Serves the Kuala Lumpur page"""
    return render_template("kualalumpur.html")

@app.route('/penang')
def penang():
    """Serves the Penang page"""
    return render_template("penang.html")

@app.route('/singapore')
def singapore():
    """Serves the Singapore page"""
    return render_template("singapore.html")

@app.route('/vietnam')
def vietnam():
    """Serves the Vietnam page"""
    return render_template("vietnam.html")

if __name__ == '__main__':
    app.run(debug=True)
