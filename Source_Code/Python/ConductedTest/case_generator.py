import json
from labinstrument.SS.CMW500.CMW500_WIFI.CMW500_WIFI import *

if __name__ == '__main__':
    new_config_name='emm'
    new_config=CMW_WIFI(17).get_parameters()
    config=json.load(open('config.txt'))
    config[new_config_name]=new_config
    json.dump(config,open('config.txt','w'))