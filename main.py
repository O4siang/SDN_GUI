# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, jsonify, request, g, abort, redirect, url_for
from rest import Rest
import json

app = Flask(__name__)

global_flow_table = {}

# mainpage
@app.route("/")
def main():
    print "test"
    sw_desc = Rest.get_switch_desc()
    print sw_desc
    sw_dpid_list = Rest.get_switch_list()
    print sw_dpid_list
    
    #if sw_desc is False  or int(dpid) not in sw_dpid_list:     
     #   sw_desc = "not connected"
    for dpid in sw_dpid_list:
        print dpid
        dpid_t = dpid
        flow_table = None
        flow_table = Rest.get_flow_table(dpid)
        global global_flow_table
        global_flow_table = flow_table
        port = Rest.get_switch_port(dpid)
        print "test"
    return render_template("index.html",sw_desc=sw_desc,dpid=dpid_t, port=port, flow_table=flow_table)

@app.route("/add", methods=['POST'])
def add():
    usertable = {}
    usertable["username"] = request.form['username']
    usertable["mac"] = request.form['mac']
    usertable["port"] = request.form['port']
    print json.dumps(usertable)
    Rest.add_user(json.dumps(usertable))
    return redirect(url_for('main'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5566, debug=False)
