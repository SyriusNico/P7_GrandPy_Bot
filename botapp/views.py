#! /usr/bin/env python
# coding : utf-8
from flask import Flask , render_template, request, url_for, jsonify

from botapp import app
from botapp.api import mediaWiki as m
from botapp.api import googlePlace as g



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def result():   
    wiki = m.MediaWiki()
    place = g.GooglePlace()
    req = request.form['question']
    address = place.sendQuery(req)
    extract = wiki.extractQuery(req)
    _dict = {"extract": extract, "address": address[0], "position": address[1]}
    return jsonify(title=extract[0], query=extract[1], label=address)
