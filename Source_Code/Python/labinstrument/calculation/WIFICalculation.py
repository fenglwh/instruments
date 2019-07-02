import math

def WIFI_channel2freq(channel):
    if channel not in list(range(1,167)):
        raise Exception('the channel:{} is not a valid frequency'.format(channel))
    if channel < 35:
        return 2407+ 5* channel
    else:
        return 5000+5*channel

def WIFI_freq2channel(freq):
    if freq not in list(range(2412,2463,5))+list(range(5180,5786,5)):
        raise Exception('the freq:{} is not a valid frequency'.format(freq))
    if freq<5000:
        return (freq-2407)//5
    else:
        return (freq-5000)//5

if __name__ == "__main__":
    print(WIFI_channel2freq(36))
    print(WIFI_channel2freq(52))
    print(WIFI_channel2freq(60))
    print(WIFI_channel2freq(120))
    print(WIFI_channel2freq(157))
    print()
    print(WIFI_freq2channel(2412))
    print(WIFI_freq2channel(5180))
    print(WIFI_freq2channel(5600))
    print(WIFI_freq2channel(5785))