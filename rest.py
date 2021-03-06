# -*- coding: utf-8 -*-

import requests
import json
import networkx as nx
from networkx.readwrite import json_graph

RYU_SERVER_URL = "http://127.0.0.1:8080"

def hex2decimal(hex):
    i = int(hex, 16)
    return str(i)

class Rest():
    def __init__(self):
        pass

    @staticmethod
    def get_switch_list():
        get_switch_list_url = "%s/stats/switches" % (RYU_SERVER_URL)
        try:
            req = requests.get(get_switch_list_url)
        except requests.exceptions.ConnectionError:
            return False

        
        return req.json()


    @staticmethod
    def get_switch_desc():
        data = Rest.get_switch_list()
        if data is False:
            return False
        desc_list = []
        desc_dict = {}
        for dpid in data:
            get_switch_desc_url = "%s/stats/desc/%s" % (RYU_SERVER_URL, dpid)
            try:
                req = requests.get(get_switch_desc_url)
            except requests.exceptions.ConnectionError:
                return False

            flow_table = Rest.get_flow_table(dpid)
            for dpid, f_list in flow_table.iteritems():
                flow_num = len(f_list)

            for dpid, sw_dict in req.json().iteritems():
                sw_dict["flow_num"] = flow_num
                desc_dict[dpid] = sw_dict

        desc_list.append(desc_dict)
        #print desc_list

        return desc_list

    @staticmethod
    def get_flow_table(dpid):
        get_flow_table_url = "%s/stats/flow/%s" % (RYU_SERVER_URL, dpid)
        req = requests.get(get_flow_table_url)
        
        return req.json()
        
    @staticmethod
    def get_switch_port(dpid):
        get_switch_port_url = "%s/stats/port/%s" % (RYU_SERVER_URL, dpid)
        req = requests.get(get_switch_port_url)

        for dpid, p_list in req.json().iteritems():
            p_list.sort()
            del p_list[-1]
            return p_list
            


        #return req.json()


    @staticmethod
    def add_flow(req_data):
        add_flow_url = "%s/stats/flowentry/add" % (RYU_SERVER_URL)
        try:
            req = requests.post(add_flow_url, data=req_data)
        except requests.exceptions.eonnectionError:
            return False

        return req.status_code

    @staticmethod
    def del_flow(req_data):
        del_flow_url = "%s/stats/flowentry/delete" % (RYU_SERVER_URL)
        try:
            req = requests.post(del_flow_url, data=req_data)
        except requests.exceptions.ConnectionError:
            return False

        return req.status_code

    @staticmethod
    def add_user(req_data):
        print req_data
        usertable_url = "%s/simpleswitch/usertable" % (RYU_SERVER_URL)
        try:
            req = requests.post(usertable_url, data=req_data)
        except requests.exceptions.eonnectionError:
            return False

        return req.status_code

 


