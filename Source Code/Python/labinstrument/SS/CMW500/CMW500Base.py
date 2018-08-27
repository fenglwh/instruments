#! /usr/bin/python
# ___________________________
# Author: Adair 2018
# Do not use in other program without permission
# If shared, pls keep this information
# ___________________________
from ...remote import *


class CMW500Base(GPIB):

    def __init__(self, *args, connect_string='', signalling_no=1, **kwargs):
        super(CMW500Base, self).__init__(*args, **kwargs)
        self.signalling_No = signalling_no

    def CLS(self):
        '''Clear Status:  status byte,  event register, Operation register'''
        self.write('*CLS')

    def DEV(self):
        '''Query the device SN'''
        return self.query('*DEV?')

    def OPC(self):
        '''Operation comleted 0 for busy, 1 for idle'''

        return self.query('*OPC')

    def OPT(self):
        '''get options installed'''
        return self.query('SYSTem::BASE::OPTIon::LIST?')

    def save(self, index):
        self.write('*SAV {}'.format(index))

    def recall(self, index):
        self.write('*RCL {}'.format(index))

    def save_file(self, index, file_name):
        self.save(index)
        self.write("MMEM:STORe:STATe {},'@SAVE\{}.dfl'".format(index, file_name))

    def recall_file(self, index, file_name):
        self.write("MMEM:LOAD:STATe {},'@SAVE\{}.dfl'".format(index, file_name))
        self.recall(index)

    def GTR(self):
        self.write('*GTR')

    def hide_remote_screen(self):
        self.write('SYSTem:DISPlay:UPDate OFF')

    def show_remote_screen(self):
        self.write('SYSTem:DISPlay:UPDate ON')

    def WAI(self):
        self.write('*WAI')

    def wait_until_all_command_done(self, timeout=60):
        self.WAI()
        while not self.OPC():
            time.sleep(0.2)

    def get_SW_version(self):
        return dict(x.split(',') for x in self.query('SYST:BASE:OPT:VERS?').split(';'))

    def get_generator_on(self, re='.*'):
        return self.query('STATus:GENerator:CONDition:ON? {}'.format(re))

    def get_generator_off(self, re='.*'):
        return self.query('STATus:GENerator:CONDition:OFF? {}'.format(re))

    def get_generator_pending(self, re='.*'):
        return self.query('STATus:GENerator:CONDition:PENDing? {}'.format(re))

    def get_meas_off(self, re='.*'):
        return self.query('STATus: MEASurement:CONDition: OFF? {}'.format(re))

    def get_meas_qued(self, re='.*'):
        return self.query('STATus:MEASurement:CONDition:QUED? {}'.format(re))

    def get_meas_ready(self, re='.*'):
        return self.query('STATus:MEASurement:CONDition:RDY? {}'.format(re))

    def get_meas_run(self, re='.*'):
        return self.query('STATus:MEASurement:CONDition:RUN? {}'.format(re))

    def get_meas_SD_reached(self, re='.*'):
        return self.query('STATus:MEASurement:CONDition:SDReached? {}'.format(re))

    def get_supported_tech(self):
        tmp=self.query('SYSTem:HELP:STATus:BITS?')
        tech_list=['GPRF','LTE',"WCDMA",'TDSCDMA','CDMA','EVDO','GSM']
        supported=[]
        unknown=[]
        for line in tmp.split(','):
            for tech in tech_list:
                if ":{}:".format(tech) in line.upper():
                    if tech not in supported:
                        supported.append(tech)
                    break
            else:
                unknown.append(line)
        return supported



