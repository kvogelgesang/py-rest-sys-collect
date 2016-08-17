#!/usr/bin/env python3

import sys
sys.path.append("../python")
sys.path.append("src/main/python")

class RestSysCollectorCollect():

    def getFileDataAsList(self, fullfilename):
        try:
            f = open(fullfilename, 'r')
            return f.readlines()
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        return False


if __name__ == '__main__':
    pass