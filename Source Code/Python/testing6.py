import visa

rs=visa.ResourceManager()
instrument=rs.open_resource("GPIB::20::INSTR")
print('init ok')
instrument.write('CONF:WLAN:SIGN1:CONN:CCODe:CCC?')
print(instrument.read())
instrument.write('*GTL')