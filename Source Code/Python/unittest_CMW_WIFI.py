from labinstrument.SS.CMW500.CMW500_WIFI.CMW500_WIFI import CMW_WIFI

if __name__ == '__main__':
    instrument=CMW_WIFI(20)
    instrument.signal_off()
    instrument.signal_on()