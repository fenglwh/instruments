#!/usr/bin/python
# coding:utf-8
__Author__ = 'Adair.l'


from ....Interface import *
from ..CMW500Base import *
import time
import re



class CMW_WIFI(CMW500Base, IConfigurable,SnapShot, OTASSInterface):

    def __init__(self):
        def __init__(self, *args, **kwargs):
            super(CMW_WIFI, self).__init__(*args, **kwargs)
            self.GTL()





















    def set_parameters(self, parameter):
        self.signal_off()
        self.all_setting_status=parameter


    def get_parameters(self):
        return self.all_setting_status

    def save_snapshot(self, param):
        file_path = os.path.join(os.path.dirname(__file__), 'config', str(param) + '.sav')
        with open(file_path, 'w') as f:
            f.write(json.dumps(self.get_parameters()))

    def load_snapshot(self, param):
        file_path = os.path.join(os.path.dirname(__file__), 'config', str(param) + '.sav')
        with open(file_path, 'r') as f:
            self.set_parameters(json.loads(f.read()))

    def ota_meas_power(self):
        pass

    def ota_meas_per(self):
        pass

    def ota_meas_sensitivity(self):
        pass

    def ota_meas_rssi(self):
        pass

    def ota_set_freq(self):
        pass

    def ota_set_channel(self):
        pass