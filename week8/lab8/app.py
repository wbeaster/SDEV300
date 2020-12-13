"""
This application serves pages that can be used to illustrate some of the
places I have travelled to.
"""

import os
from datetime import datetime
from os.path import exists
from string import punctuation
from flask import Flask, flash, render_template, redirect, request, session, url_for, abort
from passlib.hash import sha256_crypt

# passfile format: username password hash
PASSFILE = "passfile"

# location of the Flask app.secret_key
KEYFILE = "keyfile"

# location of the common passwords file
COMMON_PASSWORDS = "CommonPassword.txt"

# location of temporary file used when changing someone's passwrod
# no passwords are stored in this file, only hashes
# used by change_password()
TEMPFILE = "tempfile"

# location of file to record failed logins
FAILED_LOGINS = "failed_logins"

app = Flask(__name__)
app.debug = True

# create a file for logins and hashes if it does not exist
if not exists(PASSFILE):
    open(PASSFILE, "w").close()

common_passwords = set()
with open(COMMON_PASSWORDS, "r") as common_passwords_file:
    for pword in common_passwords_file:
        common_passwords.add(pword.strip())

# comment the two line below if there is no seperate key file
# in the next block you can uncomment a line to use a weak key
with open(KEYFILE, "r") as keyfile:
    app.secret_key = keyfile.readlines()[0]

# Uncomment the below line to not have to check a file for the secret
# key. Secret ket normally stored in a file that is not uploaded to github
# app.secret_key = "changeToFile"

def is_registered(username):
    """
    Function checks to see if the user already exists in PASSFILE
    """
    with open(PASSFILE, "r") as passfile:
        for record in passfile:
            try:
                r_username, r_salt_hash = record.split()
                # The below is just for the linter
                r_salt_hash = r_salt_hash + "nothing"
                if username == r_username:
                    return True
            # this is to handle the initial blank file
            except ValueError:
                pass
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

#def is_common_password(password):
#    """
#    Function determines if a password is in common passwords list
#    """
#    # this is very naive, but there is no need for premature optimization
#    with open(COMMON_PASSWORDS, "r") as common_passwords:
#        for word in common_passwords:
#            # have to strip() or Python
#            if password == word.strip():
#                return True
#    return False

def is_valid_login(username, password):
    """
    Function determines username/password combination is valid
    Returns True if valid combination, False otherwise
    """
    with open(PASSFILE, "r") as passfile:
        for record in passfile:
            try:
                valid_user, valid_password = False, False
                r_username, r_salt_hash = record.split()
                if username == r_username:
                    valid_user = True
                if sha256_crypt.verify(password, r_salt_hash):
                    valid_password = True
                if valid_user and valid_password:
                    return True
            except ValueError:
                pass
    return False

def change_password_tests(new_password1, new_password2):
    """
    Function runs some routine password tests
    """
    error = None
    if not new_password1 == new_password2:
        error = "New passwords do no match"
    elif new_password1 in common_passwords:
        error = "New password is frequently used. Please use another password."
    elif not is_complex(new_password1):
        error = "New password not complex enough"

    return error

def record_failed_login(username):
    """
    Function writes failed logins to a file
    """

    # so we do not risk writing to a non-existent file
    if not exists(FAILED_LOGINS):
        open(FAILED_LOGINS, "w").close()

    time = datetime.now()

    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip_addr = request.environ['REMOTE_ADDR']
    else:
        ip_addr = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy

    with open(FAILED_LOGINS, "a") as logfile:
        logfile.write(time.isoformat() + " " + ip_addr + " " + username + "\n")

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

        # check if the user and hash are in the file
        if not is_valid_login(username, password):
            flash("Invalid username or password")
            record_failed_login(username)
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
    if "username" in session:
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
        elif password in common_passwords:
            error = "Password is frequently used. Please use another password."
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

@app.route('/changepassword', methods=["POST", "GET"])
def change_password():
    """Serves the change password page."""
    if request.method == "POST":
        error = None
        if "username" in session:
            username = session["username"]
            old_password = request.form["old_password"]
            new_password1 = request.form["new_password1"]
            new_password2 = request.form["new_password2"]

            error = change_password_tests(new_password1, new_password2)

            if not is_valid_login(username, old_password):
                error = "Incorrect old password"

            if error:
                flash(error)
            else:
                with open(PASSFILE, "r") as passfile, open(TEMPFILE, "a") as tempfile:
                    for record in passfile:
                        try:
                            r_username, r_salt_hash = record.split()

                            # same_username & same_password exist to
                            # avoid the linter's 'Line too long' flag
                            same_username = username == r_username
                            same_password = sha256_crypt.verify(old_password, r_salt_hash)

                            if same_username and same_password:
                                t_salt_hash = sha256_crypt.hash(new_password1)
                                tempfile.write(username + " " + t_salt_hash + "\n")
                            else:
                                tempfile.write(r_username + " " + r_salt_hash + "\n")
                        except ValueError:
                            pass

                # remove the password backup file that *may* have been previously created
                # fail silently if the file does not exist
                try:
                    os.remove(PASSFILE + ".bak")
                except OSError:
                    pass

                # this keeps a backup of the previous passfile
                os.rename(PASSFILE, PASSFILE + ".bak")
                os.rename(TEMPFILE, PASSFILE)
                flash("Password changed")
                return render_template("index.html")
        else:
            flash("Must be logged in to change password.")
            return redirect(url_for("login"))

    return render_template("changepassword.html")

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
