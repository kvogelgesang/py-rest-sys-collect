#!/usr/bin/env python3

from restsyscollector_ps_interface_class import RestSysCollectorPsInterface
from restsyscollector_ps_system_class import RestSysCollectorPsSystem
from restsyscollector_format_class import RestSysCollectorFormat
import sys
sys.path.append("../python")
sys.path.append("src/main/python")

class RestSysCollectorPsMain(RestSysCollectorPsInterface):

    def __init__(self, collect_method, format, system_component_list):
        self._cpu_data_list = []
        self._disk_size_data_list = []
        self._render_format = format
        self._system_component_list = system_component_list
        self.collect_method = collect_method
        self.collect_ps = RestSysCollectorPsSystem()
        self.collect_format = RestSysCollectorFormat()
        if collect_method == "system":
            self.collect_ps = RestSysCollectorPsSystem()

        for method_name in system_component_list:
            print(str(method_name))
            try:
                method = getattr(self, method_name)
                method()
            except AttributeError:
                raise NotImplementedError("Method " + method_name + " does not implement.")

    def cpu(self):
        data_list = self.collect_ps.getCpuList()
        if self._render_format == "json":
            self._cpu_data_list = self.collect_format.getListAsJson(data_list)
        if self._render_format == "html":
            self._cpu_data_list = self.collect_format.getStringAsHtml(data_list)
        if self._render_format == "text":
            self._cpu_data_list = self.collect_format.getStringAsText(data_list)

    @property
    def render_format(self):
        return self._render_format

    @render_format.setter
    def render_format(self, format):
        self._render_format = format

    @property
    def cpu_data(self):
        return self._cpu_data_list

    @cpu_data.setter
    def cpu_data(self, data_list):
        #data_list = self.collect_ps.getFileDataAsList("/proc/cpuinfo")
        if self._render_format == "json":
            self._cpu_data_list = self.collect_format.getListAsJson(data_list)
        if self._render_format == "html":
            self._cpu_data_list = self.collect_format.getStringAsHtml(data_list)
        if self._render_format == "text":
            self._cpu_data_list = self.collect_format.getStringAsText(data_list)

    @property
    def disk_size_data(self):
        pass

    @disk_size_data.setter
    def disk_size_data(self, format):
        pass

if __name__ == '__main__':
    system_component_list = [ "cpu" ]
    collect = RestSysCollectorPsMain("system", "html", system_component_list)
    #collect.cpu_data = "json"
    #collect.cpu_data = "html"
    #collect.cpu_data = "text"
    #collect._render_format = "json"
    print(collect._render_format)
    #collect.cpu_data = RestSysCollectorPsSystem().getFileDataAsList("/proc/cpuinfo")
    cpu_data = collect.cpu_data
    print(str(cpu_data))