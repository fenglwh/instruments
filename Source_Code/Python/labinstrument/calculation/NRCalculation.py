import math


NRchannelmapping={
    #this should be band : channel_dl_start,channel_dl_end, channel_ul_start, channel_ul_stop, freq_dl_start, freq_dl_stop, freq_ul_start, freq_ul_stop, 
    # delta_channel, delta_freq, raster_supported, basic_channel
    '':['','','','','','',''],
}

# step = channelraster/delta_global

def NRchannel2freq(channel):
    if channel<600000:
        delta_global = 0.005
        freq_offset = 0
        channel_offset = 0
    if 600000<=channel<2016667:
        delta_global = 0.015
        freq_offset = 3000
        channel_offset = 600000
    if 2016667<=channel<3279166:
        delta_global = 0.06
        freq_offset = 2450.08
        channel_offset = 2016667
    return freq_offset + delta_global*(channel-channel_offset)

def NRfreq2channel(freq):
    if freq<3000:
        delta_global = 0.005
        freq_offset = 0
        channel_offset = 0
    if 3000<=freq<24250:
        delta_global = 0.015
        freq_offset = 3000
        channel_offset = 600000
    if 24250<=freq<100000:
        delta_global = 0.06
        freq_offset = 2450.08
        channel_offset = 2016667
    return (freq-freq_offset)/delta_global+channel_offset

def get_NR_band_by_channel(channel):
    pass

def get_NR_band_by_freq(channel):
    pass

def get_NR_information_by_band(band):
    pass

def get_valid_channels(band,raster):
    pass

def get_BMT_channel(band,raster):
    pass

def get_LMH_channel(band,raster):
    pass

def get_valid_freqs(band, raster):
    pass

def get_BMT_freq(band, raster):
    pass

def get_LMH_freq(band, raster):
    pass



if __name__ == "__main__":
    print(NRfreq2channel(2496))
    print(NRchannel2freq(499200))

