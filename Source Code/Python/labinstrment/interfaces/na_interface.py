import abc
class NAInterface:
    @abc.abstractmethod
    def peak_search(self):
        pass

    @abc.abstractmethod
    def get_linear_response(self,freq):
        pass

    @abc.abstractmethod
    def get_log_response(self,freq):
        pass
    @abc.abstractmethod
    def get_range_linear_response(self,start,stop):
        pass
    @abc.abstractmethod
    def get_range_log_response(self,start,stop):
        pass







