#!/usr/bin/env python3

import sys

from abc import ABCMeta, abstractmethod
sys.path.append("../python")
sys.path.append("src/main/python")

class RestSysCollectorPsInterface(metaclass=ABCMeta):

    #@staticmethod
    #@abstractmethod
    #def getCpuData(self, format):
    #    pass

    @property
    @abstractmethod
    def cpu_data(self):
        pass

    @cpu_data.setter
    @abstractmethod
    def cpu_data(self, format):
        pass

    @property
    @abstractmethod
    def disk_size_data(self):
        pass

    @disk_size_data.setter
    @abstractmethod
    def disk_size_data(self, format):
        pass
