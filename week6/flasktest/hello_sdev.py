from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return show_hello()

def show_hello():
    return 'Hellow world!'