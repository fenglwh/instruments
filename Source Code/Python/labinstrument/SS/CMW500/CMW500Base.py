#! /usr/bin/python
# ___________________________
# Author: Adair 2018
# Do not use in other program without permission
# If shared, pls keep this information
# ___________________________
from ...remote import *
class CMW500Base(GPIB):

    def __init__(self,connect_string='',signalling_no=1):
        super(CMW500Base, self).__init__(connect_string)
        self.signalling_No=signalling_no

    def CLS(self):
        '''Clear Status:  status byte,  event register, Operation register'''
        self.write('*CLS')

    def DEV(self):
        '''Query the device SN'''
        return self.query('*DEV?')

    def OPC(self):
        '''Operation comleted'''
        return self.query('*OPC')

    def OPT(self):
        '''get options installed'''
        return self.query('SYSTem::BASE::OPTIon::LIST?')

    def save(self,index):
        self.write('*SAV {}'.format(index))

    def recall(self,index):
        self.write('*RCL {}'.format(index))

    def save_file(self,index,file_name):
        self.save(index)
        self.write("MMEM:STORe:STATe {},'@SAVE\{}.dfl'".format(index,file_name))


    def recall_file(self,index,file_name):
        self.write("MMEM:LOAD:STATe {},'@SAVE\{}.dfl'".format(index,file_name))
        self.recall(index)

    def GTR(self):
        self.write('*GTR')

    def hide_remote_screen(self):
        self.write('SYSTem:DISPlay:UPDate OFF')

    def show_remote_screen(self):
        self.write('SYSTem:DISPlay:UPDate ON')

    def get_SW_version(self):
        return dict(x.split(',') for x in self.query('SYST:BASE:OPT:VERS?').split(';'))


