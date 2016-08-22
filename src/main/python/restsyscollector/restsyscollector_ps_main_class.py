#!/usr/bin/env python3

from restsyscollector_ps_interface_class import RestSysCollectorPsInterface
from restsyscollector_ps_system_class import RestSysCollectorPsSystem
from restsyscollector_format_class import RestSysCollectorFormat
import sys
sys.path.append("../python")
sys.path.append("src/main/python")

class RestSysCollectorPsMain(RestSysCollectorPsInterface):

    def __init__(self, collect_method):
        self._cpu_data_list = []
        self._disk_size_data_list = []
        self.collect_method = collect_method
        self.collect_ps = RestSysCollectorPsSystem()
        self.collect_format = RestSysCollectorFormat()
        if collect_method == "system":
            self.collect_ps = RestSysCollectorPsSystem()

    @property
    def cpu_data(self):
        return self._cpu_data_list

    @cpu_data.setter
    def cpu_data(self, format):
        data_list = self.collect_ps.getFileDataAsList("/proc/cpuinfo")
        if format == "json":
            self._cpu_data_list = self.collect_format.getListAsJson(data_list)
        if format == "html":
            self._cpu_data_list = self.collect_format.getStringAsHtml(data_list)
        if format == "text":
            self._cpu_data_list = self.collect_format.getStringAsText(data_list)

    @property
    def disk_size_data(self):
        pass

    @disk_size_data.setter
    def disk_size_data(self, format):
        pass

if __name__ == '__main__':
    collect = RestSysCollectorPsMain("system")
    #collect.cpu_data = "json"
    #collect.cpu_data = "html"
    collect.cpu_data = "text"
    cpu_data = collect.cpu_data
    print(str(cpu_data))