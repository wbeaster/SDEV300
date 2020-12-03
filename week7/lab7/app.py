"""
This application serves pages that can be used to illustrate some of the
places I have travelled to.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, request, session, url_for, abort

app = Flask(__name__)

# TODO: Change this to a file
app.secret_key = "changeToFile"

#Uncomment the below line to not have to check a file for the secret
#key. Secret ket normally stored in a file that is not uploaded to github
#app.secret_key = "changeToFile"

@app.route('/')
def index():
    """Serves the homepage"""
    
    # Prep the time information
    now = datetime.now()
    nowstr = now.strftime('%Y-%m-%d %H:%M:%S')

    if "username" in session:
        return render_template("index.html", nowstr=nowstr)
    else:
        return redirect(url_for("login"))

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        session["username"] = username
        return redirect(url_for("index"))
    else:
        if "username" in session:
            return redirect(url_for("index"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route('/user')
def user():
    if "username" in session:
        username = session["username"]
        return f"<h1>{username}</h1>"
    else:
        return redirect(url_for("login"))

@app.route('/kualalumpur')
def kualalumpur():
    """Serves the Kuala Lumpur page"""
    if "username" in session:
        return render_template("kualalumpur.html")
    else:
        abort(403)

@app.route('/penang')
def penang():
    """Serves the Penang page"""
    if "username" in session:
        return render_template("penang.html")
    else:
        abort(403)


@app.route('/singapore')
def singapore():
    """Serves the Singapore page"""
    if "username" in session:
        return render_template("singapore.html")
    else:
        abort(403)


@app.route('/vietnam')
def vietnam():
    """Serves the Vietnam page"""
    if "username" in session:
        return render_template("vietnam.html")
    else:
        abort(403)

if __name__ == '__main__':
    app.run(debug=True)
