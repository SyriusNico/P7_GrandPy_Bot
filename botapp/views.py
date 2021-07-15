#! /usr/bin/env python
# coding : utf-8
from flask import Flask , render_template, request, url_for
from . import app
from botapp.api import mediaWiki as m
from botapp.api import here as h

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result", methods=['GET', 'POST'])
def result():   
    wiki = m.MediaWiki()
    here = h.HereApi()
    req = request.form
    reqToApi = req['query']
    address = here.sendQuery(reqToApi)
    extract = wiki.extractQuery(reqToApi)
    _dict = {"request" : extract,
            "address" : address}
    return render_template('result.html', query=_dict["request"],
                                          label=_dict["address"])