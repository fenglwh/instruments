from ...remote import *
from ...Interface import *
import time

class ETS2090(IConfigurable):
    '''
    This instrment include 2 rotations, one is theta, the other is phi, so this init message should contain 2 gpib port
    '''

    def __init__(self, theta_string, phi_string):
        self.theta = simpleETS2090(theta_string)
        self.phi = simpleETS2090(phi_string)

    def set_parameters(self, parameter: dict):
        self.theta.set_parameters(parameter['theta'])
        self.phi.set_parameters(parameter['phi'])

    def get_parameters(self) -> dict:
        return {
            "theta": self.theta.get_parameters(),
            "phi": self.phi.get_parameters()
        }


class simpleETS2090(GPIB, IConfigurable):
    def __init__(self, *args, **kwargs):
        super(simpleETS2090, self).__init__(*args, **kwargs)

    def __set_lower_limit(self,value):
        self.write("CL {}".format(value))

    def __set_upper_limit(self,value):
        self.write("WL {}".format(value))

    def __get_lower_limit(self):
        return self.query("CL?")

    def __get_upper_limit(self):
        return self.query("WL?")

    def __get_speed(self):
        return self.query("S?")

    def __set_speed(self,value):
        self.write('S{}'.format(value))

    def __set_mode(self,value):
        self.write('N{}'.format(value) if type(value) is int else value)

    def __get_mode(self):
        return self.query('LV?')

    def __set_current_position(self,value):
        self.write("CP {}".format(value))

    def __get_current_position(self):
        return self.query('CP?')

    def __set_scan_count(self,value):
        self.write("CY {}".format(value))

    def __get_scan_count(self):
        return self.query("WL?")


    def seek(self,value,timeout=200):
        #second
        self.write('SK {}'.format(value))
        return self.wait_until_done(timeout)

    def seek_async(self,value,timeout=200):
        self.write('SK {}'.format(value))

    def done(self):
        return self.OPC()

    def wait_until_done(self,timeout=200):
        time_start_stamp=float(datetime.datetime.now().timestamp())
        while 1:
            if float(datetime.datetime.now().timestamp())-time_start_stamp>timeout:
                return 0
            else:
                if self.OPC()=="1":
                    return 1
                else:
                    time.sleep(0.1)

    def scan(self):
        self.write('SC')

    def is_scanning(self):
        self.query("SC?")

    def stop_scan(self):
        # !!! we should know how to stop the scanning
        pass

    def set_preset_speed(self,speed_index,speed):
        self.write("SS{} {}".format(speed_index,speed))

    def get_preset_speed(self,speed_index):
        return self.query("SS{}?".format(speed_index))

    def select_turntable_mode(self,instrument_type1,instrument_type2):
        # TT<NRM/AIR/TWO> <CONT/NONCONT>
        # NRM     Normal turntable
        # AIR     Air flotation turntable
        # TWO     Two speed turntable
        # CONT    continuous rotation turntable
        # NOCONT  Non continuous rotation turntable
        self.write("TT {} {}".format(instrument_type1,instrument_type2))

    def select_tower_mode(self,instrument_type1):
        # NRM     Normal turntable
        # BOR     Bore sight tower
        self.write("TWR {}".format(instrument_type1))

    mode=property(__get_mode,__set_mode)
    speed=property(__get_speed,__set_speed)
    current_position = property(__get_current_position, __set_current_position)
    lower_limit = property(__get_lower_limit, __set_lower_limit)
    upper_limit = property(__get_upper_limit, __set_upper_limit)


    def set_parameters(self, parameter: dict):
        if "mode" in parameter:
            self.mode=parameter['mode']
        if "speed" in parameter:
            self.speed=parameter['speed']
        if "lower limit" in parameter:
            self.lower_limit=parameter['lower limit']
        if "upper limit" in parameter:
            self.upper_limit=parameter['upper limit']

    def get_parameters(self) -> dict:
        return {
            'mode':self.mode,
            'speed':self.speed,
            'lower limit':self.lower_limit,
            'upper limit':self.upper_limit,
        }


if __name__ == '__main__':
    # init instrument
    # query idn
    # config status reporting
    # set numeric mode2
    # verify current position
    # set sw limit as needed
    # set scan count, polarization, and any other desired motion related parameters
    # send gpib command for desired motion
    # wait for motion to complete
    # monitor current position as required
    # check for operation complete
    # repeat until motion complete
    # stop all devices
    pass
