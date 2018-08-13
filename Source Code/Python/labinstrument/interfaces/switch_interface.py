import abc


class SwitchInterface():

    @abc.abstractmethod
    def switch_stat(self):
        pass
    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass
    @abc.abstractmethod
    def open_all(self):
        pass

    @abc.abstractmethod
    def open_multiple(self):
        pass

    @abc.abstractmethod
    def close_multiple(self):
        pass

