#!/usr/bin/python
# coding:utf-8
__Author__ = 'Adair.l'
from labinstrument.SS.CMW500.CMW500_WIFI.CMW500_WIFI import *



if __name__ == '__main__':
    instrument=CMW_WIFI(17)

    # tx test
    # 11b
    for channel in [1,6,13]:
        instrument.load_snapshot('11b_conducted_power')
        instrument.standard='BSTD'
        instrument.uddrate_mode='ENAB'
        instrument.DSSS_rate=
        power=instrument.meas_tx_ping()
        print('{} {} {}:{}'.format('b',channel,))
    # 11g
    # 11n


    for standard in ['a','n']:
        for channel in [36,40,44,48,60,100,120,132,140,157,161,165]:
            pass





