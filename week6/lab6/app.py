from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    nowstr = now.strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", nowstr=nowstr)

@app.route('/kualalumpur')
def kualalumpur():
    return render_template("kualalumpur.html")
# TODO: Make routes for the other pages

@app.route('/penang')
def penang():
    return render_template("penang.html")

@app.route('/singapore')
def singapore():
    return render_template("singapore.html")

@app.route('/vietnam')
def vietnam():
    return render_template("vietnam.html")


if __name__ == "__main__":
    app.run(debug=True)