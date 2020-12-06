"""
This application serves pages that can be used to illustrate some of the
places I have travelled to.
"""

from datetime import datetime
from os.path import exists
from string import punctuation
from flask import Flask, flash, render_template, redirect, request, session, url_for, abort
from passlib.hash import sha256_crypt

# passfile format: username password hash
PASSFILE = "passfile"

# location of the Flask app.secret_key
KEYFILE = "keyfile"

app = Flask(__name__)
app.debug = True

# comment the two line below if there is no seperate key file
# in the next block you can uncomment a line to use a weak key
with open(KEYFILE, "r") as keyfile:
    app.secret_key = keyfile.readlines()[0]

# Uncomment the below line to not have to check a file for the secret
# key. Secret ket normally stored in a file that is not uploaded to github
# app.secret_key = "changeToFile"

# create a file for logins and hashes if it does not exist
if not exists(PASSFILE):
    open(PASSFILE, "w").close()

def is_registered(username):
    """
    Function checks to see if the user already exists in PASSFILE
    """
    with open(PASSFILE, "r") as passfile:
        for record in passfile:
            r_username, r_salt_hash = record.split()
            # The below is just for the linter
            r_salt_hash = r_salt_hash + "nothing"
            if username == r_username:
                return True
    return False

def has_whitespace(string):
    """
    Function determines if a string, probably a username, has white space
    in it.
    """
    temp = string.split()
    return len(temp) > 1

def is_complex(password):
    """
    Function determines if a password meets the programs complexity requirements
    """
    if len(password) >= 12:
        if any(c.isupper() for c in password):
            if any(c.islower() for c in password):
                if any(c.isdigit() for c in password):
                    if any(c in punctuation for c in password):
                        return True
    return False

@app.route('/')
def index():
    """Serves the homepage"""
    # Prep the time information
    now = datetime.now()
    nowstr = now.strftime('%Y-%m-%d %H:%M:%S')

    if "username" in session:
        return render_template("index.html", nowstr=nowstr)
    return redirect(url_for("login"))

@app.route('/login', methods=["POST", "GET"])
def login():
    """Serves the login page"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        valid_user = False
        valid_password = False

        # check if the user and hash are in the file
        with open(PASSFILE, "r") as passfile:
            for record in passfile:
                r_username, r_salt_hash = record.split()
                if username == r_username:
                    valid_user = True
                    if sha256_crypt.verify(password, r_salt_hash):
                        valid_password = True
                        break
                valid_user, valid_password = False, False

        if not valid_user or not valid_password:
            flash("Invalid username or password")
        else:
            session["username"] = username
            return redirect(url_for("index"))
    else:
        if "username" in session:
            return redirect(url_for("index"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    """Serves the logout page"""
    session.pop("username", None)
    flash("You have been logged out.")
    return redirect(url_for("index"))

@app.route("/register", methods=["POST", "GET"])
def register():
    """Serve the register page."""
    if request.method == "POST":
        if "username" in session:
            flash("Logout if you would like a new registration.")

        username = None
        password = None
        error = None
        username = request.form["username"]
        password = request.form["password"]

        if not username:
            error = "Please enter a username"
        elif not password:
            error = "Please enter a password."
        elif is_registered(username):
            error = "Username already registered"
        elif has_whitespace(username):
            error = "Username may not have spaces"
        elif not is_complex(password):
            error = "Password not complex enough"

        if error:
            flash(error)
        else:
            password_hash = sha256_crypt.hash(password)
            with open(PASSFILE, "a") as passfile:
                passfile.write(username + " " + password_hash + "\n")
            flash("Registration successful. Please login.")
            return redirect(url_for("login"))

    return render_template("register.html")

@app.route('/user')
def user():
    """Serves a page with the user's name on it."""
    if "username" in session:
        username = session["username"]
        return f"<h1>{username}</h1>"
    return redirect(url_for("login"))

@app.route('/kualalumpur')
def kualalumpur():
    """Serves the Kuala Lumpur page"""
    if "username" in session:
        return render_template("kualalumpur.html")
    return abort(401)

@app.route('/penang')
def penang():
    """Serves the Penang page"""
    if "username" in session:
        return render_template("penang.html")
    return abort(401)

@app.route('/singapore')
def singapore():
    """Serves the Singapore page"""
    if "username" in session:
        return render_template("singapore.html")
    return abort(401)


@app.route('/vietnam')
def vietnam():
    """Serves the Vietnam page"""
    if "username" in session:
        return render_template("vietnam.html")
    return abort(401)

@app.route('/table')
def table():
    """Serves a table of pictures"""
    if "username" in session:
        return render_template("table.html")
    return abort(401)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
