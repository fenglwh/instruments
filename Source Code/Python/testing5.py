a='''
ret_val['IP_version'] = self.IP_version
        ret_val['IPV4_stack'] = self.IPV4_stack
        ret_val['IPV4_destination'] = self.IPV4_destination
        ret_val['IPV4_subnet_mask'] = self.IPV4_subnet_mask
        ret_val['IPV4_gateway'] = self.IPV4_gateway
        ret_val['IPV4_DNS'] = self.IPV4_DNS
        ret_val['IPV4_DHCP'] = self.IPV4_DHCP
        ret_val['BIPV6_prefix'] = self.IPV6_prefix
'''


for line in a.split('\n'):
    print(' = '.join([x.strip() for x in line.split('=')[::-1]]).replace('ret_val','value'))