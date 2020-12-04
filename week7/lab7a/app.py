"""
This application serves pages that can be used to illustrate some of the
places I have travelled to.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, request, session, url_for, abort
from os.path import exists
from passlib.hash import sha256_crypt

# TODO: Need to make a new virtual environment, not just copy and paste from lab6
# TODO: Make a constant for the name of the password file
# PSsfile format: username, salt, password hash
PASSFILE = "passfile"
KEYFILE = "keyfile"

app = Flask(__name__)

# TODO: Change this to a file
app.secret_key = "changeToFile"

#Uncomment the below line to not have to check a file for the secret
#key. Secret ket normally stored in a file that is not uploaded to github
#app.secret_key = "changeToFile"

if not exists(PASSFILE):
    open(PASSFILE, "w").close()

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
        username = request.form["username"]
        #TODO: Write the code to check the passfile
        
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

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # TODO: salt = ???
        salt = "a"
        password_hash = sha256_crypt.hash(password + salt)

        # TODO: Use flash to highlight registration errors

        # open file
        with open(PASSFILE, "a") as f:
            f.writelines(username + ", " + salt + "," + password_hash)
        # write date to file
        # close file
        # show success screen
        # go to login
    
    if "username" in session:
        # TODO: Show them a special page
        pass
    else:
        return render_template("register.html")


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
        abort(401)

@app.route('/penang')
def penang():
    """Serves the Penang page"""
    if "username" in session:
        return render_template("penang.html")
    else:
        abort(401)


@app.route('/singapore')
def singapore():
    """Serves the Singapore page"""
    if "username" in session:
        return render_template("singapore.html")
    else:
        abort(401)


@app.route('/vietnam')
def vietnam():
    """Serves the Vietnam page"""
    if "username" in session:
        return render_template("vietnam.html")
    else:
        abort(401)

if __name__ == '__main__':
    app.run(debug=True)
