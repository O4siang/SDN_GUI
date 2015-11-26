# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, jsonify, request, g, abort, redirect, url_for

import json

app = Flask(__name__)

global_flow_table = {}

# mainpage
@app.route("/")
def main():
    #sw_desc = Rest.get_switch_desc()
    #if sw_desc is False:		
        #sw_desc = "not connected"
    return render_template("index.html",sw_desc='notconnn')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5566, debug=False)