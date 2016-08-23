#!/usr/bin/env python3

import re
import sys

sys.path.append("../python")
sys.path.append("src/main/python")


class RestSysCollectorPsSystem():
    def __init__(self):
        pass

    @staticmethod
    def openFileHandler(fullfilename):
        try:
            f = open(fullfilename, 'r')
            return f
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            #raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            #raise

    @staticmethod
    def closeFileHandler(filehandler):
        filehandler.close()

    @staticmethod
    def putDataInList(filehandler):
        data = []
        for line in filehandler.readlines():
            data.append(line)
        return data

    def getCpuList(self):
        return self.getFileDataAsList("/proc/cpuinfo")

    def getFileDataAsList(self, fullfilename):
        try:
            f = self.openFileHandler(fullfilename)
        except Exception as e:
            print("Unexpected error:", str(e))
        if f is not None:
            data = self.putDataInList(f)
            self.closeFileHandler(f)
            return data

    def getFileDataAsDict(self, data_list, delimiter):
        data_dict = {}
        for line in data_list:
            line = re.sub('\n+|\t+','',line)
            line = line.split(delimiter)
            if line[0].strip() and line[1].strip():
                #print(line[0].strip() + " : " + line[1].strip())
                data_dict[line[0].strip()] = line[1].strip()
        return data_dict

    def getCpuInfoAsDictInList(self, data_list, delimiter):
        data_dict = {}
        cpu_list = []
        for line in data_list:
            line = re.sub('\n+|\t+','',line)
            line = line.split(delimiter)
            if line[0].strip() and line[1].strip():
                #print(line[0].strip() + " : " + line[1].strip())
                data_dict[line[0].strip()] = line[1].strip()
            else:
                cpu_list.append(data_dict)
                data_dict = {}
        return cpu_list



if __name__ == '__main__':
    collect = RestSysCollectorPsSystem()
    #data = collect.getFileDataAsList("/proc/version")
    data_list = collect.getFileDataAsList("/proc/cpuinfo")
    if data_list is not None:
        data_list_cpu =collect.getCpuInfoAsDictInList(data_list, ":")
        for obj in data_list:
          print(str(obj))
        #for line in data_list:
         #   print(str(line).strip("\n"))
