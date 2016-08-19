#!/usr/bin/env python3

import sys
import psutil

sys.path.append("../python")
sys.path.append("src/main/python")

class RestSysCollectorPsutils():

    def getCpuTimes(self, percent=False, interval=0, percpu=False):
        return  psutil.cpu_times_percent()