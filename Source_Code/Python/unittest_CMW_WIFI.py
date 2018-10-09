from labinstrument.SS.CMW500.CMW500_WIFI.CMW500_WIFI import CMW_WIFI

if __name__ == '__main__':
    instrument=CMW_WIFI(20)
    # status=instrument.get_parameters()
    # print(status)
    # instrument.make_a_conenction()
    # print(instrument.meas_rx_sensitivity())
    instrument.tx_power=-20





