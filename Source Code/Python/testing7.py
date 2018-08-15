from labinstrument.SS.CMW500.CMW500_WIFI.CMW500_WIFI import CMW_WIFI
from labinstrument.turntable.ETS2090.ETS2090 import ETS2090

if __name__ == '__main__':
    instrument=ETS2090('GPIB0::8::INSTR','GPIB::7::INSTR')
    # for theta in range(0,180,15):
    #     print('theta:{}'.format(theta))
    #     instrument.theta.seek(theta)
    #     for phi in range(0,360,15):
    #         print('phi:{}'.format(phi))
    #         instrument.phi.seek(phi)
    instrument.theta.seek(90)
    instrument.phi.seek(180)