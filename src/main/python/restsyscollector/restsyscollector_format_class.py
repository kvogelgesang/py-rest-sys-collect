#!/usr/bin/env python3

import sys
import json
import re

sys.path.append("../python")
sys.path.append("src/main/python")

class RestSysCollectorFormat():

    def __init__(self):
        pass
        #self.json = json

    def getListAsJson(self, data_list):
        return self.setDataFormat(data_list, "json")

    def getStringAsHtml(self, data_list):
        return self.setDataFormat(data_list, "html")

    def getStringAsText(self, data_list):
        return self.setDataFormat(data_list, "text")

    def setDataFormat(self, data_list, format):
        return_list = []
        return_string = ""
        for line in data_list:
            line = re.sub('\n+|\t+','',line)
            if format == "text":
                line += "\n"
                return_string += line
            if format == "html":
                line += "<br />"
                return_string += line
            if format == "json":
                return_list.append(json.dumps(line))

        if format == "html" or format == "text":
            return return_string
        if format == "json":
            return return_list

