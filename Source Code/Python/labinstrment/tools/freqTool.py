__Author__="Adair.l@qq.com"

import math
import re
# channel info is used to comment and list all the capability
channel_info = {
    "LTE": "",
    "WCDMA": "",
    "TDSCDMA": "",
    "CDMA2000": "",
    "GSM": "",
    "WLAN": "",

}

LTE_channel_map = {
    # channel interval=0.1MHz
    # band: DL_freq_low,DL_channel_start,DL_channel stop DL-UL freq offset,UL-DL channel offset
    "B1": {
        "dl_channel_low": 0,
        "dl_channel_high": 599,
        "ul_channel_low": 18000,
        "ul_channel_high": 18599,
        "dl_freq_low": 2110,
        "dl_freq_high": 2169.9,
        "ul_freq_low": 1920,
        "ul_freq_high": 1979.9,
        "freq2channel_dl": lambda freq: (freq - 2110) / 0.1 + 0,
        "freq2channel_ul": lambda freq: (freq - 1920) / 0.1 + 18000,
        "channel2freq_ul": lambda channel: (channel - 18000) * 0.1 + 1920,
        "channel2freq_dl": lambda channel: (channel - 0) * 0.1 + 2110,
    },
    "B2": {
        "dl_channel_low": 600,
        "dl_channel_high": 1199,
        "ul_channel_low": 18600,
        "ul_channel_high": 19199,
        "dl_freq_low": 1930,
        "dl_freq_high": 1989.9,
        "ul_freq_low": 1850,
        "ul_freq_high": 1909.9,
        "freq2channel_dl": lambda freq: (freq - 1930) / 0.1 + 600,
        "freq2channel_ul": lambda freq: (freq - 1850) / 0.1 + 18600,
        "channel2freq_ul": lambda channel: (channel - 18600) * 0.1 + 1850,
        "channel2freq_dl": lambda channel: (channel - 600) * 0.1 + 1930,
    },
    "B3": {
        "dl_channel_low": 1200,
        "dl_channel_high": 1949,
        "ul_channel_low": 19200,
        "ul_channel_high": 19949,
        "dl_freq_low": 1805,
        "dl_freq_high": 1879.9,
        "ul_freq_low": 1710,
        "ul_freq_high": 1784.9,
        "freq2channel_dl": lambda freq: (freq - 1805) / 0.1 + 1200,
        "freq2channel_ul": lambda freq: (freq - 1710) / 0.1 + 19200,
        "channel2freq_ul": lambda channel: (channel - 19200) * 0.1 + 1710,
        "channel2freq_dl": lambda channel: (channel - 1200) * 0.1 + 1805,
    },
    "B4": {
        "dl_channel_low": 1950,
        "dl_channel_high": 2399,
        "ul_channel_low": 19950,
        "ul_channel_high": 20399,
        "dl_freq_low": 2110,
        "dl_freq_high": 2154.9,
        "ul_freq_low": 1710,
        "ul_freq_high": 1754.9,
        "freq2channel_dl": lambda freq: (freq - 2110) / 0.1 + 1950,
        "freq2channel_ul": lambda freq: (freq - 1710) / 0.1 + 19950,
        "channel2freq_ul": lambda channel: (channel - 19950) * 0.1 + 1710,
        "channel2freq_dl": lambda channel: (channel - 1950) * 0.1 + 2110,
    },
    "B5": {
        "dl_channel_low": 2400,
        "dl_channel_high": 2649,
        "ul_channel_low": 20400,
        "ul_channel_high": 20649,
        "dl_freq_low": 869,
        "dl_freq_high": 893.9,
        "ul_freq_low": 824,
        "ul_freq_high": 848.9,
        "freq2channel_dl": lambda freq: (freq - 869) / 0.1 + 2400,
        "freq2channel_ul": lambda freq: (freq - 824) / 0.1 + 20400,
        "channel2freq_ul": lambda channel: (channel - 20400) * 0.1 + 824,
        "channel2freq_dl": lambda channel: (channel - 2400) * 0.1 + 869,
    },
    "B6": {
        "dl_channel_low": 2650,
        "dl_channel_high": 2749,
        "ul_channel_low": 20650,
        "ul_channel_high": 20749,
        "dl_freq_low": 875,
        "dl_freq_high": 884.9,
        "ul_freq_low": 830,
        "ul_freq_high": 839.9,
        "freq2channel_dl": lambda freq: (freq - 875) / 0.1 + 2650,
        "freq2channel_ul": lambda freq: (freq - 830) / 0.1 + 20650,
        "channel2freq_ul": lambda channel: (channel - 20650) * 0.1 + 830,
        "channel2freq_dl": lambda channel: (channel - 2650) * 0.1 + 875,
    },
    "B7": {
        "dl_channel_low": 2750,
        "dl_channel_high": 3449,
        "ul_channel_low": 20750,
        "ul_channel_high": 21449,
        "dl_freq_low": 2620,
        "dl_freq_high": 2689.9,
        "ul_freq_low": 2500,
        "ul_freq_high": 2569.9,
        "freq2channel_dl": lambda freq: (freq - 2620) / 0.1 + 2750,
        "freq2channel_ul": lambda freq: (freq - 2500) / 0.1 + 20750,
        "channel2freq_ul": lambda channel: (channel - 20750) * 0.1 + 2500,
        "channel2freq_dl": lambda channel: (channel - 2750) * 0.1 + 2620,
    },
    "B8": {
        "dl_channel_low": 3450,
        "dl_channel_high": 3799,
        "ul_channel_low": 21450,
        "ul_channel_high": 21799,
        "dl_freq_low": 925,
        "dl_freq_high": 959.9,
        "ul_freq_low": 880,
        "ul_freq_high": 914.9,
        "freq2channel_dl": lambda freq: (freq - 925) / 0.1 + 3450,
        "freq2channel_ul": lambda freq: (freq - 880) / 0.1 + 21450,
        "channel2freq_ul": lambda channel: (channel - 21450) * 0.1 + 880,
        "channel2freq_dl": lambda channel: (channel - 3450) * 0.1 + 925,
    },
    "B9": {
        "dl_channel_low": 3800,
        "dl_channel_high": 4149,
        "ul_channel_low": 21800,
        "ul_channel_high": 22149,
        "dl_freq_low": 1844.9,
        "dl_freq_high": 1879.8000000000002,
        "ul_freq_low": 1749.9,
        "ul_freq_high": 1784.8000000000002,
        "freq2channel_dl": lambda freq: (freq - 1844.9) / 0.1 + 3800,
        "freq2channel_ul": lambda freq: (freq - 1749.9) / 0.1 + 21800,
        "channel2freq_ul": lambda channel: (channel - 21800) * 0.1 + 1749.9,
        "channel2freq_dl": lambda channel: (channel - 3800) * 0.1 + 1844.9,
    },
    "B10": {
        "dl_channel_low": 4150,
        "dl_channel_high": 4749,
        "ul_channel_low": 22150,
        "ul_channel_high": 22749,
        "dl_freq_low": 2110,
        "dl_freq_high": 2169.9,
        "ul_freq_low": 1710,
        "ul_freq_high": 1769.9,
        "freq2channel_dl": lambda freq: (freq - 2110) / 0.1 + 4150,
        "freq2channel_ul": lambda freq: (freq - 1710) / 0.1 + 22150,
        "channel2freq_ul": lambda channel: (channel - 22150) * 0.1 + 1710,
        "channel2freq_dl": lambda channel: (channel - 4150) * 0.1 + 2110,
    },
    "B11": {
        "dl_channel_low": 4750,
        "dl_channel_high": 4949,
        "ul_channel_low": 22750,
        "ul_channel_high": 22949,
        "dl_freq_low": 1475.9,
        "dl_freq_high": 1495.8000000000002,
        "ul_freq_low": 1427.9,
        "ul_freq_high": 1447.8000000000002,
        "freq2channel_dl": lambda freq: (freq - 1475.9) / 0.1 + 4750,
        "freq2channel_ul": lambda freq: (freq - 1427.9) / 0.1 + 22750,
        "channel2freq_ul": lambda channel: (channel - 22750) * 0.1 + 1427.9,
        "channel2freq_dl": lambda channel: (channel - 4750) * 0.1 + 1475.9,
    },
    "B12": {
        "dl_channel_low": 5010,
        "dl_channel_high": 5179,
        "ul_channel_low": 23010,
        "ul_channel_high": 23179,
        "dl_freq_low": 729,
        "dl_freq_high": 745.9,
        "ul_freq_low": 699,
        "ul_freq_high": 715.9,
        "freq2channel_dl": lambda freq: (freq - 729) / 0.1 + 5010,
        "freq2channel_ul": lambda freq: (freq - 699) / 0.1 + 23010,
        "channel2freq_ul": lambda channel: (channel - 23010) * 0.1 + 699,
        "channel2freq_dl": lambda channel: (channel - 5010) * 0.1 + 729,
    },
    "B13": {
        "dl_channel_low": 5180,
        "dl_channel_high": 5279,
        "ul_channel_low": 23180,
        "ul_channel_high": 23279,
        "dl_freq_low": 746,
        "dl_freq_high": 755.9,
        "ul_freq_low": 777,
        "ul_freq_high": 786.9,
        "freq2channel_dl": lambda freq: (freq - 746) / 0.1 + 5180,
        "freq2channel_ul": lambda freq: (freq - 777) / 0.1 + 23180,
        "channel2freq_ul": lambda channel: (channel - 23180) * 0.1 + 777,
        "channel2freq_dl": lambda channel: (channel - 5180) * 0.1 + 746,
    },
    "B14": {
        "dl_channel_low": 5280,
        "dl_channel_high": 5379,
        "ul_channel_low": 23280,
        "ul_channel_high": 23379,
        "dl_freq_low": 758,
        "dl_freq_high": 767.9,
        "ul_freq_low": 788,
        "ul_freq_high": 797.9,
        "freq2channel_dl": lambda freq: (freq - 758) / 0.1 + 5280,
        "freq2channel_ul": lambda freq: (freq - 788) / 0.1 + 23280,
        "channel2freq_ul": lambda channel: (channel - 23280) * 0.1 + 788,
        "channel2freq_dl": lambda channel: (channel - 5280) * 0.1 + 758,
    },
    "B17": {
        "dl_channel_low": 5730,
        "dl_channel_high": 5849,
        "ul_channel_low": 23730,
        "ul_channel_high": 23849,
        "dl_freq_low": 734,
        "dl_freq_high": 745.9,
        "ul_freq_low": 704,
        "ul_freq_high": 715.9,
        "freq2channel_dl": lambda freq: (freq - 734) / 0.1 + 5730,
        "freq2channel_ul": lambda freq: (freq - 704) / 0.1 + 23730,
        "channel2freq_ul": lambda channel: (channel - 23730) * 0.1 + 704,
        "channel2freq_dl": lambda channel: (channel - 5730) * 0.1 + 734,
    },
    "B18": {
        "dl_channel_low": 5850,
        "dl_channel_high": 5999,
        "ul_channel_low": 23850,
        "ul_channel_high": 23999,
        "dl_freq_low": 860,
        "dl_freq_high": 874.9,
        "ul_freq_low": 815,
        "ul_freq_high": 829.9,
        "freq2channel_dl": lambda freq: (freq - 860) / 0.1 + 5850,
        "freq2channel_ul": lambda freq: (freq - 815) / 0.1 + 23850,
        "channel2freq_ul": lambda channel: (channel - 23850) * 0.1 + 815,
        "channel2freq_dl": lambda channel: (channel - 5850) * 0.1 + 860,
    },
    "B19": {
        "dl_channel_low": 6000,
        "dl_channel_high": 6149,
        "ul_channel_low": 24000,
        "ul_channel_high": 24149,
        "dl_freq_low": 875,
        "dl_freq_high": 889.9,
        "ul_freq_low": 830,
        "ul_freq_high": 844.9,
        "freq2channel_dl": lambda freq: (freq - 875) / 0.1 + 6000,
        "freq2channel_ul": lambda freq: (freq - 830) / 0.1 + 24000,
        "channel2freq_ul": lambda channel: (channel - 24000) * 0.1 + 830,
        "channel2freq_dl": lambda channel: (channel - 6000) * 0.1 + 875,
    },
    "B20": {
        "dl_channel_low": 6150,
        "dl_channel_high": 6449,
        "ul_channel_low": 24150,
        "ul_channel_high": 24449,
        "dl_freq_low": 791,
        "dl_freq_high": 820.9,
        "ul_freq_low": 832,
        "ul_freq_high": 861.9,
        "freq2channel_dl": lambda freq: (freq - 791) / 0.1 + 6150,
        "freq2channel_ul": lambda freq: (freq - 832) / 0.1 + 24150,
        "channel2freq_ul": lambda channel: (channel - 24150) * 0.1 + 832,
        "channel2freq_dl": lambda channel: (channel - 6150) * 0.1 + 791,
    },
    "B21": {
        "dl_channel_low": 6450,
        "dl_channel_high": 6599,
        "ul_channel_low": 24450,
        "ul_channel_high": 24599,
        "dl_freq_low": 1495.9,
        "dl_freq_high": 1510.8000000000002,
        "ul_freq_low": 1447.9,
        "ul_freq_high": 1462.8000000000002,
        "freq2channel_dl": lambda freq: (freq - 1495.9) / 0.1 + 6450,
        "freq2channel_ul": lambda freq: (freq - 1447.9) / 0.1 + 24450,
        "channel2freq_ul": lambda channel: (channel - 24450) * 0.1 + 1447.9,
        "channel2freq_dl": lambda channel: (channel - 6450) * 0.1 + 1495.9,
    },
    "B22": {
        "dl_channel_low": 6600,
        "dl_channel_high": 7399,
        "ul_channel_low": 24600,
        "ul_channel_high": 25399,
        "dl_freq_low": 3510,
        "dl_freq_high": 3589.9,
        "ul_freq_low": 3410,
        "ul_freq_high": 3489.9,
        "freq2channel_dl": lambda freq: (freq - 3510) / 0.1 + 6600,
        "freq2channel_ul": lambda freq: (freq - 3410) / 0.1 + 24600,
        "channel2freq_ul": lambda channel: (channel - 24600) * 0.1 + 3410,
        "channel2freq_dl": lambda channel: (channel - 6600) * 0.1 + 3510,
    },
    "B23": {
        "dl_channel_low": 7500,
        "dl_channel_high": 7699,
        "ul_channel_low": 25500,
        "ul_channel_high": 25699,
        "dl_freq_low": 2180,
        "dl_freq_high": 2199.9,
        "ul_freq_low": 2000,
        "ul_freq_high": 2019.9,
        "freq2channel_dl": lambda freq: (freq - 2180) / 0.1 + 7500,
        "freq2channel_ul": lambda freq: (freq - 2000) / 0.1 + 25500,
        "channel2freq_ul": lambda channel: (channel - 25500) * 0.1 + 2000,
        "channel2freq_dl": lambda channel: (channel - 7500) * 0.1 + 2180,
    },
    "B24": {
        "dl_channel_low": 7700,
        "dl_channel_high": 8039,
        "ul_channel_low": 25700,
        "ul_channel_high": 26039,
        "dl_freq_low": 1525,
        "dl_freq_high": 1558.9,
        "ul_freq_low": 1626.5,
        "ul_freq_high": 1660.4,
        "freq2channel_dl": lambda freq: (freq - 1525) / 0.1 + 7700,
        "freq2channel_ul": lambda freq: (freq - 1626.5) / 0.1 + 25700,
        "channel2freq_ul": lambda channel: (channel - 25700) * 0.1 + 1626.5,
        "channel2freq_dl": lambda channel: (channel - 7700) * 0.1 + 1525,
    },
    "B25": {
        "dl_channel_low": 8040,
        "dl_channel_high": 8689,
        "ul_channel_low": 26040,
        "ul_channel_high": 26689,
        "dl_freq_low": 1930,
        "dl_freq_high": 1994.9,
        "ul_freq_low": 1850,
        "ul_freq_high": 1914.9,
        "freq2channel_dl": lambda freq: (freq - 1930) / 0.1 + 8040,
        "freq2channel_ul": lambda freq: (freq - 1850) / 0.1 + 26040,
        "channel2freq_ul": lambda channel: (channel - 26040) * 0.1 + 1850,
        "channel2freq_dl": lambda channel: (channel - 8040) * 0.1 + 1930,
    },
    "B26": {
        "dl_channel_low": 8690,
        "dl_channel_high": 9039,
        "ul_channel_low": 26690,
        "ul_channel_high": 27039,
        "dl_freq_low": 859,
        "dl_freq_high": 893.9,
        "ul_freq_low": 814,
        "ul_freq_high": 848.9,
        "freq2channel_dl": lambda freq: (freq - 859) / 0.1 + 8690,
        "freq2channel_ul": lambda freq: (freq - 814) / 0.1 + 26690,
        "channel2freq_ul": lambda channel: (channel - 26690) * 0.1 + 814,
        "channel2freq_dl": lambda channel: (channel - 8690) * 0.1 + 859,
    },
    "B27": {
        "dl_channel_low": 9040,
        "dl_channel_high": 9209,
        "ul_channel_low": 27040,
        "ul_channel_high": 27209,
        "dl_freq_low": 852,
        "dl_freq_high": 868.9,
        "ul_freq_low": 807,
        "ul_freq_high": 823.9,
        "freq2channel_dl": lambda freq: (freq - 852) / 0.1 + 9040,
        "freq2channel_ul": lambda freq: (freq - 807) / 0.1 + 27040,
        "channel2freq_ul": lambda channel: (channel - 27040) * 0.1 + 807,
        "channel2freq_dl": lambda channel: (channel - 9040) * 0.1 + 852,
    },
    "B28": {
        "dl_channel_low": 9210,
        "dl_channel_high": 9659,
        "ul_channel_low": 27210,
        "ul_channel_high": 27659,
        "dl_freq_low": 758,
        "dl_freq_high": 802.9,
        "ul_freq_low": 703,
        "ul_freq_high": 747.9,
        "freq2channel_dl": lambda freq: (freq - 758) / 0.1 + 9210,
        "freq2channel_ul": lambda freq: (freq - 703) / 0.1 + 27210,
        "channel2freq_ul": lambda channel: (channel - 27210) * 0.1 + 703,
        "channel2freq_dl": lambda channel: (channel - 9210) * 0.1 + 758,
    },
    "B29": {
        "dl_channel_low": 9660,
        "dl_channel_high": 9769,
        "ul_channel_low": None,
        "ul_channel_high": None,
        "dl_freq_low": 717,
        "dl_freq_high": 727.9,
        "ul_freq_low": None,
        "ul_freq_high": None,
        "freq2channel_dl": lambda freq: (freq - 717) / 0.1 + 9660,
        "channel2freq_dl": lambda channel: (channel - 9660) * 0.1 + 717,
    },
    "B30": {
        "dl_channel_low": 9770,
        "dl_channel_high": 9869,
        "ul_channel_low": 27660,
        "ul_channel_high": 27759,
        "dl_freq_low": 2350,
        "dl_freq_high": 2359.9,
        "ul_freq_low": 2305,
        "ul_freq_high": 2314.9,
        "freq2channel_dl": lambda freq: (freq - 2350) / 0.1 + 9770,
        "freq2channel_ul": lambda freq: (freq - 2305) / 0.1 + 27660,
        "channel2freq_ul": lambda channel: (channel - 27660) * 0.1 + 2305,
        "channel2freq_dl": lambda channel: (channel - 9770) * 0.1 + 2350,
    },
    "B31": {
        "dl_channel_low": 9870,
        "dl_channel_high": 9919,
        "ul_channel_low": 27760,
        "ul_channel_high": 27809,
        "dl_freq_low": 462.5,
        "dl_freq_high": 467.4,
        "ul_freq_low": 452.5,
        "ul_freq_high": 457.4,
        "freq2channel_dl": lambda freq: (freq - 462.5) / 0.1 + 9870,
        "freq2channel_ul": lambda freq: (freq - 452.5) / 0.1 + 27760,
        "channel2freq_ul": lambda channel: (channel - 27760) * 0.1 + 452.5,
        "channel2freq_dl": lambda channel: (channel - 9870) * 0.1 + 462.5,
    },
    "B32": {
        "dl_channel_low": 9920,
        "dl_channel_high": 10359,
        "ul_channel_low": None,
        "ul_channel_high": None,
        "dl_freq_low": 1452,
        "dl_freq_high": 1495.9,
        "ul_freq_low": None,
        "ul_freq_high": None,
        "freq2channel_dl": lambda freq: (freq - 1452) / 0.1 + 9920,
        "channel2freq_dl": lambda channel: (channel - 9920) * 0.1 + 1452,
    },
    "B33": {
        "dl_channel_low": 36000,
        "dl_channel_high": 36199,
        "ul_channel_low": 36000,
        "ul_channel_high": 36199,
        "dl_freq_low": 1900,
        "dl_freq_high": 1919.9,
        "ul_freq_low": 1900,
        "ul_freq_high": 1919.9,
        "freq2channel_dl": lambda freq: (freq - 1900) / 0.1 + 36000,
        "freq2channel_ul": lambda freq: (freq - 1900) / 0.1 + 36000,
        "channel2freq_ul": lambda channel: (channel - 36000) * 0.1 + 1900,
        "channel2freq_dl": lambda channel: (channel - 36000) * 0.1 + 1900,
    },
    "B34": {
        "dl_channel_low": 36200,
        "dl_channel_high": 36349,
        "ul_channel_low": 36200,
        "ul_channel_high": 36349,
        "dl_freq_low": 2010,
        "dl_freq_high": 2024.9,
        "ul_freq_low": 2010,
        "ul_freq_high": 2024.9,
        "freq2channel_dl": lambda freq: (freq - 2010) / 0.1 + 36200,
        "freq2channel_ul": lambda freq: (freq - 2010) / 0.1 + 36200,
        "channel2freq_ul": lambda channel: (channel - 36200) * 0.1 + 2010,
        "channel2freq_dl": lambda channel: (channel - 36200) * 0.1 + 2010,
    },
    "B35": {
        "dl_channel_low": 36350,
        "dl_channel_high": 36949,
        "ul_channel_low": 36350,
        "ul_channel_high": 36949,
        "dl_freq_low": 1850,
        "dl_freq_high": 1909.9,
        "ul_freq_low": 1850,
        "ul_freq_high": 1909.9,
        "freq2channel_dl": lambda freq: (freq - 1850) / 0.1 + 36350,
        "freq2channel_ul": lambda freq: (freq - 1850) / 0.1 + 36350,
        "channel2freq_ul": lambda channel: (channel - 36350) * 0.1 + 1850,
        "channel2freq_dl": lambda channel: (channel - 36350) * 0.1 + 1850,
    },
    "B36": {
        "dl_channel_low": 36950,
        "dl_channel_high": 37549,
        "ul_channel_low": 36950,
        "ul_channel_high": 37549,
        "dl_freq_low": 1930,
        "dl_freq_high": 1989.9,
        "ul_freq_low": 1930,
        "ul_freq_high": 1989.9,
        "freq2channel_dl": lambda freq: (freq - 1930) / 0.1 + 36950,
        "freq2channel_ul": lambda freq: (freq - 1930) / 0.1 + 36950,
        "channel2freq_ul": lambda channel: (channel - 36950) * 0.1 + 1930,
        "channel2freq_dl": lambda channel: (channel - 36950) * 0.1 + 1930,
    },
    "B37": {
        "dl_channel_low": 37550,
        "dl_channel_high": 37749,
        "ul_channel_low": 37550,
        "ul_channel_high": 37749,
        "dl_freq_low": 1910,
        "dl_freq_high": 1929.9,
        "ul_freq_low": 1910,
        "ul_freq_high": 1929.9,
        "freq2channel_dl": lambda freq: (freq - 1910) / 0.1 + 37550,
        "freq2channel_ul": lambda freq: (freq - 1910) / 0.1 + 37550,
        "channel2freq_ul": lambda channel: (channel - 37550) * 0.1 + 1910,
        "channel2freq_dl": lambda channel: (channel - 37550) * 0.1 + 1910,
    },
    "B38": {
        "dl_channel_low": 37750,
        "dl_channel_high": 38249,
        "ul_channel_low": 37750,
        "ul_channel_high": 38249,
        "dl_freq_low": 2570,
        "dl_freq_high": 2619.9,
        "ul_freq_low": 2570,
        "ul_freq_high": 2619.9,
        "freq2channel_dl": lambda freq: (freq - 2570) / 0.1 + 37750,
        "freq2channel_ul": lambda freq: (freq - 2570) / 0.1 + 37750,
        "channel2freq_ul": lambda channel: (channel - 37750) * 0.1 + 2570,
        "channel2freq_dl": lambda channel: (channel - 37750) * 0.1 + 2570,
    },
    "B39": {
        "dl_channel_low": 38250,
        "dl_channel_high": 28649,
        "ul_channel_low": 38250,
        "ul_channel_high": 28649,
        "dl_freq_low": 1880,
        "dl_freq_high": 919.9,
        "ul_freq_low": 1880,
        "ul_freq_high": 919.9,
        "freq2channel_dl": lambda freq: (freq - 1880) / 0.1 + 38250,
        "freq2channel_ul": lambda freq: (freq - 1880) / 0.1 + 38250,
        "channel2freq_ul": lambda channel: (channel - 38250) * 0.1 + 1880,
        "channel2freq_dl": lambda channel: (channel - 38250) * 0.1 + 1880,
    },
    "B40": {
        "dl_channel_low": 38650,
        "dl_channel_high": 39649,
        "ul_channel_low": 38650,
        "ul_channel_high": 39649,
        "dl_freq_low": 2300,
        "dl_freq_high": 2399.9,
        "ul_freq_low": 2300,
        "ul_freq_high": 2399.9,
        "freq2channel_dl": lambda freq: (freq - 2300) / 0.1 + 38650,
        "freq2channel_ul": lambda freq: (freq - 2300) / 0.1 + 38650,
        "channel2freq_ul": lambda channel: (channel - 38650) * 0.1 + 2300,
        "channel2freq_dl": lambda channel: (channel - 38650) * 0.1 + 2300,
    },
    "B41": {
        "dl_channel_low": 39650,
        "dl_channel_high": 41589,
        "ul_channel_low": 39650,
        "ul_channel_high": 41589,
        "dl_freq_low": 2496,
        "dl_freq_high": 2689.9,
        "ul_freq_low": 2496,
        "ul_freq_high": 2689.9,
        "freq2channel_dl": lambda freq: (freq - 2496) / 0.1 + 39650,
        "freq2channel_ul": lambda freq: (freq - 2496) / 0.1 + 39650,
        "channel2freq_ul": lambda channel: (channel - 39650) * 0.1 + 2496,
        "channel2freq_dl": lambda channel: (channel - 39650) * 0.1 + 2496,
    },
    "B42": {
        "dl_channel_low": 41590,
        "dl_channel_high": 43589,
        "ul_channel_low": 41590,
        "ul_channel_high": 43589,
        "dl_freq_low": 3400,
        "dl_freq_high": 3599.9,
        "ul_freq_low": 3400,
        "ul_freq_high": 3599.9,
        "freq2channel_dl": lambda freq: (freq - 3400) / 0.1 + 41590,
        "freq2channel_ul": lambda freq: (freq - 3400) / 0.1 + 41590,
        "channel2freq_ul": lambda channel: (channel - 41590) * 0.1 + 3400,
        "channel2freq_dl": lambda channel: (channel - 41590) * 0.1 + 3400,
    },
    "B43": {
        "dl_channel_low": 43590,
        "dl_channel_high": 45589,
        "ul_channel_low": 43590,
        "ul_channel_high": 45589,
        "dl_freq_low": 3600,
        "dl_freq_high": 3799.9,
        "ul_freq_low": 3600,
        "ul_freq_high": 3799.9,
        "freq2channel_dl": lambda freq: (freq - 3600) / 0.1 + 43590,
        "freq2channel_ul": lambda freq: (freq - 3600) / 0.1 + 43590,
        "channel2freq_ul": lambda channel: (channel - 43590) * 0.1 + 3600,
        "channel2freq_dl": lambda channel: (channel - 43590) * 0.1 + 3600,
    },
    "B44": {
        "dl_channel_low": 45590,
        "dl_channel_high": 46589,
        "ul_channel_low": 45590,
        "ul_channel_high": 46589,
        "dl_freq_low": 703,
        "dl_freq_high": 802.9,
        "ul_freq_low": 703,
        "ul_freq_high": 802.9,
        "freq2channel_dl": lambda freq: (freq - 703) / 0.1 + 45590,
        "freq2channel_ul": lambda freq: (freq - 703) / 0.1 + 45590,
        "channel2freq_ul": lambda channel: (channel - 45590) * 0.1 + 703,
        "channel2freq_dl": lambda channel: (channel - 45590) * 0.1 + 703,
    },
    "B45": {
        "dl_channel_low": 46590,
        "dl_channel_high": 46789,
        "ul_channel_low": 46590,
        "ul_channel_high": 46789,
        "dl_freq_low": 1447,
        "dl_freq_high": 1466.9,
        "ul_freq_low": 1447,
        "ul_freq_high": 1466.9,
        "freq2channel_dl": lambda freq: (freq - 1447) / 0.1 + 46590,
        "freq2channel_ul": lambda freq: (freq - 1447) / 0.1 + 46590,
        "channel2freq_ul": lambda channel: (channel - 46590) * 0.1 + 1447,
        "channel2freq_dl": lambda channel: (channel - 46590) * 0.1 + 1447,
    },
    "B46": {
        "dl_channel_low": 46790,
        "dl_channel_high": 43589,
        "ul_channel_low": 46790,
        "ul_channel_high": 43589,
        "dl_freq_low": 5150,
        "dl_freq_high": 4829.9,
        "ul_freq_low": 5150,
        "ul_freq_high": 4829.9,
        "freq2channel_dl": lambda freq: (freq - 5150) / 0.1 + 46790,
        "freq2channel_ul": lambda freq: (freq - 5150) / 0.1 + 46790,
        "channel2freq_ul": lambda channel: (channel - 46790) * 0.1 + 5150,
        "channel2freq_dl": lambda channel: (channel - 46790) * 0.1 + 5150,
    },
    "B47": {
        "dl_channel_low": 54540,
        "dl_channel_high": 55239,
        "ul_channel_low": 54540,
        "ul_channel_high": 55239,
        "dl_freq_low": 5855,
        "dl_freq_high": 5924.9,
        "ul_freq_low": 5855,
        "ul_freq_high": 5924.9,
        "freq2channel_dl": lambda freq: (freq - 5855) / 0.1 + 54540,
        "freq2channel_ul": lambda freq: (freq - 5855) / 0.1 + 54540,
        "channel2freq_ul": lambda channel: (channel - 54540) * 0.1 + 5855,
        "channel2freq_dl": lambda channel: (channel - 54540) * 0.1 + 5855,
    },
    "B65": {
        "dl_channel_low": 65536,
        "dl_channel_high": 66435,
        "ul_channel_low": 131072,
        "ul_channel_high": 131971,
        "dl_freq_low": 2110,
        "dl_freq_high": 2199.9,
        "ul_freq_low": 1920,
        "ul_freq_high": 2009.9,
        "freq2channel_dl": lambda freq: (freq - 2110) / 0.1 + 65536,
        "freq2channel_ul": lambda freq: (freq - 1920) / 0.1 + 131072,
        "channel2freq_ul": lambda channel: (channel - 131072) * 0.1 + 1920,
        "channel2freq_dl": lambda channel: (channel - 65536) * 0.1 + 2110,
    },
    "B66": {
        "dl_channel_low": 66436,
        "dl_channel_high": 67335,
        "ul_channel_low": 131972,
        "ul_channel_high": 132871,
        "dl_freq_low": 2110,
        "dl_freq_high": 2199.9,
        "ul_freq_low": 1710,
        "ul_freq_high": 1799.9,
        "freq2channel_dl": lambda freq: (freq - 2110) / 0.1 + 66436,
        "freq2channel_ul": lambda freq: (freq - 1710) / 0.1 + 131972,
        "channel2freq_ul": lambda channel: (channel - 131972) * 0.1 + 1710,
        "channel2freq_dl": lambda channel: (channel - 66436) * 0.1 + 2110,
    },
    "B67": {
        "dl_channel_low": 67336,
        "dl_channel_high": 67335,
        "ul_channel_low": None,
        "ul_channel_high": None,
        "dl_freq_low": 738,
        "dl_freq_high": 737.9,
        "ul_freq_low": None,
        "ul_freq_high": None,
        "freq2channel_dl": lambda freq: (freq - 738) / 0.1 + 67336,
        "channel2freq_dl": lambda channel: (channel - 67336) * 0.1 + 738,
    },
    "B69": {
        "dl_channel_low": 66436,
        "dl_channel_high": 67335,
        "ul_channel_low": None,
        "ul_channel_high": None,
        "dl_freq_low": 2110,
        "dl_freq_high": 2199.9,
        "ul_freq_low": None,
        "ul_freq_high": None,
        "freq2channel_dl": lambda freq: (freq - 2110) / 0.1 + 66436,
        "channel2freq_dl": lambda channel: (channel - 66436) * 0.1 + 2110,
    },
    "B70": {
        "dl_channel_low": 68336,
        "dl_channel_high": 68585,
        "ul_channel_low": 132472,
        "ul_channel_high": 132721,
        "dl_freq_low": 1995,
        "dl_freq_high": 2019.9,
        "ul_freq_low": 1695,
        "ul_freq_high": 1719.9,
        "freq2channel_dl": lambda freq: (freq - 1995) / 0.1 + 68336,
        "freq2channel_ul": lambda freq: (freq - 1695) / 0.1 + 132472,
        "channel2freq_ul": lambda channel: (channel - 132472) * 0.1 + 1695,
        "channel2freq_dl": lambda channel: (channel - 68336) * 0.1 + 1995,
    },
    "B71": {
        "dl_channel_low": 68586,
        "dl_channel_high": 68935,
        "ul_channel_low": 133122,
        "ul_channel_high": 133471,
        "dl_freq_low": 617,
        "dl_freq_high": 651.9,
        "ul_freq_low": 663,
        "ul_freq_high": 697.9,
        "freq2channel_dl": lambda freq: (freq - 617) / 0.1 + 68586,
        "freq2channel_ul": lambda freq: (freq - 663) / 0.1 + 133122,
        "channel2freq_ul": lambda channel: (channel - 133122) * 0.1 + 663,
        "channel2freq_dl": lambda channel: (channel - 68586) * 0.1 + 617,
    },
    "B72": {
        "dl_channel_low": 68936,
        "dl_channel_high": 68985,
        "ul_channel_low": 133472,
        "ul_channel_high": 133521,
        "dl_freq_low": 461,
        "dl_freq_high": 465.9,
        "ul_freq_low": 451,
        "ul_freq_high": 455.9,
        "freq2channel_dl": lambda freq: (freq - 461) / 0.1 + 68936,
        "freq2channel_ul": lambda freq: (freq - 451) / 0.1 + 133472,
        "channel2freq_ul": lambda channel: (channel - 133472) * 0.1 + 451,
        "channel2freq_dl": lambda channel: (channel - 68936) * 0.1 + 461,
    },
    "B75": {
        "dl_channel_low": 69466,
        "dl_channel_high": 70315,
        "ul_channel_low": None,
        "ul_channel_high": None,
        "dl_freq_low": 1432,
        "dl_freq_high": 1516.9,
        "ul_freq_low": None,
        "ul_freq_high": None,
        "freq2channel_dl": lambda freq: (freq - 1432) / 0.1 + 69466,
        "channel2freq_dl": lambda channel: (channel - 69466) * 0.1 + 1432,
    },
    "B76": {
        "dl_channel_low": 70316,
        "dl_channel_high": 70365,
        "ul_channel_low": None,
        "ul_channel_high": None,
        "dl_freq_low": 1427,
        "dl_freq_high": 1431.9,
        "ul_freq_low": None,
        "ul_freq_high": None,
        "freq2channel_dl": lambda freq: (freq - 1427) / 0.1 + 70316,
        "channel2freq_dl": lambda channel: (channel - 70316) * 0.1 + 1427,
    },
}

WCDMA_channel_map = {
    # channel interval=0.2MHz
    # band: DL_freq_low,DL_channel_start,DL_channel stop DL-UL freq offset,UL-DL channel offset )
    "B1": {
        "dl_channel_low": 10562,
        "dl_channel_high": 10838,
        "ul_channel_low": 10752,
        "ul_channel_high": 11028,
        "dl_freq_low": 2112.4,
        "dl_freq_high": 2140.0,
        "ul_freq_low": 1162.4,
        "ul_freq_high": 1190.0,
        "freq2channel_dl": lambda freq: (freq - 2112.4) / 0.1 + 10562,
        "freq2channel_ul": lambda freq: (freq - 1162.4) / 0.1 + 10752,
        "channel2freq_ul": lambda channel: (channel - 10752) * 0.1 + 1162.4,
        "channel2freq_dl": lambda channel: (channel - 10562) * 0.1 + 2112.4,
    },
    "B2": {
        "dl_channel_low": 9662,
        "dl_channel_high": 9938,
        "ul_channel_low": 9742,
        "ul_channel_high": 10018,
        "dl_freq_low": 1932.4,
        "dl_freq_high": 1960.0,
        "ul_freq_low": 1532.4,
        "ul_freq_high": 1560.0,
        "freq2channel_dl": lambda freq: (freq - 1932.4) / 0.1 + 9662,
        "freq2channel_ul": lambda freq: (freq - 1532.4) / 0.1 + 9742,
        "channel2freq_ul": lambda channel: (channel - 9742) * 0.1 + 1532.4,
        "channel2freq_dl": lambda channel: (channel - 9662) * 0.1 + 1932.4,
    },
    "B3": {
        "dl_channel_low": 1162,
        "dl_channel_high": 1513,
        "ul_channel_low": 1257,
        "ul_channel_high": 1608,
        "dl_freq_low": 1807.4,
        "dl_freq_high": 1842.5,
        "ul_freq_low": 1582.4,
        "ul_freq_high": 1617.5,
        "freq2channel_dl": lambda freq: (freq - 1807.4) / 0.1 + 1162,
        "freq2channel_ul": lambda freq: (freq - 1582.4) / 0.1 + 1257,
        "channel2freq_ul": lambda channel: (channel - 1257) * 0.1 + 1582.4,
        "channel2freq_dl": lambda channel: (channel - 1162) * 0.1 + 1807.4,
    },
    "B4": {
        "dl_channel_low": 1537,
        "dl_channel_high": 1738,
        "ul_channel_low": 1937,
        "ul_channel_high": 2138,
        "dl_freq_low": 2112.4,
        "dl_freq_high": 2132.5,
        "ul_freq_low": 1887.4,
        "ul_freq_high": 1907.5,
        "freq2channel_dl": lambda freq: (freq - 2112.4) / 0.1 + 1537,
        "freq2channel_ul": lambda freq: (freq - 1887.4) / 0.1 + 1937,
        "channel2freq_ul": lambda channel: (channel - 1937) * 0.1 + 1887.4,
        "channel2freq_dl": lambda channel: (channel - 1537) * 0.1 + 2112.4,
    },
    "B5": {
        "dl_channel_low": 4357,
        "dl_channel_high": 4458,
        "ul_channel_low": 4402,
        "ul_channel_high": 4503,
        "dl_freq_low": 871.4,
        "dl_freq_high": 881.5,
        "ul_freq_low": 646.4,
        "ul_freq_high": 656.5,
        "freq2channel_dl": lambda freq: (freq - 871.4) / 0.1 + 4357,
        "freq2channel_ul": lambda freq: (freq - 646.4) / 0.1 + 4402,
        "channel2freq_ul": lambda channel: (channel - 4402) * 0.1 + 646.4,
        "channel2freq_dl": lambda channel: (channel - 4357) * 0.1 + 871.4,
    },
    "B6": {
        "dl_channel_low": 4387,
        "dl_channel_high": 4413,
        "ul_channel_low": 4432,
        "ul_channel_high": 4458,
        "dl_freq_low": 877.4,
        "dl_freq_high": 880.0,
        "ul_freq_low": 652.4,
        "ul_freq_high": 655.0,
        "freq2channel_dl": lambda freq: (freq - 877.4) / 0.1 + 4387,
        "freq2channel_ul": lambda freq: (freq - 652.4) / 0.1 + 4432,
        "channel2freq_ul": lambda channel: (channel - 4432) * 0.1 + 652.4,
        "channel2freq_dl": lambda channel: (channel - 4387) * 0.1 + 877.4,
    },
    "B7": {
        "dl_channel_low": 2237,
        "dl_channel_high": 2563,
        "ul_channel_low": 2357,
        "ul_channel_high": 2683,
        "dl_freq_low": 2622.4,
        "dl_freq_high": 2655.0,
        "ul_freq_low": 2397.4,
        "ul_freq_high": 2430.0,
        "freq2channel_dl": lambda freq: (freq - 2622.4) / 0.1 + 2237,
        "freq2channel_ul": lambda freq: (freq - 2397.4) / 0.1 + 2357,
        "channel2freq_ul": lambda channel: (channel - 2357) * 0.1 + 2397.4,
        "channel2freq_dl": lambda channel: (channel - 2237) * 0.1 + 2622.4,
    },
    "B8": {
        "dl_channel_low": 2937,
        "dl_channel_high": 3088,
        "ul_channel_low": 2982,
        "ul_channel_high": 3133,
        "dl_freq_low": 927.4,
        "dl_freq_high": 942.5,
        "ul_freq_low": 702.4,
        "ul_freq_high": 717.5,
        "freq2channel_dl": lambda freq: (freq - 927.4) / 0.1 + 2937,
        "freq2channel_ul": lambda freq: (freq - 702.4) / 0.1 + 2982,
        "channel2freq_ul": lambda channel: (channel - 2982) * 0.1 + 702.4,
        "channel2freq_dl": lambda channel: (channel - 2937) * 0.1 + 927.4,
    },
}

TDSCDMA_channel_map = {
    # channel interval=0.2MHz
    # band: DL_freq_low,DL_channel_start,DL_channel stop, DL-UL freq offset,UL-DL channel offset )
    "B34": {
        "dl_channel_low": 10054,
        "dl_channel_high": 10121,
        "ul_channel_low": 10054,
        "ul_channel_high": 10121,
        "dl_freq_low": 2010.8,
        "dl_freq_high": 2017.5,
        "ul_freq_low": 2010.8,
        "ul_freq_high": 2017.5,
        "freq2channel_dl": lambda freq: (freq - 2010.8) / 0.1 + 10054,
        "freq2channel_ul": lambda freq: (freq - 2010.8) / 0.1 + 10054,
        "channel2freq_ul": lambda channel: (channel - 10054) * 0.1 + 2010.8,
        "channel2freq_dl": lambda channel: (channel - 10054) * 0.1 + 2010.8,
    },
    "B35": {
        "dl_channel_low": 9654,
        "dl_channel_high": 9946,
        "ul_channel_low": 9654,
        "ul_channel_high": 9946,
        "dl_freq_low": 1930.8,
        "dl_freq_high": 1960.0,
        "ul_freq_low": 1930.8,
        "ul_freq_high": 1960.0,
        "freq2channel_dl": lambda freq: (freq - 1930.8) / 0.1 + 9654,
        "freq2channel_ul": lambda freq: (freq - 1930.8) / 0.1 + 9654,
        "channel2freq_ul": lambda channel: (channel - 9654) * 0.1 + 1930.8,
        "channel2freq_dl": lambda channel: (channel - 9654) * 0.1 + 1930.8,
    },
    "B36": {
        "dl_channel_low": 9554,
        "dl_channel_high": 9646,
        "ul_channel_low": 9554,
        "ul_channel_high": 9646,
        "dl_freq_low": 1910.8,
        "dl_freq_high": 1920.0,
        "ul_freq_low": 1910.8,
        "ul_freq_high": 1920.0,
        "freq2channel_dl": lambda freq: (freq - 1910.8) / 0.1 + 9554,
        "freq2channel_ul": lambda freq: (freq - 1910.8) / 0.1 + 9554,
        "channel2freq_ul": lambda channel: (channel - 9554) * 0.1 + 1910.8,
        "channel2freq_dl": lambda channel: (channel - 9554) * 0.1 + 1910.8,
    },
    "B37": {
        "dl_channel_low": 12854,
        "dl_channel_high": 13096,
        "ul_channel_low": 12854,
        "ul_channel_high": 13096,
        "dl_freq_low": 2570.8,
        "dl_freq_high": 2595.0,
        "ul_freq_low": 2570.8,
        "ul_freq_high": 2595.0,
        "freq2channel_dl": lambda freq: (freq - 2570.8) / 0.1 + 12854,
        "freq2channel_ul": lambda freq: (freq - 2570.8) / 0.1 + 12854,
        "channel2freq_ul": lambda channel: (channel - 12854) * 0.1 + 2570.8,
        "channel2freq_dl": lambda channel: (channel - 12854) * 0.1 + 2570.8,
    },
    "B38": {
        "dl_channel_low": 11504,
        "dl_channel_high": 11996,
        "ul_channel_low": 11504,
        "ul_channel_high": 11996,
        "dl_freq_low": 2300.8,
        "dl_freq_high": 2350.0,
        "ul_freq_low": 2300.8,
        "ul_freq_high": 2350.0,
        "freq2channel_dl": lambda freq: (freq - 2300.8) / 0.1 + 11504,
        "freq2channel_ul": lambda freq: (freq - 2300.8) / 0.1 + 11504,
        "channel2freq_ul": lambda channel: (channel - 11504) * 0.1 + 2300.8,
        "channel2freq_dl": lambda channel: (channel - 11504) * 0.1 + 2300.8,
    },
    "B39": {
        "dl_channel_low": 9404,
        "dl_channel_high": 9596,
        "ul_channel_low": 9404,
        "ul_channel_high": 9596,
        "dl_freq_low": 1880.8,
        "dl_freq_high": 1900.0,
        "ul_freq_low": 1880.8,
        "ul_freq_high": 1900.0,
        "freq2channel_dl": lambda freq: (freq - 1880.8) / 0.1 + 9404,
        "freq2channel_ul": lambda freq: (freq - 1880.8) / 0.1 + 9404,
        "channel2freq_ul": lambda channel: (channel - 9404) * 0.1 + 1880.8,
        "channel2freq_dl": lambda channel: (channel - 9404) * 0.1 + 1880.8,
    },
}
CDMA_channel_map = {
    "BC0": {
        "channel_range":list(range(1, 800)) + list(range(991, 1024)),
        "freq_range_dl":((825.03,848.97),(824.04,825)),
        "freq_range_ul":((870.03,893.97),(869.04,870)),
        "freq2channel_dl":lambda freq:(freq-870)/0.03 if 870.03<=freq<=893.97 else (freq-870)/0.03+1023,
        "freq2channel_ul":lambda freq:(freq-825)/0.03 if 825.03<=freq<=848.97 else (freq-825)/0.03+1023,
        "channel2freq_dl":lambda channel:0.03*channel+870 if 1<=channel<=799 else 0.03*(channel-1023)+870,
        "channel2freq_ul":lambda channel:0.03*channel+825 if 1<=channel<=799 else 0.03*(channel-1023)+825,
    },
    "BC1": {
        "channel_range":list(range(1,1200)),
        "freq_range_dl":((1930.05,1989.95)),
        "freq_range_ul":((1850.05,1909.95)),
        "freq2channel_dl":lambda freq:(freq-1930)/0.05,
        "freq2channel_ul":lambda freq:(freq-1850)/0.05,
        "channel2freq_dl":lambda channel:0.05*channel+1930,
        "channel2freq_ul":lambda channel:0.05*channel+1850,
    },
    "BC2": {
        "channel_range":list(range(0, 1001))+list(range(1329, 2048)),
        "freq_range_dl":((934.9875,959.9875),(917.0125,934.9625)),
        "freq_range_ul":((889.9875,914.9875),(872.0125,889.9625)),
        "freq2channel_dl":lambda freq:(freq-934.9875)/0.025 if 934.9875<=freq<=959.9875 else (freq-916.9875)/0.025+1328,
        "freq2channel_ul":lambda freq:(freq-889.9875)/0.025 if 889.9875<=freq<=914.9875 else (freq-871.9875)/0.025+1328,
        "channel2freq_dl":lambda channel:0.03*channel+870,
        "channel2freq_ul":lambda channel:0.03*channel+825,
    },
    #!!!
"BC": {
        "channel_range":list(range(1, 800)),
        "freq_range_dl":(()),
        "freq_range_ul":(()),
        "freq2channel_dl":lambda freq:None,
        "freq2channel_ul":lambda freq:None,
        "channel2freq_dl":lambda channel:None,
        "channel2freq_ul":lambda channel:None,
    },
}

GSM_channel_map = {
    "850": {
        "channel_range":list(range(128, 252)),
        "freq_range_dl":1,
        "freq_range_ul":1,
        "freq2channel_dl": lambda f:f/824.2/0.2+128,
        "freq2channel_ul": lambda f:f/824.2/0.2+128,
        "channel2freq_dl": lambda n:824.2 + 0.2*(n-128),
        "channel2freq_ul": lambda n:824.2 + 0.2*(n-128),
    },
    "900": list(range(0, 125)) + list(range(975, 1024)),
    "1800": list(range(512, 886)),
    "1900": list(range(512, 811)),
}
WIFI_channel_map = {
    # band: DL_freq_low,DL_channel_start,DL_channel stop, DL-UL freq offset,UL-DL channel offset )
    "2G": (2412, 1, 15, 0, 0),
    "5G": (5100, 20, 170, 0, 0),
}

predefined_channel = {
    # !!!
    "LTE": {},
    "WCDMA": {},
    "TDSCDMA": {},
    "CDMA2000": {},
    "GSM": {},
    "WIFI": {},
}


# (Band , channel dl, channel ul, freq dl, freq ul)
def freq2channel(tech, band, freq_dl=0,freq_ul=0) :
    # band: DL_freq_low,DL_channel_start,DL_channel stop, DL-UL freq offset,UL-DL channel offset
    def LTE_channel(band,freq_dl=0,freq_ul=0):
        ret_val=["","","","",""]
        ret_val[0]=band
        if freq_dl:
            ret_val[3]=round(freq_dl,11)
            ret_val[4]=round(freq_dl-(LTE_channel_map[band]["dl_freq_low"]-LTE_channel_map[band]["ul_freq_low"]),11)
            ret_val[1]=int(LTE_channel_map[band]["freq2channel_dl"](freq_dl))
            ret_val[2]=int(ret_val[1]-(LTE_channel_map[band]["dl_channel_low"]-LTE_channel_map[band]["ul_channel_low"]))
        elif freq_ul:
            ret_val[4] = round(freq_ul,11)
            ret_val[3] = round(freq_ul+((LTE_channel_map[band]["dl_freq_low"]-LTE_channel_map[band]["ul_freq_low"])),11)
            ret_val[2] = int(LTE_channel_map[band]["freq2channel_ul"](freq_ul))
            ret_val[1] = int(ret_val[2] + (
                        LTE_channel_map[band]["dl_channel_low"] - LTE_channel_map[band]["ul_channel_low"]))
        return ret_val

    def WCDMA_channel(tech, band, freq_dl=0,freq_ul=0):
        ret_val = ["", "", "", "", ""]
        ret_val[0] = band
        if freq_dl:
            ret_val[3] = round(freq_dl,11)
            ret_val[4] = round(freq_dl - (WCDMA_channel_map[band]["dl_freq_low"] - WCDMA_channel_map[band]["ul_freq_low"]),11)
            ret_val[1] = int(WCDMA_channel_map[band]["freq2channel_dl"](freq_dl))
            ret_val[2] = int(
                ret_val[1] - (WCDMA_channel_map[band]["dl_channel_low"] - WCDMA_channel_map[band]["ul_channel_low"]))
        elif freq_ul:
            ret_val[4] = round(freq_ul,11)
            ret_val[3] = round(freq_ul + ((WCDMA_channel_map[band]["dl_freq_low"] - WCDMA_channel_map[band]["ul_freq_low"])),11)
            ret_val[2] = int(WCDMA_channel_map[band]["freq2channel_ul"](freq_ul))
            ret_val[1] = int(ret_val[2] + (
                WCDMA_channel_map[band]["dl_channel_low"] - WCDMA_channel_map[band]["ul_channel_low"]))
        return ret_val

    def TDSCDMA_channel(tech, band, freq_dl=0,freq_ul=0):
        ret_val = ["", "", "", "", ""]
        ret_val[0] = band
        if freq_dl:
            ret_val[3] = round(freq_dl,11)
            ret_val[4] = round(freq_dl - (TDSCDMA_channel_map[band]["dl_freq_low"] - TDSCDMA_channel_map[band]["ul_freq_low"]),11)
            ret_val[1] = int(TDSCDMA_channel_map[band]["freq2channel_dl"](freq_dl))
            ret_val[2] = int(
                ret_val[1] - (TDSCDMA_channel_map[band]["dl_channel_low"] - TDSCDMA_channel_map[band]["ul_channel_low"]))
        elif freq_ul:
            ret_val[4] = round(freq_ul,11)
            ret_val[3] = round(freq_ul + ((TDSCDMA_channel_map[band]["dl_freq_low"] - TDSCDMA_channel_map[band]["ul_freq_low"])),11)
            ret_val[2] = int(TDSCDMA_channel_map[band]["freq2channel_ul"](freq_ul))
            ret_val[1] = int(ret_val[2] + (
                TDSCDMA_channel_map[band]["dl_channel_low"] - TDSCDMA_channel_map[band]["ul_channel_low"]))
        return ret_val

    def CDMA_channel(tech, band, freq_dl=0,freq_ul=0):
        # ret_val = ["", "", "", "", ""]
        # ret_val[0] = band
        # if freq_dl:
        #     ret_val[3] = freq_dl
        #     ret_val[4] = freq_dl - (CDMA_channel_map[band]["dl_freq_low"] - CDMA_channel_map[band]["ul_freq_low"])
        #     ret_val[1] = int(CDMA_channel_map[band]["freq2channel_dl"](freq_dl))
        #     ret_val[2] = int(
        #         ret_val[1] - (CDMA_channel_map[band]["dl_channel_low"] - CDMA_channel_map[band]["ul_channel_low"]))
        # elif freq_ul:
        #     ret_val[4] = freq_ul
        #     ret_val[3] = freq_ul + ((CDMA_channel_map[band]["dl_freq_low"] - CDMA_channel_map[band]["ul_freq_low"]))
        #     ret_val[2] = int(CDMA_channel_map[band]["freq2channel_ul"](freq_ul))
        #     ret_val[1] = int(ret_val[2] + (
        #         CDMA_channel_map[band]["dl_channel_low"] - CDMA_channel_map[band]["ul_channel_low"]))
        # return ret_val
        pass

    def GSM_channel(tech, band, freq_dl=0,freq_ul=0):
        ret_val = ["", "", "", "", ""]
        ret_val[0] = band
        if freq_dl:
            ret_val[3] = round(freq_dl, 11)
            ret_val[4] = round(freq_dl, 11)
            ret_val[1] = int(TDSCDMA_channel_map[band]["freq2channel_dl"](freq_dl))
            ret_val[2] = int(TDSCDMA_channel_map[band]["freq2channel_dl"](freq_dl))
        elif freq_ul:
            ret_val[4] = round(freq_ul, 11)
            ret_val[3] = round(freq_ul, 11)
            ret_val[2] = int(TDSCDMA_channel_map[band]["freq2channel_ul"](freq_ul))
            ret_val[1] = int(TDSCDMA_channel_map[band]["freq2channel_ul"](freq_ul))
        return ret_val

    def WIFI_channel(tech, band, freq_dl=0,freq_ul=0):
        ret_val = ["", "", "", "", ""]
        ret_val[0] = band
        if freq_dl:
            ret_val[3] = freq_dl
            ret_val[4] = freq_dl - (LTE_channel_map[band]["dl_freq_low"] - LTE_channel_map[band]["ul_freq_low"])
            ret_val[1] = int(LTE_channel_map[band]["freq2channel_dl"](freq_dl))
            ret_val[2] = int(
                ret_val[1] - (LTE_channel_map[band]["dl_channel_low"] - LTE_channel_map[band]["ul_channel_low"]))
        elif freq_ul:
            ret_val[4] = freq_ul
            ret_val[3] = freq_ul + ((LTE_channel_map[band]["dl_freq_low"] - LTE_channel_map[band]["ul_freq_low"]))
            ret_val[2] = int(LTE_channel_map[band]["freq2channel_ul"](freq_ul))
            ret_val[1] = int(ret_val[2] + (
                LTE_channel_map[band]["dl_channel_low"] - LTE_channel_map[band]["ul_channel_low"]))
        return ret_val
    # process all the parameters passed by.
    tech=tech.upper()
    freq_ul=float(freq_ul)
    freq_dl=float(freq_dl)
    if tech.upper()=="LTE":
        if type(band) is str:
            band = band.upper()
            if re.match("^B\d+", band):
                band = band
            elif re.match("^BAND(\d+)", band):
                band = "B{}".format(re.match("^BAND(\d+)", band).group(1))
            elif re.match("^\d+$", band):
                band = "B{}".format(band)
        elif type(band) is int or type(band) is float:
            band = "B{}".format(band)
        return LTE_channel(band,freq_dl,freq_ul)
    if tech.upper()=="WCDMA":
        return WCDMA_channel(band,freq_dl,freq_ul)
    if tech.upper()=="TDSCDMA":
        return TDSCDMA_channel(band,freq_dl,freq_ul)
    if tech.upper()=="CDMA":
        return CDMA_channel(band,freq_dl,freq_ul)
    if tech.upper()=="GSM":
        band = band.upper()
        if type(band) is str:
            if re.match("^GSM(\d+)", band):
                band = re.match("^GSM(\d+)", band).group(1)
            elif "DCS"in band:
                band="1800"
            elif "PCS"in band:
                band="1900"
            elif re.match("^\d+$", band):
                band = band
        elif type(band) is int or type(band) is float:
            band=str(int(band))
        return GSM_channel(band,freq_dl,freq_ul)
    if tech.upper()=="WIFI":
        return WIFI_channel(band,freq_dl,freq_ul)

def channel2freq(tech, band, channel_dl=0,channel_ul=0):
    def LTE_freq(tech: str, band: str, freq: str) -> dict:
        ret_val = ["", "", "", "", ""]
        ret_val[0] = band
        if channel_dl:
            ret_val[1] = round(channel_dl, 11)
            ret_val[2] = round(channel_dl - (LTE_channel_map[band]["dl_channel_low"] - LTE_channel_map[band]["ul_freq_low"]),
                               11)
            ret_val[3] = int(LTE_channel_map[band]["channel2freq_dl"](channel_dl))
            ret_val[4] = int(
                ret_val[1] - (LTE_channel_map[band]["dl_freq_low"] - LTE_channel_map[band]["ul_freq_low"]))
        elif channel_ul:
            ret_val[2] = round(channel_ul, 11)
            ret_val[1] = round(
                channel_ul + ((LTE_channel_map[band]["dl_channel_low"] - LTE_channel_map[band]["ul_channel_low"])), 11)
            ret_val[4] = int(LTE_channel_map[band]["channel2freq_ul"](channel_ul))
            ret_val[3] = int(ret_val[2] + (
                LTE_channel_map[band]["dl_freq_low"] - LTE_channel_map[band]["ul_freq_low"]))
        return ret_val

    def WCDMA_freq(tech, band, channel_dl=0,channel_ul=0) -> dict:
        pass

    def TDSCDMA_freq(tech, band, channel_dl=0,channel_ul=0) -> dict:
        pass

    def CDMA_freq(tech, band, channel_dl=0,channel_ul=0) -> dict:
        pass

    def GSM_freq(tech, band, channel_dl=0,channel_ul=0) -> dict:
        pass

    def WIFI_freq(tech, band, channel_dl=0,channel_ul=0) -> dict:
        pass

    tech = tech.upper()
    freq_ul = float(channel_ul)
    freq_dl = float(channel_dl)
    if tech.upper() == "LTE":
        if type(band) is str:
            band = band.upper()
            if re.match("^B\d+", band):
                band = band
            elif re.match("^BAND(\d+)", band):
                band = "B{}".format(re.match("^BAND(\d+)", band).group(1))
            elif re.match("^\d+$", band):
                band = "B{}".format(band)
        elif type(band) is int or type(band) is float:
            band = "B{}".format(band)
        return LTE_freq(band, freq_dl, freq_ul)
    if tech.upper() == "WCDMA":
        return WCDMA_freq(band, freq_dl, freq_ul)
    if tech.upper() == "TDSCDMA":
        return TDSCDMA_freq(band, freq_dl, freq_ul)
    if tech.upper() == "CDMA":
        return CDMA_freq(band, freq_dl, freq_ul)
    if tech.upper() == "GSM":
        band = band.upper()
        if type(band) is str:
            if re.match("^GSM(\d+)", band):
                band = re.match("^GSM(\d+)", band).group(1)
            elif "DCS" in band:
                band = "1800"
            elif "PCS" in band:
                band = "1900"
            elif re.match("^\d+$", band):
                band = band
        elif type(band) is int or type(band) is float:
            band = str(int(band))
        return GSM_freq(band, freq_dl, freq_ul)
    if tech.upper() == "WIFI":
        return WIFI_freq(band, freq_dl, freq_ul)



def get_LTE_offset_by_RB_setting(bandwidth,rb_start,rb_stop):
    pass

def get_tech_and_channels_by_freq(freq):
    pass

if __name__ == '__main__':
    print(freq2channel("LTE","1",2110))
    print(channel2freq("LTE",1,300))
    print((lambda n:824.2 + 0.2*(n-128))(128))
    print((lambda n:824.2 + 0.2*(n-128))(251))