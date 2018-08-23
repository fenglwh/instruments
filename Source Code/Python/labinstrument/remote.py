#!/usr/bin/python
# coding:utf-8
import datetime
import threading

__Author__ = 'Adair.l'
import pyvisa.errors
import socket
import visa
import pyvisa.constants as constants

class CommunicationUnit():
    def __init__(self,connect_string,target_type='GPIB',previous_type=None):
        self.target_type = type
        self.previous_type=previous_type
        self.connect_string = connect_string
        self.using = 0
        if self.target_type== 'GPIB':
            self.core=GPIB(self.connect_string)
        elif self.target_type=='socket server':
            self.core=SocketBasedClient()#!!! not finished
        elif self.target_type=='socket relay':
            self.core=SocketRelay()

        self.write = self.core.write
        self.read = self.core.read
        self.query = self.core.query
        self.reconnect = self.core.reconnect
        self.init_instrument = self.init_instrument

        if self.previous_type=='socket':
            self.core=SocketBasedServer()#!!! not finished





class GPIB:
    def __init__(self, connect_string, GPIB_number=0):
        if type(connect_string) is int or connect_string.isdigit() :
            self.connect_string='GPIB{}::{}::INSTR'.format(GPIB_number, connect_string)
        elif type(connect_string) is str:
            if 'TCPIP' in connect_string or 'GPIB' in connect_string:
                self.connect_string=connect_string
            elif '.' in connect_string:
                self.connect_string='TCPIP::{}'.format(connect_string)
        self.rm = visa.ResourceManager()
        self.vi_open_resource()

    def vi_open_resource(self):
        try:
            print('connecting: {}'.format(self.connect_string))
            self.instrument=self.rm.open_resource(self.connect_string)
        except Exception as e:
            print(e)


    def list_resources(self):
        return self.rm.list_resources()

    def make_connect_string(self,arg):
        rm=visa.ResourceManager()
        resources=rm.list_resources()
        prefixs=[x[:resources.index(':')] for x in resources]
        strings=[x[ resources.index(':'):resources.rindex(':')] for x in resources]
        last_words=[x[resources.rindex(':'):] for x in resources]
        if len(set(prefixs))==1:
            return "{}:{}:{}".format(prefixs[0],arg,last_words)
        else:
            for resource in resources:
                if str(arg).lower() in resource.lower():
                    return resource
                else:
                    raise Exception("We can not point out which resource you are using\nthe arg you passed is".format(arg))


    def __init__instrument(self):
       self.__init__(self.connect_string)

    def read(self):
        try:
            return self.instrument.read()
        except pyvisa.errors.VisaIOError as vi_error:
            print('vierror:{}'.format(vi_error))
            self.vi_open_resource()
            return self.read()
        except Exception as e:
            print(e)
            raise (e)

    def write(self,command):
        try:
            self.instrument.write(command)
        except pyvisa.errors.VisaIOError as vi_error:
            print('vierror:{}'.format(vi_error))
            self.vi_open_resource()
            self.write(command)
        except Exception as e:
            print (e)
            raise (e)

    def query(self,command):
        self.write(command)
        return self.read().strip()

    def IDN(self):
        return self.query('*IDN?')

    def GTL(self):
        self.write('*GTL')

    def OPC(self):
        return self.query("*OPC?")

    def reset(self):
        self.write('*RST')

    def __get_online(self):
        tmp=''
        try:
            tmp=self.IDN()
        except:
            return 0
        return 1 if tmp else 0

    is_online=property(__get_online)



class instrument():
    def __init__(self):
        self.type='GPIB'
        self.connect_string='GPIB::5:INSTR'
        self.in_use=0


class SocketBasedClient:
    def __init__(self):
        self.rd_buffer=b''
        self.wt_buffer=b''
        self.heart_beat_state='on'
        self.heart_beat_thread=None

    def heart_beat(self):
        pass

    def check_packet(self):
        pass

    def __init__instrument(self):
        pass

    def reconnect(self):
        pass

    def write(self):
        pass

    def read(self):
        pass

    def query(self):
        pass

class SocketBasedServer:

    class Client():
        def __init__(self):
            self.socket=None
            self.rd_buffer=b''
            self.wt_buffer=b''
            self.rd_lock=threading.Lock()
            self.wt_lock=threading.Lock()
            self.last_heart_beat=datetime.datetime.now()
            self.timeout=15 #second

    def __init__(self):
        self.client_num=1
        self.instruments=[]
        self.clients=[]


    def check_packet(self):
        pass

    def mainloop(self):
        last_loop_time=datetime.datetime.now()

        while 1:
            pass

            current_time=datetime.datetime.now()
            delta=current_time.timestamp()-last_loop_time.timestamp()
            if delta<0.1:
                time.sleep(delta)

    # a serials method for function and exception handling

class SocketRelay():
    def __init__(self,self_ip,self_port,target_ip,target_port,client_num):
        pass

    def mainloop(self):
        pass

    def write(self):
        pass

    def read(self):
        pass

    def query(self):
        pass


def list_resources():
    rm=visa.ResourceManager()
    return rm.list_resources()





if __name__ == '__main__':
    import time
    # a=GPIB('192.168.0.237')
    b=GPIB('GPIB0::7::INSTR')
    # c=GPIB(8)
    # print(a.IDN())
    # print(a.query('2:INT_RELAY_C_NO'))
    # print(b.IDN())
    # print(c.IDN())
    # b.write('SK 135.0')
    # c.write('SK 135.0')



