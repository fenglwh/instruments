a='''
ret_val['freq'] = self.freq
        ret_val['channel'] = self.channel
        ret_val['tx_power'] = self.tx_power
        ret_val['pep_power'] = self.pep_power
        ret_val['operation_mode'] = self.operation_mode
        ret_val['standard'] = self.standard
        ret_val['bandwidth'] = self.bandwidth
        ret_val['beacon_interval'] = self.beacon_interval
        ret_val['senario'] = self.senario
        ret_val['mimo_path'] = self.mimo_path
        ret_val['path'] = self.path
        ret_val['input_attanuation'] = self.input_attanuation
        ret_val['output_attanuation'] = self.output_attanuation
        ret_val['rx_mix_level_offset'] = self.rx_mix_level_offset
'''


for line in a.split('\n'):
    print(' = '.join([x.strip() for x in line.split('=')[::-1]]))