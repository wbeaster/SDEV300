"""
This application serves pages that can be used to illustrate some of the
places I have travelled to.
"""

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the homepage"""
    now = datetime.now()
    nowstr = now.strftime('%Y-%m-%d %H:%M:%S')
    return render_template("index.html", nowstr=nowstr)

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
