#!/usr/bin/env python3

import sys

sys.path.append("../python")
sys.path.append("src/main/python")


class RestSysCollectorCollect():
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

    def getFileDataAsList(self, fullfilename):
        try:
            f = self.openFileHandler(fullfilename)
        except Exception as e:
            print("Unexpected error:", str(e))
        if f is not None:
            data = self.putDataInList(f)
            self.closeFileHandler(f)
            return data


if __name__ == '__main__':
    collect = RestSysCollectorCollect()
    #data = collect.getFileDataAsList("/proc/version")
    data = collect.getFileDataAsList("/proc/cpuinfo")
    if data is not None:
        for line in data:
            print(str(line).strip("\n"))
