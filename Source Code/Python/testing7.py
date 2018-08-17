CONFigure:WLAN:MEAS:MEValuation:SCOunt:MODulation 20
CONFigure:WLAN:MEAS:MEValuation:SCOunt:PVTime 20
CONFigure:WLAN:MEAS:MEValuation:SCOunt:TSMask 20
CONFigure:WLAN:MEAS:MEValuation:COMPensation:CESTimation PAYL
CONFigure:WLAN:MEAS:MEValuation:COMPensation:TRACking:PHASe OFF
CONFigure:WLAN:MEAS:MEValuation:SCONdition SLFail
CONFigure:WLAN:MEAS:MEValuation:MOEXception ON
CONFigure:WLAN:MEAS:MEValuation:TSMask:TROTime 0.0001
CONFigure:WLAN:MEAS:MEValuation:TSMask:AFFTnum 5


CONFigure:WLAN:MEAS:MEValuation:RESult ON,ON,ON,ON,ON,ON,ON,ON


TRIGger:WLAN:MEAS:MEValuation:SOURce 'IF Power'
TRIGger:WLAN:MEAS:MEValuation:TOUT 1
TRIGger:WLAN:MEAS:MEValuation:THReshold -25
TRIGger:WLAN:MEAS:MEValuation:SLOPe REDGe
TRIGger:WLAN:MEAS:MEValuation:MGAP 0.00002


FETCh:WLAN:MEAS:MEValuation:MODulation:OFDM:CURRent?
FETCh:WLAN:MEAS:MEValuation:TSMask:OFDM:AVERage?
FETCh:WLAN:MEAS:MEValuation:SFLatness:MINimum?
FETCh:WLAN:MEAS:MEValuation:SFLatness:X:MINimum?
FETCh:WLAN:MEAS:MEValuation:SFLatness:AVERage?


FETCh:WLAN:MEAS:MEValuation:MODulation:DSSS:CURRent?
FETCh:WLAN:MEAS:MEValuation:TSMask:DSSS:AVERage?
FETCh:WLAN:MEAS:MEValuation:PVTime:REDGe:AVERage?
FETCh:WLAN:MEAS:MEValuation:PVTime:FEDGe:AVERage?


INIT:WLAN:MEAS:MEValuation
ROUTe:WLAN:MEAS<i>:SCENario:CSPath