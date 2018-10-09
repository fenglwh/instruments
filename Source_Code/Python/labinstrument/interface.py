#!/usr/bin/python
# coding:utf-8
__Author__ = 'Adair.l'
import abc
from labinstrument.tools.buildin_ex import *
import json
import os




class OTASSInterface:
    '''
    As a consideration, this interface is defined for the pre-defined function
    which will called by the GUI or in other palces.
    '''
    @abc.abstractmethod
    def ota_meas_power(self):
        '''
        this is a function meas tx power
        :return: (indicator,value)   indicator is to show if the meas is running normally or something happend
        such as:0 for normal
                1 for measurement timeout , this exception is critical
                2 for signalling error,    this exception is fixable
                3 for .....
        and these exceptions should be handled in the full procedure.
        as if we got 1, then we should pop an messagebox for fixed second, and tell the tester, this point will be skipped.
        as we got 2, the we should reestablish the call and remeas, it should be able to fix the problem. and pop a connection dialog and try to connect.
        '''
        pass

    @abc.abstractmethod
    def ota_meas_per(self):
        '''
               this is a function meas tx power
               :return: (indicator,value)   indicator is to show if the meas is running normally or something happend
               such as:0 for normal
                       1 for measurement timeout , this exception is critical
                       2 for signalling error,    this exception is fixable
                       3 for .....
               and these exceptions should be handled in the full procedure.
               as if we got 1, then we should pop an messagebox for fixed second, and tell the tester, this point will be skipped.
               as we got 2, the we should reestablish the call and remeas, it should be able to fix the problem. and pop a connection dialog and try to connect.
               '''

    @abc.abstractmethod
    def ota_meas_sensitivity(self):
        '''
               this is a function meas tx power
               :return: (indicator,value)   indicator is to show if the meas is running normally or something happend
               such as:0 for normal
                       1 for measurement timeout , this exception is critical
                       2 for signalling error,    this exception is fixable
                       3 for .....
               and these exceptions should be handled in the full procedure.
               as if we got 1, then we should pop an messagebox for fixed second, and tell the tester, this point will be skipped.
               as we got 2, the we should reestablish the call and remeas, it should be able to fix the problem. and pop a connection dialog and try to connect.
               '''

    @abc.abstractmethod
    def ota_meas_rssi(self):
        '''
               this is a function meas tx power
               :return: (indicator,value)   indicator is to show if the meas is running normally or something happend
               such as:0 for normal
                       1 for measurement timeout , this exception is critical
                       2 for signalling error,    this exception is fixable
                       3 for .....
               and these exceptions should be handled in the full procedure.
               as if we got 1, then we should pop an messagebox for fixed second, and tell the tester, this point will be skipped.
               as we got 2, the we should reestablish the call and remeas, it should be able to fix the problem. and pop a connection dialog and try to connect.
               '''

    @abc.abstractmethod
    def ota_set_freq(self):
        pass

    @abc.abstractmethod
    def ota_set_channel(self):
        pass

class IConfigurable():
    @abc.abstractmethod
    def set_parameters(self, parameter: dict):
        ' this dict can be delta or actually'
        pass

    @abc.abstractmethod
    def get_parameters(self) -> dict:
        pass


class SnapShot:
    @abc.abstractmethod
    def save_snapshot(self, param):
        """
        This method is to save instrument's setting -> quick save
        :param param: name of sav file, should be anything any type you want
        :return: None 
        """
        file_path = os.path.join(os.path.dirname(__file__), 'config', str(param) + '.sav')
        with open(file_path, 'w') as f:
            f.write(json.dumps(self.get_parameters()))

    @abc.abstractmethod
    def load_snapshot(self, param):
        """
        This method is to set quick save -> instrument's setting
        :param param: name of sav file, should be anything any type you want
        :return: None
        """
        file_path = os.path.join(os.path.dirname(__file__), 'config', str(param) + '.sav')
        with open(file_path, 'r') as f:
            self.set_parameters(json.loads(f.read()))

