import abc

class OTAInterface():

    @abc.abstractmethod
    def init_ota(self):
        pass

    @abc.abstractmethod
    def power_ota(self):
        pass

    @abc.abstractmethod
    def per_ota(self):
        pass

    @abc.abstractmethod
    def sensitivity_ota(self):
        pass

    @abc.abstractmethod
    def sensitivity_rssi_ota(self):
        pass

    @abc.abstractmethod
    def sensitivity_pattern_based_ota(self):
        pass

    @abc.abstractmethod
    def sensitivity_continuous_ota(self):
        pass

    @abc.abstractmethod
    def set_channel_ota(self):
        pass

    @abc.abstractmethod
    def set_freq_ota(self):
        pass
    @abc.abstractmethod
    def rotate_ota(self,poloarization,angle):
        pass
    @abc.abstractmethod
    def re_init_ota(self):
        pass
    @abc.abstractmethod
    def connect(self):
        pass
    @abc.abstractmethod
    def reconnect(self):
        pass
    @abc.abstractmethod

    def disconnect(self):
        pass

