from flask import Flask, render_template, url_for
from datetime import datetime



app = Flask(__name__)

@app.route('/')
def index():
    #now = datetime.now()
    return render_template("index.html", now=datetime.now())

# TODO: Make routes for the other pages

if __name__ == "__main__":
    app.run(debug=True)

# TODO: Make three links