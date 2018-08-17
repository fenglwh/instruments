#!/usr/bin/python
import re

__Author__ = 'Adair.l'
from ....Interface import *
from ..CMW500Base import *
import time



class CMW_WIFI(CMW500Base, IConfigurable,SnapShot, OTASSInterface):
    def __init__(self, *args, **kwargs):
        super(CMW_WIFI, self).__init__(*args, **kwargs)
        self.GTL()
        self.tx_modulation_format='OFDM'

    def translate_datarate(self,datarate):
        dataratemap={
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
            '':'',
        }
        return

    # signalling

    def __set_signalling_state(self, state):
        self.write('SOURce:WLAN:SIGN<i>:STATe {}'.replace('<i>', str(self.signalling_No)).format(state))

    def __get_signalling_state(self):
        return self.query('SOURce:WLAN:SIGN<i>:STATe?'.replace('<i>', str(self.signalling_No)))

    def signal_on(self):
        while self.signal_state != 'ON':
            if self.signal_state == 'OFF':
                self.signal_state = 'ON'
            elif self.signal_state == 'PEND':
                time.sleep(0.2)

    def signal_off(self):
        while self.signal_state != 'OFF':
            if self.signal_state == 'ON':
                self.signal_state = 'OFF'
            elif self.signal_state == 'PEND':
                time.sleep(0.2)

    def signal_restart(self):
        self.signal_off()
        self.signal_on()

    def connected_bool(self):
        if self.connected()=='ASS':
            return 1
        else:
            return 0

    def connected(self):
        'FETCh:WLAN:SIGN<i>:PSWitched:STATe?'
        'IDLE | PROBed | AUTHenticated | ASSociated | DEAuthenticated | DISassociated | CTIMeout'
        # IDLE   PROB     AUTH            ASS          DEA               DIS             CTIMeout
        return self.query('FETCh:WLAN:SIGN<i>:PSWitched:STATe?'.replace('<i>', str(self.signalling_No)))

    def wait_for_connect(self,trigger=0):
        while not trigger:
            self.signal_on()
            if self.connected()=='ASS':
                return 1
            else:
                time.sleep(0.2)

    def connect(self):
        self.write('CALL:WLAN:SIGN<i>:ACTion:STATion:CONNect'.replace('<i>', str(self.signalling_No)))

    def disconnect(self):
        self.write('CALL:WLAN:SIGN<i>:ACTion:DISConnect'.replace('<i>', str(self.signalling_No)))

    def reconnect(self):
        self.write('CALL:WLAN:SIGN<i>:ACTion:STATion:REConnect'.replace('<i>', str(self.signalling_No)))

    def WIFI_direct_connect(self):
        self.write('CALL:WLAN:SIGN<i>:ACTion:WDIRect:SCONnection'.replace('<i>', str(self.signalling_No)))

    def WPS_connect(self):
        self.write('CALL:WLAN:SIGN<i>:ACTion:WPS:SCONnection'.replace('<i>', str(self.signalling_No)))

    # RF setting

    def __set_freq(self, freq):
        self.write('CONFigure:WLAN:SIGN<i>:RFSettings:FREQuency {}'.replace('<i>', str(self.signalling_No)).format(
            freq))

    def __get_freq(self):
        return str(eval(self.query(
            'CONFigure:WLAN:SIGN<i>:RFSettings:FREQuency?'.replace('<i>', str(self.signalling_No)))) / 1000000)

    def __set_channel(self, channel):
        self.write(
            'CONFigure:WLAN:SIGN<i>:RFSettings:CHANnel {}'.format(channel).replace('<i>', str(self.signalling_No)))

    def __get_channel(self):
        return self.query('CONFigure:WLAN:SIGN<i>:RFSettings:CHANnel?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_burst_power(self, power):
        self.write('CONFigure:WLAN:SIGN<i>:RFSettings:BOPower {}'.format(power).replace('<i>', str(self.signalling_No)))

    def __get_tx_burst_power(self):
        return str(
            eval(self.query('CONFigure:WLAN:SIGN<i>:RFSettings:BOPower?'.replace('<i>', str(self.signalling_No)))))

    def __set_PEP_power(self, power):
        self.write(
            'CONFigure:WLAN:SIGN<i>:RFSettings:EPEPower {}'.format(power).replace('<i>', str(self.signalling_No)))

    def __get_PEP_power(self):
        return str(
            eval(self.query('CONFigure:WLAN:SIGN<i>:RFSettings:EPEPower?'.replace('<i>', str(self.signalling_No)))))

    def __set_operation_mode(self, mode):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:OMODe {}'.format(mode).replace('<i>', str(self.signalling_No)))

    def __get_operation_mode(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:OMODe?'.replace('<i>', str(self.signalling_No)))

    def __set_standard(self, standard):
        '''

        :param standard:  
        :return: BSTD GSTD ASTD GOST(G_OFDM/N)  NGFS  ANST  GNST   GONS
        '''
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:STANdard {}'.format(standard).replace('<i>', str(self.signalling_No)))

    def __get_standard(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:STANdard?'.replace('<i>', str(self.signalling_No)))

    def __set_bandwidth(self, bw):
        self.write(
            'CONFigure:WLAN:SIGN<i>:RFSettings:BWIDth {}'.format(bw * 1000000).replace('<i>', str(self.signalling_No)))

    def __get_bandwidth(self):
        return str(eval(
            self.query('CONFigure:WLAN:SIGN<i>:RFSettings:BWIDth?'.replace('<i>', str(self.signalling_No)))) / 1000000)

    def __set_senario(self, senario):
        self.write('ROUTe:WLAN:SIGN<i>:SCENario {}'.format(senario).replace('<i>', str(self.signalling_No)))

    def __get_senario(self):
        return self.query('ROUTe:WLAN:SIGN<i>:SCENario?'.replace('<i>', str(self.signalling_No)))

    def __set_mimo_path(self, path):
        self.write('ROUTe:WLAN:SIGN<i>:SCENario:MIMO {}'.format(path).replace('<i>', str(self.signalling_No)))

    def __get_mimo_path(self):
        return self.query('ROUTe:WLAN:SIGN<i>:SCENario:MIMO?'.replace('<i>', str(self.signalling_No)))

    def __set_path(self, path):
        self.write('ROUTe:WLAN:SIGN<i>:SCENario:SCELl {}'.format(path).replace('<i>', str(self.signalling_No)))

    def __get_path(self):
        return self.query('ROUTe:WLAN:SIGN<i>:SCENario:SCELl?'.replace('<i>', str(self.signalling_No)))

    def set_tx_port(self, port):
        '''!!! This function is used in single tx, and should not be used in mimo, will improve or remove'''
        re_result = re.fullmatch('RF(.{2}),RX1,RF(.{2}),TX1', self.path)
        rx_port = re_result.group(1)
        tx_port = re_result.group(2)
        self.path = 'RF{},RX1,RF{},TX1'.format(rx_port, port)

    def set_rx_port(self, port):
        '''!!! This function is used in single tx, and should not be used in mimo, will improve or remove'''
        re_result = re.fullmatch('RF(.{2}),RX1,RF(.{2}),TX1', self.path)
        rx_port = re_result.group(1)
        tx_port = re_result.group(2)
        self.path = 'RF{},RX1,RF{},TX1'.format(port, tx_port)

    def __set_input_attanuation(self, att_in):
        '!!!should take mimo as consideration too'
        self.write('CONFigure:WLAN:SIGN<i>:RFSettings:EATTenuation:INPut {}'.format(att_in).replace('<i>', str(
            self.signalling_No)))

    def __get_input_attanuation(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:RFSettings:EATTenuation:INPut?'.replace('<i>', str(self.signalling_No)))

    def __set_output_attanuation(self, att_out):
        self.write('CONFigure:WLAN:SIGN<i>:RFSettings:EATTenuation:OUTPut {}'.format(att_out).replace('<i>', str(
            self.signalling_No)))

    def __get_output_attanuation(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:RFSettings:EATTenuation:OUTPut?'.replace('<i>', str(self.signalling_No)))

    def set_attenuation(self, att_in, attout):
        pass

    def get_attenuation(self):
        pass

    def __set_RX_mix_level_offset(self, value):
        self.write(
            'CONFigure:WLAN:SIGN<i>:RFSettings:MLOFfset {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_RX_mix_level_offset(self):
        return self.query('CONFigure:WLAN:SIGN<i>:RFSettings:MLOFfset?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_MIMO_mode(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:MIMO:TMMode {}'.replace('<i>', str(self.signalling_No)))

    def __get_tx_MIMO_mode(self):
        return self.query('CONFigure:WLAN:SIGN<i>:MIMO:TMMode?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_MIMO_CSD(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:MIMO:TCSD {}'.replace('<i>', str(self.signalling_No)))

    def __get_tx_MIMO_CSD(self):
        return self.query('CONFigure:WLAN:SIGN<i>:MIMO:TCSD?'.replace('<i>', str(self.signalling_No)))

    # connection

    def __set_beacon_interval(self, interval):
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:BEACon {}'.format(interval).replace('<i>', str(self.signalling_No)))

    def __get_beacon_interval(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:BEACon?'.replace('<i>', str(self.signalling_No)))

    def __set_dim_period(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:DPERiod {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_dim_period(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:DPERiod?'.replace('<i>', str(self.signalling_No)))

    def __set_BSSID(self, bssid):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:BSSid {}'.format(bssid).replace('<i>', str(self.signalling_No)))

    def __get_BSSID(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:BSSid?'.replace('<i>', str(self.signalling_No)))

    def __set_SSID(self, ssid):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SSID {}'.format(ssid).replace('<i>', str(self.signalling_No)))

    def __get_SSID(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:SSID?'.replace('<i>', str(self.signalling_No)))

    def __set_country_code_config(self,country_code_settings):
        # should as format US,1,13,0
        self.write('CONF:WLAN:SIGN<i>:CONN:CCODe:CCConf {}'.format(country_code_settings).replace('<i>', str(self.signalling_No)))

    def __get_country_code_config(self):
        return self.query('CONF:WLAN:SIGN<i>:CONN:CCODe:CCConf?'.replace('<i>', str(self.signalling_No)))

    def __set_country_code_state(self,country_code_state):
        self.write('CONF:WLAN:SIGN<i>:CONN:CCODe:CCST {}'.format(country_code_state).replace('<i>', str(self.signalling_No)))

    def __get_country_code_state(self):
        return self.query('CONF:WLAN:SIGN<i>:CONN:CCOD:CCST?'.replace('<i>', str(self.signalling_No)))

    def __set_WIFI_direct_authentication_type(self, authentication_type):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:WDIRect:ATYPe {}'.format(authentication_type).replace('<i>', str(
            self.signalling_No)))

    def __get_WIFI_direct_authentication_type(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:WDIRect:ATYPe?'.replace('<i>', str(self.signalling_No)))

    def __set_WIFI_direct_config(self, config):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:WDIRect:WDConf {}'.format(config).replace('<i>', str(
            self.signalling_No)))

    def __get_WIFI_direct_config(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:WDIRect:WDConf?'.replace('<i>', str(self.signalling_No)))

    # !!! hot spot not finished

    def __set_uddrate_mode(self, bool_value):
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:SRATes {}'.format('ENABle' if bool_value else 'DISable').replace('<i>',
                                                                                                                str(
                                                                                                                    self.signalling_No)))
        'ENABle | DISable'

    def __get_uddrate_mode(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:SRATes?'.replace('<i>', str(self.signalling_No))) == 'ENAB'

    def __set_DSSS_rate(self, value):
        # we concern this func will get two input types,one is the default CMW define
        # the other is indexed 0 for disabled, 1 for mandatory, 2 for supported
        # DSSS [1,2,5.5,11]
        # MAND,DIS,DIS,DIS
        # OFDM [6, 9, 12, 18, 24, 36, 48, 54]
        # MCS [0,1,2,3,4,5,6,7]
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SRATes:DSSSconf {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_DSSS_rate(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:SRATes:DSSSconf?'.replace('<i>', str(self.signalling_No)))

    def __set_OFDM_rate(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SRATes:OFDMconf {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_OFDM_rate(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:SRATes:OFDMconf?'.replace('<i>', str(self.signalling_No)))

    def __set_OMCS_rate(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SRATes:OMCSconf {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_OMCS_rate(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:SRATes:OMCSconf?'.replace('<i>', str(self.signalling_No)))

    def __set_MFR_control_rate(self, value):
        # ENAB DIS
        # D1MB D2MB C55M C11M BR12 BR34 QR12 QR34 Q1M12 Q1M34 Q6M23 Q634
        # 1    2    5.5  11   6    9    12   18   24    36    48    54
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:MFRControl {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_MFR_control_rate(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:MFRControl?'.replace('<i>', str(self.signalling_No)))

    def __set_DFR_control_rate(self, value):
        # ENAB DIS
        # D1MB D2MB C55M C11M BR12 BR34 QR12 QR34 Q1M12 Q1M34 Q6M23 Q634
        # 1    2    5.5  11   6    9    12   18   24    36    48    54
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:DFRControl {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_DFR_control_rate(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:DFRControl?'.replace('<i>', str(self.signalling_No)))

    def __set_rx_filter(self, value):
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:RXFilter {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_rx_filter(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:RXFilter?'.replace('<i>', str(self.signalling_No)))

    def __set_connection_mode(self, value):
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:STATion:CMODe {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_connection_mode(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:STATion:CMODe?'.replace('<i>', str(self.signalling_No)))

    def __set_SSID_connection(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:STATion:SCONnection {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_SSID_connection(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:STATion:SCONnection?'.replace('<i>', str(self.signalling_No)))

    def __set_security_type(self, value):
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:TYPE {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_security_type(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:TYPE?'.replace('<i>', str(self.signalling_No)))

    def __set_security_encrypt_type(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:ENCRyption {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_security_encrypt_type(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:ENCRyption?'.replace('<i>', str(self.signalling_No)))

    # !!! WPA place here, should finished in days.

    def __set_WPS_authentication_type(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:WPS:ATYPe {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_authentication_type(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:WPS:ATYPe?'.replace('<i>', str(self.signalling_No)))

    def __set_WPS_radius_server_mode(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:RSERver:MODE {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_radius_server_mode(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:RSERver:MODE?'.replace('<i>', str(self.signalling_No)))

    def __set_WPS_radius_server_IP(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:RSERver:ICONf {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_radius_server_IP(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:RSERver:ICONf?'.replace('<i>', str(self.signalling_No)))

    def __set_WPS_radius_server_pharase(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:RSERver:PNUMber {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_radius_server_pharase(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:RSERver:PNUMber?'.replace('<i>', str(self.signalling_No)))

    def __set_WPS_radius_server_security_key(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:RSERver:SKEY {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_radius_server_security_key(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:RSERver:SKEY?'.replace('<i>', str(self.signalling_No)))

    def __set_WPS_radius_server_ESIM_keyone(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:ESIM:KTONe {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_radius_server_ESIM_keyone(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:ESIM:KTONe?'.replace('<i>', str(self.signalling_No)))

    def __set_WPS_radius_server_ESIM_keytwo(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:ESIM:KTTWo {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_radius_server_ESIM_keytwo(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:ESIM:KTTWo?'.replace('<i>', str(self.signalling_No)))

    def __set_WPS_radius_server_ESIM_keythree(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:ESIM:KTTHree {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_radius_server_ESIM_keythree(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:ESIM:KTTHree?'.replace('<i>', str(self.signalling_No)))

    def __set_WPS_radius_server_EAP_AKA(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:CONNection:SECurity:EAKA:KALGo {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_WPS_radius_server_EAP_AKA(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:CONNection:SECurity:EAKA:KALGo?'.replace('<i>', str(self.signalling_No)))

    # Trigger

    def __set_tx_mac_frame_trigger(self, value):
        self.write('TRIGger:WLAN:SIGN<i>:TX:MACFrame:SLOPe {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_mac_frame_trigger(self):
        return self.query('TRIGger:WLAN:SIGN<i>:TX:MACFrame:SLOPe?'.replace('<i>', str(self.signalling_No)))

    def __set_rx_mac_frame_trigger(self, value):
        self.write('TRIGger:WLAN:SIGN<i>:TX:MACFrame:SLOPe {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_rx_mac_frame_trigger(self):
        return self.query('TRIGger:WLAN:SIGN<i>:TX:MACFrame:SLOPe?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_mac_frame_pulse_length_mode(self, value):
        self.write(
            'TRIGger:WLAN:SIGN<i>:TX:MACFrame:PLENgth:MODE {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_mac_frame_pulse_length_mode(self):
        return self.query('TRIGger:WLAN:SIGN<i>:TX:MACFrame:PLENgth:MODE?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_mac_frame_pulse_length_value(self, value):
        self.write(
            'TRIGger:WLAN:SIGN<i>:TX:MACFrame:PLENgth:VALue {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_mac_frame_pulse_length_value(self):
        return self.query('TRIGger:WLAN:SIGN<i>:TX:MACFrame:PLENgth:VALue?'.replace('<i>', str(self.signalling_No)))

    def __set_rx_mac_frame_mode(self, value):
        self.write('TRIGger:WLAN:SIGN<i>:RX:MACFrame:BTYPe {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_rx_mac_frame_mode(self):
        return self.query('TRIGger:WLAN:SIGN<i>:RX:MACFrame:BTYPe?'.replace('<i>', str(self.signalling_No)))

    def __set_rx_mac_frame_min_length(self, value):
        self.write('TRIGger:WLAN:SIGN<i>:RX:MACFrame:MLENgth {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_rx_mac_frame_min_length(self):
        return self.query('TRIGger:WLAN:SIGN<i>:RX:MACFrame:MLENgth?'.replace('<i>', str(self.signalling_No)))

    def __set_rx_mac_frame_pulse_length_mode(self, value):
        self.write(
            'TRIGger:WLAN:SIGN<i>:RX:MACFrame:PLENgth:MODE {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_rx_mac_frame_pulse_length_mode(self):
        return self.query('TRIGger:WLAN:SIGN<i>:RX:MACFrame:PLENgth:MODE?'.replace('<i>', str(self.signalling_No)))

    def __set_rx_mac_frame_pulse_length_value(self, value):
        self.write(
            'TRIGger:WLAN:SIGN<i>:RX:MACFrame:PLENgth:VALue {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_rx_mac_frame_pulse_length_value(self):
        return self.query('TRIGger:WLAN:SIGN<i>:RX:MACFrame:PLENgth:VALue?'.replace('<i>', str(self.signalling_No)))

    # IP interface

    def __set_IP_version(self, value):
        self.write(
            'CONFigure:WLAN:SIGN<i>:CONNection:IVSupport {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_IP_version(self):
        return self.query('CONFigure:WLAN:SIGN<i>:CONNection:IVSupport?'.replace('<i>', str(self.signalling_No)))

    def __set_IPV4_stack(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:IPVFour:STATic:IPADdress:STACk {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_IPV4_stack(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:IPVFour:STATic:IPADdress:STACk?'.replace('<i>', str(self.signalling_No)))

    def __set_IPV4_destination(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:IPVFour:STATic:IPADdress:DESTination {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_IPV4_destination(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:IPVFour:STATic:IPADdress:DESTination?'.replace('<i>', str(self.signalling_No)))

    def __set_IPV4_subnet_mask(self, value):
        self.write(
            'CONFigure:WLAN:SIGN<i>:IPVFour:STATic:SMASk {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_IPV4_subnet_mask(self):
        return self.query('CONFigure:WLAN:SIGN<i>:IPVFour:STATic:SMASk?'.replace('<i>', str(self.signalling_No)))

    def __set_IPV4_gateway(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:IPVFour:STATic:IPADdress:GATeway {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_IPV4_gateway(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:IPVFour:STATic:IPADdress:GATeway?'.replace('<i>', str(self.signalling_No)))

    def __set_IPV4_DNS(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:IPVFour:STATic:IPADdress:DNS {}'.format(value).replace('<i>', str(
            self.signalling_No)))

    def __get_IPV4_DNS(self):
        return self.query(
            'CONFigure:WLAN:SIGN<i>:IPVFour:STATic:IPADdress:DNS?'.replace('<i>', str(self.signalling_No)))

    def __set_IPV4_DHCP(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:IPVFour:DHCP {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_IPV4_DHCP(self):
        return self.query('CONFigure:WLAN:SIGN<i>:IPVFour:DHCP?'.replace('<i>', str(self.signalling_No)))

    def __set_IPV6_prefix(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:IPVSix:PREFix {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_IPV6_prefix(self):
        return self.query('CONFigure:WLAN:SIGN<i>:IPVSix:PREFix?'.replace('<i>', str(self.signalling_No)))

    # packet generator

    def __set_packet_generator(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PGEN:CONFig {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_packet_generator(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PGEN:CONFig?'.replace('<i>', str(self.signalling_No)))

    def __set_packet_generator_protocol(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PGEN:PROTocol {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_packet_generator_protocol(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PGEN:PROTocol?'.replace('<i>', str(self.signalling_No)))

    def __set_packet_generator_IP(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PGEN:IPVersion {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_packet_generator_IP(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PGEN:IPVersion?'.replace('<i>', str(self.signalling_No)))

    def __set_packet_generator_UDP_port(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PGEN:UPORts {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_packet_generator_UDP_port(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PGEN:UPORts?'.replace('<i>', str(self.signalling_No)))

    # tx test
    def __set_tx_CSP(self,value):
        self.write('ROUTe:WLAN:MEAS<i>:SCENario:CSPath {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_CSP(self):
        return self.query('ROUTe:WLAN:MEAS<i>:SCENario:CSPath?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_modulation(self,value):
        self.write('CONFigure:WLAN:MEAS<i>:MEValuation:SCOunt:MODulation {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_modulateion(self):
        return self.query('CONFigure:WLAN:MEAS<i>:MEValuation:SCOunt:MODulation?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_PVTime(self,value):
        self.write('CONFigure:WLAN:MEAS<i>:MEValuation:SCOunt:PVTime {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_PVTime(self):
        return self.query('CONFigure:WLAN:MEAS<i>:MEValuation:SCOunt:PVTime?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_TSMask(self,value):
        self.write('CONFigure:WLAN:MEAS<i>:MEValuation:SCOunt:TSMask {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_TSMask(self):
        return self.query('CONFigure:WLAN:MEAS<i>:MEValuation:SCOunt:TSMask?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_trigger_source(self,value):
        self.write('TRIGger:WLAN:MEAS<i>:MEValuation:SOURce {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_trigger_source(self):
        return self.query('TRIGger:WLAN:MEAS<i>:MEValuation:SOURce?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_trigger_timeout(self, value):
        self.write('TRIGger:WLAN:MEAS<i>:MEValuation:TOUT {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_trigger_timeout(self):
        return self.query('TRIGger:WLAN:MEAS<i>:MEValuation:TOUT?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_trigger_threshold(self, value):
        self.write('TRIGger:WLAN:MEAS<i>:MEValuation:THReshold {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_trigger_threshold(self):
        return self.query('TRIGger:WLAN:MEAS<i>:MEValuation:THReshold?'.replace('<i>', str(self.signalling_No)))

    def __set_tx_trigger_slope(self, value):
        self.write('TRIGger:WLAN:MEAS<i>:MEValuation:SLOPe {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_tx_trigger_slope(self):
        return self.query('TRIGger:WLAN:MEAS<i>:MEValuation:SLOPe?'.replace('<i>', str(self.signalling_No)))


    def init_tx_measurement(self):
        self.write('INITiate:WLAN:MEAS<i>:MEValuation'.replace('<i>', str(self.signalling_No)))

    def stop_tx_measurement(self):
        self.write('STOP:WLAN:MEAS<i>:MEValuation'.replace('<i>', str(self.signalling_No)))

    def abort_tx_measurement(self):
        self.write('ABORt:WLAN:MEAS<i>:MEValuation'.replace('<i>', str(self.signalling_No)))

    def get_tx_state(self):
        return self.query('FETCh:WLAN:MEAS<i>:MEValuation:STATe?'.replace('<i>', str(self.signalling_No)))

    def get_tx_state_all(self):
        return self.query('FETCh:WLAN:MEAS<i>:MEValuation:STATe:ALL?'.replace('<i>', str(self.signalling_No)))

    def get_tx_result(self):
        tmp='FETCh:WLAN:MEAS:MEValuation:MODulation:{}:AVERage?'.format(self.tx_modulation_format).replace('<i>', str(self.signalling_No))
        result= self.query(tmp)
        splited=[x for x in result.split(',')]
        reality_indicator=splited[0]
        datarate=splited[1]
        package_length=splited[2]
        burst_power=splited[3]
        EVM_all_carrier=splited[4]
        EVM_data_carrier=splited[5]
        EVM_pilot_carrier=splited[6]
        center_frequency_error=splited[7]
        symbol_clock_error=splited[8]
        IQ_offset=splited[9]
        gain_imbalance=splited[10]
        quadrature_error=splited[11]
        return {'power':burst_power,'reality_indicator':reality_indicator,'datarate':datarate,'package_length':package_length}

    # rx test

    def PER(self):
            return self.query('FETCh:WLAN:SIGN<i>:PER?'.replace('<i>', str(self.signalling_No)))
        # 'READ:WLAN:SIGN<i>:PER?'

    def get_ul_package_rate(self):
        return self.query('READ:WLAN:SIGN<i>:PER?'.replace('<i>', str(self.signalling_No)))

    def __set_dl_package_rate(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PER:MCRate {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_dl_package_rate(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PER:MCRate?'.replace('<i>', str(self.signalling_No)))

    def init_per_measurement(self):
        self.write('INITiate:WLAN:SIGN<i>:PER'.replace('<i>', str(self.signalling_No)))

    def stop_per_measurement(self):
        self.write('STOP:WLAN:SIGN<i>:PER'.replace('<i>', str(self.signalling_No)))

    def abort_per_measurement(self):
        self.write('ABORt:WLAN:SIGN<i>:PER'.replace('<i>', str(self.signalling_No)))

    def get_per_state(self):
        return self.query('FETCh:WLAN:SIGN<i>:PER:STATe?'.replace('<i>', str(self.signalling_No)))

    def get_per_state_all(self):
        return self.query('FETCh:WLAN:SIGN<i>:PER:STATe:ALL?'.replace('<i>', str(self.signalling_No)))

    def __set_ack_type(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PER:ATYPe {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_ack_type(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PER:ATYPe?'.replace('<i>', str(self.signalling_No)))

    def __set_data_pattern(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PER:DPATtern {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_date_pattern(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PER:DPATtern?'.replace('<i>', str(self.signalling_No)))

    def __set_packet_num(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PER:PACKets {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_packet_num(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PER:PACKets?'.replace('<i>', str(self.signalling_No)))

    def __set_data_interval(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PER:DINTerval {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_data_interval(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PER:DINTerval?'.replace('<i>', str(self.signalling_No)))

    def __set_payload_size(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PER:PAYLoad:SIZE{}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_payload_size(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PER:PAYLoad:SIZE?'.replace('<i>', str(self.signalling_No)))

    def __set_PER_limit(self, value):
        self.write('CONFigure:WLAN:SIGN<i>:PER:LIMit {}'.format(value).replace('<i>', str(self.signalling_No)))

    def __get_PER_limit(self):
        return self.query('CONFigure:WLAN:SIGN<i>:PER:LIMit?'.replace('<i>', str(self.signalling_No)))



    # info

    def get_AP_SSID(self):
        return self.query('SENSe:WLAN:SIGN<i>:STAinfo:APSSid?'.replace('<i>', str(self.signalling_No)))

    def get_DUT_MAC(self):
        return self.query('SENSe:WLAN:SIGN<i>:UECapability:MAC:ADDRess?'.replace('<i>', str(self.signalling_No)))

    def get_DUT_MAC_version(self):
        return self.query('SENSe:WLAN:SIGN<i>:UECapability:MAC:VERSion?'.replace('<i>', str(self.signalling_No)))

    def get_IP_address(self):
        return self.query('SENSe:WLAN:SIGN<i>:UESinfo:UEADdress:IPV<n>?'.replace('<i>', str(self.signalling_No)))





    # config ,all status this part should be changable when operation mode changes!!!

    def __get_all_status(self):
        ret_val={}
        ret_val['packet_generator_setting_status']=self.packet_generator_setting_status
        ret_val['RF_setting_status']=self.RF_setting_status
        ret_val['connection_setting_status']=self.connection_setting_status
        ret_val['ip_setting_status']=self.ip_setting_status
        ret_val['packet_generator_setting_status']=self.packet_generator_setting_status
        ret_val['trigger_setting_status']=self.trigger_setting_status
        ret_val['tx_setting_status']=self.tx_setting_status
        ret_val['rx_setting_status']=self.rx_setting_status
        return ret_val

    def __set_all_status(self,value):
        self.packet_generator_setting_status = value['packet_generator_setting_status']
        self.RF_setting_status = value['RF_setting_status']
        self.connection_setting_status = value['connection_setting_status']
        self.ip_setting_status = value['ip_setting_status']
        self.packet_generator_setting_status = value['packet_generator_setting_status']
        self.trigger_setting_status = value['trigger_setting_status']
        self.tx_setting_status=value['trigger_setting_status']

    def __set_setting_status(self, value):
        for k,v in value.items():
            if getattr(self,k)!=v:
                if k in ['BSSID','SSID','dim_period','operation_mode','scenario','bandwidth','standard',
                         'security_encrypt_type','security_type']:
                    self.signal_off()
                setattr(self,k,v)

    def __get_packet_generator_status(self):
        ret_val = {}
        ret_val['packet_generator'] = self.packet_generator
        ret_val['packet_generator_protocol'] = self.packet_generator_protocol
        ret_val['packet_generator_IP'] = self.packet_generator_IP
        ret_val['packet_generator_UDP_port'] = self.packet_generator_UDP_port
        return ret_val

    def __get_RF_setting_status(self):
        ret_val = {}
        ret_val['scenario'] = self.scenario
        ret_val['operation_mode'] = self.operation_mode
        ret_val['standard'] = self.standard
        ret_val['freq'] = self.freq
        ret_val['channel'] = self.channel
        ret_val['tx_power'] = self.tx_power
        ret_val['pep_power'] = self.pep_power
        ret_val['bandwidth'] = self.bandwidth
        # ret_val['mimo_path'] = self.mimo_path
        ret_val['path'] = self.path
        ret_val['input_attanuation'] = self.input_attanuation
        ret_val['output_attanuation'] = self.output_attanuation
        ret_val['rx_mix_level_offset'] = self.rx_mix_level_offset
        return ret_val

    def __get_connection_status(self):
        ret_val = {}
        ret_val['beacon_interval'] = self.beacon_interval
        ret_val['dim_period'] = self.dim_period
        ret_val['BSSID'] = self.BSSID
        ret_val['SSID'] = self.SSID
        ret_val['country_code_config'] = self.country_code_config
        ret_val['country_code_state'] = self.country_code_state
        # ret_val['WIFI_direct_authentication_type'] = self.WIFI_direct_authentication_type
        # ret_val['WIFI_direct_config'] = self.WIFI_direct_config
        ret_val['uddrate_mode'] = self.uddrate_mode
        ret_val['DSSS_rate'] = self.DSSS_rate
        ret_val['OFDM_rate'] = self.OFDM_rate
        ret_val['OMCS_rate'] = self.OMCS_rate
        ret_val['MFR_control_rate'] = self.MFR_control_rate
        ret_val['DFR_control_rate'] = self.DFR_control_rate
        ret_val['rx_filter'] = self.rx_filter
        ret_val['security_type'] = self.security_type
        ret_val['security_encrypt_type'] = self.security_encrypt_type
        return ret_val

    def __get_trigger_status(self):
        ret_val = {}
        ret_val['tx_mac_frame_trigger'] = self.tx_mac_frame_trigger
        ret_val['tx_mac_frame_pulse_length_mode'] = self.tx_mac_frame_pulse_length_mode
        ret_val['tx_mac_frame_pulse_length_value'] = self.tx_mac_frame_pulse_length_value
        ret_val['rx_mac_frame_trigger'] = self.rx_mac_frame_trigger
        ret_val['rx_mac_frame_mode'] = self.rx_mac_frame_mode
        ret_val['rx_mac_frame_pulse_length_mode'] = self.rx_mac_frame_pulse_length_mode
        ret_val['rx_mac_frame_pulse_length_value'] = self.rx_mac_frame_pulse_length_value
        ret_val['rx_mac_frame_min_length'] = self.rx_mac_frame_min_length
        return ret_val

    def __get_ip_status(self):
        ret_val = {}
        ret_val['IP_version'] = self.IP_version
        ret_val['IPV4_stack'] = self.IPV4_stack
        ret_val['IPV4_destination'] = self.IPV4_destination
        ret_val['IPV4_subnet_mask'] = self.IPV4_subnet_mask
        ret_val['IPV4_gateway'] = self.IPV4_gateway
        ret_val['IPV4_DNS'] = self.IPV4_DNS
        ret_val['IPV4_DHCP'] = self.IPV4_DHCP
        ret_val['IPV6_prefix'] = self.IPV6_prefix
        return ret_val


    def __get_tx_setting_status(self):
        ret_val = {}
        ret_val['tx_modulation'] = self.tx_modulation_format
        ret_val['tx_CSP'] = self.tx_CSP
        ret_val['tx_CSP'] = self.tx_modulation
        ret_val['tx_PVTime'] = self.tx_PVTime
        ret_val['tx_TSMask'] = self.tx_TSMask
        ret_val['tx_trigger_source'] = self.tx_trigger_source
        ret_val['tx_trigger_threshold'] = self.tx_trigger_threshold
        ret_val['tx_trigger_timeout'] = self.tx_trigger_timeout
        ret_val['tx_trigger_slope'] = self.tx_trigger_slope
        return ret_val

    def __get_rx_setting_status(self):
        ret_val = {}
        ret_val['RX_ack_type'] = self.RX_ack_type
        ret_val['RX_data_pattern'] = self.RX_data_pattern
        ret_val['RX_data_interval'] = self.RX_data_interval
        ret_val['RX_dl_packet_rate'] = self.RX_dl_packet_rate
        ret_val['RX_packet_num'] = self.RX_packet_num
        ret_val['RX_payload_size'] = self.RX_payload_size
        ret_val['RX_PER_limit'] = self.RX_PER_limit
        return ret_val


    # ____________________________Properties____________________________
    #  IDLE   PROB     AUTH            ASS          DEA               DIS             CTIMeout
    # rfsetting
    signal_state = property(__get_signalling_state, __set_signalling_state)
    freq = property(__get_freq, __set_freq)
    channel = property(__get_channel, __set_channel)
    tx_power = property(__get_tx_burst_power, __set_tx_burst_power)
    pep_power = property(__get_PEP_power, __set_PEP_power)
    # AP    STAT   IBSS   WDIR   HSP
    operation_mode = property(__get_operation_mode, __set_operation_mode)
    standard = property(__get_standard, __set_standard)
    bandwidth = property(__get_bandwidth, __set_bandwidth)
    scenario = property(__get_senario, __set_senario)
    path = property(__get_path, __set_path)
    mimo_path = property(__get_mimo_path, __set_mimo_path)
    input_attanuation = property(__get_input_attanuation, __set_input_attanuation)
    output_attanuation = property(__get_output_attanuation, __set_output_attanuation)
    rx_mix_level_offset = property(__get_RX_mix_level_offset, __set_RX_mix_level_offset)
    tx_MIMO_mode = property(__get_tx_MIMO_mode, __set_tx_MIMO_mode)
    tx_MIMO_CSD = property(__get_tx_MIMO_CSD, __set_tx_MIMO_CSD)
    #connection
    beacon_interval = property(__get_beacon_interval, __set_beacon_interval)
    dim_period=property(__get_dim_period,__set_dim_period)
    BSSID=property(__get_BSSID,__set_BSSID)
    SSID=property(__get_SSID,__set_SSID)
    country_code_config=property(__get_country_code_config,__set_country_code_config)
    country_code_state=property(__get_country_code_state,__set_country_code_state)
    WIFI_direct_authentication_type=property(__get_WIFI_direct_authentication_type,__set_WIFI_direct_authentication_type)
    WIFI_direct_config=property(__get_WIFI_direct_config,__set_WIFI_direct_config)
    uddrate_mode = property(__get_uddrate_mode, __set_uddrate_mode)
    DSSS_rate = property(__get_DSSS_rate, __set_DSSS_rate)
    OFDM_rate = property(__get_OFDM_rate, __set_OFDM_rate)
    OMCS_rate = property(__get_OMCS_rate, __set_OMCS_rate)
    MFR_control_rate = property(__get_MFR_control_rate, __set_MFR_control_rate)
    DFR_control_rate = property(__get_DFR_control_rate, __set_DFR_control_rate)
    rx_filter = property(__get_rx_filter, __set_rx_filter)
    # ap
    connection_mode = property(__get_connection_mode, __set_connection_mode)
    SSID_connection = property(__get_SSID_connection, __set_SSID_connection)
    #ap done
    security_type = property(__get_security_type, __set_security_type)
    security_encrypt_type = property(__get_security_encrypt_type, __set_security_encrypt_type)
    WPS_authentication_type = property(__get_WPS_authentication_type, __set_WPS_authentication_type)
    WPS_radius_server_mode = property(__get_WPS_radius_server_mode, __set_WPS_radius_server_mode)
    WPS_radius_server_IP = property(__get_WPS_radius_server_IP, __set_WPS_radius_server_IP)
    WPS_radius_server_pharase = property(__get_WPS_radius_server_pharase, __set_WPS_radius_server_pharase)
    WPS_radius_server_security_key = property(__get_WPS_radius_server_security_key,
                                              __set_WPS_radius_server_security_key)
    WPS_radius_server_ESIM_keyone = property(__get_WPS_radius_server_ESIM_keyone, __set_WPS_radius_server_ESIM_keyone)
    WPS_radius_server_ESIM_keytwo = property(__get_WPS_radius_server_ESIM_keytwo, __set_WPS_radius_server_ESIM_keytwo)
    WPS_radius_server_ESIM_keythree = property(__get_WPS_radius_server_ESIM_keythree,
                                               __set_WPS_radius_server_ESIM_keythree)
    WPS_radius_server_EAP_AKA = property(__get_WPS_radius_server_EAP_AKA, __set_WPS_radius_server_EAP_AKA)
    tx_mac_frame_trigger = property(__get_tx_mac_frame_trigger, __set_tx_mac_frame_trigger)
    rx_mac_frame_trigger = property(__get_rx_mac_frame_trigger, __set_rx_mac_frame_trigger)
    tx_mac_frame_pulse_length_mode = property(__get_tx_mac_frame_pulse_length_mode,
                                              __set_tx_mac_frame_pulse_length_mode)
    tx_mac_frame_pulse_length_value = property(__get_tx_mac_frame_pulse_length_value,
                                            __set_tx_mac_frame_pulse_length_value)
    rx_mac_frame_mode = property(__get_rx_mac_frame_mode, __set_rx_mac_frame_mode)
    rx_mac_frame_min_length = property(__get_rx_mac_frame_min_length, __set_rx_mac_frame_min_length)
    rx_mac_frame_pulse_length_mode = property(__get_rx_mac_frame_pulse_length_mode,
                                              __set_rx_mac_frame_pulse_length_mode)
    rx_mac_frame_pulse_length_value = property(__get_rx_mac_frame_pulse_length_value,
                                               __set_rx_mac_frame_pulse_length_value)
    IP_version = property(__get_IP_version, __set_IP_version)
    IPV4_stack = property(__get_IPV4_stack, __set_IPV4_stack)
    IPV4_destination = property(__get_IPV4_destination, __set_IPV4_destination)
    IPV4_subnet_mask = property(__get_IPV4_subnet_mask, __set_IPV4_subnet_mask)
    IPV4_gateway = property(__get_IPV4_gateway, __set_IPV4_gateway)
    IPV4_DNS = property(__get_IPV4_DNS, __set_IPV4_DNS)
    IPV4_DHCP = property(__get_IPV4_DHCP, __set_IPV4_DHCP)
    IPV6_prefix = property(__get_IPV6_prefix, __set_IPV6_prefix)
    packet_generator = property(__get_packet_generator, __set_packet_generator)
    packet_generator_protocol = property(__get_packet_generator_protocol, __set_packet_generator_protocol)
    packet_generator_IP = property(__get_packet_generator_IP, __set_packet_generator_IP)
    packet_generator_UDP_port = property(__get_packet_generator_UDP_port, __set_packet_generator_UDP_port)

    tx_CSP=property(__get_tx_CSP,__set_tx_CSP)
    tx_modulation=property(__get_tx_modulateion,__set_tx_modulation)
    tx_PVTime=property(__get_tx_PVTime,__set_tx_PVTime)
    tx_TSMask=property(__get_tx_TSMask,__set_tx_TSMask)
    tx_trigger_source=property(__get_tx_trigger_source,__set_tx_trigger_source)
    tx_trigger_timeout=property(__get_tx_trigger_timeout,__set_tx_trigger_timeout)
    tx_trigger_threshold=property(__get_tx_trigger_threshold,__set_tx_trigger_threshold)
    tx_trigger_slope=property(__get_tx_trigger_slope,__set_tx_trigger_slope)


    RX_ack_type = property(__get_ack_type, __set_ack_type)
    RX_dl_packet_rate = property(__get_dl_package_rate, __set_dl_package_rate)
    RX_data_pattern = property(__get_date_pattern, __set_data_pattern)
    RX_packet_num = property(__get_packet_num, __set_packet_num)
    RX_data_interval = property(__get_data_interval, __set_data_interval)
    RX_payload_size = property(__get_payload_size, __set_payload_size)
    RX_PER_limit = property(__get_PER_limit, __set_PER_limit)

    # ___________________________________________________________
    all_setting_status=property(__get_all_status,__set_all_status)
    RF_setting_status = property(__get_RF_setting_status, __set_setting_status)
    connection_setting_status=property(__get_connection_status,__set_setting_status)
    trigger_setting_status=property(__get_trigger_status,__set_setting_status)
    packet_generator_setting_status=property(__get_packet_generator_status,__set_setting_status)
    ip_setting_status=property(__get_ip_status,__set_setting_status)
    tx_setting_status=property(__get_tx_setting_status,__set_setting_status)
    rx_setting_status=property(__get_rx_setting_status,__set_setting_status)

    def packet_generator_ON(self):
        if 'OFF' in self.packet_generator:
            self.packet_generator=self.packet_generator.replace('OFF','ON')

    def packet_generator_OFF(self):
        if 'ON' in self.packet_generator:
            self.packet_generator=self.packet_generator.replace('ON','OFF')

    def make_a_conenction(self):
        self.signal_on()
        self.wait_for_connect()

    def meas_tx_ping(self,timeout=20):
        self.packet_generator_ON()
        if self.get_tx_state() in ['OFF','RDY']:
            self.init_tx_measurement()
        else:
            self.abort_tx_measurement()
            self.init_tx_measurement()
        time_start=datetime.datetime.now()
        while self.get_tx_state() !='RDY':
            if (datetime.datetime.now()-time_start).seconds>timeout:
                return
            time.sleep(0.2)
        return self.get_tx_result()


    def meas_tx_ack(self):
        self.packet_generator_OFF()
        if self.get_per_state() in ['OFF', 'RDY']:
            self.init_per_measurement()
        else:
            self.abort_per_measurement()
            self.init_per_measurement()
        time_start = datetime.datetime.now()
        while self.get_tx_state() != 'RDY':
            if (datetime.datetime.now() - time_start).seconds > timeout:
                return
            time.sleep(0.2)
        return float(self.PER().split(',')[4])

    def meas_rx_per(self,timeout=5):
        self.packet_generator_OFF()
        if self.get_per_state() in ['OFF', 'RDY']:
            self.init_per_measurement()
        else:
            self.abort_per_measurement()
            self.init_per_measurement()
        time_start = datetime.datetime.now()
        while self.get_per_state() not in ['RDY','OFF']:
            if (datetime.datetime.now() - time_start).seconds > timeout:
                return self.meas_rx_per()
            time.sleep(0.2)
        print(self.get_per_state())
        return float(self.PER().split(',')[1])

    def meas_rx_sensitivity(self,start=-20,limit=10,settling_time=0.1):
        step1=2
        step2=1
        step3=0.5
        self.tx_power=start
        while self.meas_rx_per()<=limit:
            self.tx_power=str(float(self.tx_power)-step1)
            time.sleep(settling_time)
            self.tx_power = str(float(self.tx_power) + step1)
        time.sleep(settling_time)
        while self.meas_rx_per()<=limit:
            self.tx_powe=str(float(self.tx_power)-step2)
            time.sleep(settling_time)
            self.tx_power = str(float(self.tx_power) + step2)
        time.sleep(settling_time)
        while 1:
            tmp=self.meas_rx_per()
            if tmp>limit:
                return int(self.meas_rx_per()) + step3
            else:
                self.tx_power=str(float(self.tx_power)-step3)
                time.sleep(settling_time)


    def set_parameters(self, parameter):
        self.signal_off()
        self.all_setting_status=parameter


    def get_parameters(self):
        return self.all_setting_status

    def save_snapshot(self, param):
        """
        This method is to save instrument's setting -> quick save
        :param param: name of sav file, should be anything any type you want
        :return: None 
        """
        file_path = os.path.join(os.path.dirname(__file__), 'config', str(param) + '.sav')
        with open(file_path, 'w') as f:
            f.write(json.dumps(self.get_parameters()))

    def load_snapshot(self, param):
        """
        This method is to set quick save -> instrument's setting
        :param param: name of sav file, should be anything any type you want
        :return: None
        """
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

















