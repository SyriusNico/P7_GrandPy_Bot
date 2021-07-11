from flask import Flask , render_template

from . import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    return render_template('result.html')