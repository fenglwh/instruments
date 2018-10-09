from labinstrument.SS.CMW500.CMW500_WIFI.CMW500_WIFI import CMW_WIFI



if __name__ == '__main__':
    instrument=CMW_WIFI(17)
    print(instrument.standard)
    print(instrument.uddrate_mode)
    print(instrument.DSSS_rate)
    print(instrument.OFDM_rate)
    print(instrument.OMCS_rate)
    instrument.tx_modulation_format='ODFM'
    print(instrument.MFR_control_rate)
    print(instrument.query('FETCh:WLAN:MEAS:MEValuation:MODulation:OFDM:AVERage?'))
    print(instrument.query('CONFigure:WLAN:MEAS:ISIGnal:STANdard?'))
    print(instrument.query('FETCh:WLAN:MEAS:MEValuation:MODulation:AVERage?'))
    print(instrument.query('FETCh:WLAN:MEAS:MEValuation:MODulation:OFDM:AVERage?'))