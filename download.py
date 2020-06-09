# link to download data
# https://www.finam.ru/profile/mirovye-indeksy/rts/export/?market=6&em=95&token=&code=RTSI&apply=0&df=4&mf=5&yf=2020&from=04.06.2020&dt=4&mt=5&yt=2020&to=04.06.2020&p=7&f=RTSI_200604_200604&e=.txt&cn=RTSI&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1

# request to download
# http://export.finam.ru/export9.out?market=6&em=95
# &token=03AGdBq27UnRuMfA8RxUZ_rS7pRKfSHP3w4dKFhqS7GIuSFeB9qKqdWCJX4OWHzHd4jB63M1YiOQiPytrUEs7xdIfhXm6_gE5B7IpRklXVBvThHc4xZB6XL2m3eANomKbxSNZvc7FnaGikA8aK4U9QHcjJbtUyUT8as77UsEoWrBerzuYHAqWBKCaqI2Kd2Etd3peY-PlKLjDzcDp0Tx2zotm1pfGGKGDVg5MJopK1a3q-oEFVt6tKC0ZMQUGSs6LPiy_OKn2GbB6m_c2LGHoZ8SqT5mNqOu8ga1Sj6Hjc4MB4BSMTujn0nCBbdO-eEGFpmTJlJt8HoIXZWF2uCMhC4g_WtEDkfXgL4qOJK43L7sL6IAxA3hPo9FRppH2vUwdR5SvXKEQz8WxI
# &code=RTSI
# &apply=0
# &df=25&mf=4&yf=2020&from=25.05.2020
# &dt=9&mt=5&yt=2020&to=09.06.2020
# &p=4
# &f=RTSI_200525_200609_10&e=.csv
# &cn=RTSI&dtf=4&tmf=4&MSOR=0&mstime=on&mstimever=1
# &sep=3&sep2=1
# &datf=1&at=1

import wget
import urllib
import cgi        
from utils.utils import Measure

v_df = 25
v_mf = 4
v_mf1 = v_mf+1
v_yf = 2020
v_from = "{:0>2d}.{:0>2d}.{:0>4d}".format(v_df, v_mf1, v_yf)
v_dt = 9
v_mt = 5
v_mt1 = v_mt+1
v_yt = 2020
v_to = "{:0>2d}.{:0>2d}.{:0>4d}".format(v_dt, v_mt1, v_yt)
v_p = 4
v_f = "RTSI_{}{:0>2d}{:0>2d}_{}{:0>2d}{:0>2d}_{}".format(v_yf % 100, v_mf1, v_df, v_yt % 100, v_mt1, v_dt, v_p)

url = ("http://export.finam.ru/"
"export9.out?market=6&em=95"
"&token=03AGdBq27UnRuMfA8RxUZ_rS7pRKfSHP3w4dKFhqS7GIuSFeB9qKqdWCJX4OWHzHd4jB63M1YiOQiPytrUEs7xdIfhXm6_gE5B7IpRklXVBvThHc4xZB6XL2m3eANomKbxSNZvc7FnaGikA8aK4U9QHcjJbtUyUT8as77UsEoWrBerzuYHAqWBKCaqI2Kd2Etd3peY-PlKLjDzcDp0Tx2zotm1pfGGKGDVg5MJopK1a3q-oEFVt6tKC0ZMQUGSs6LPiy_OKn2GbB6m_c2LGHoZ8SqT5mNqOu8ga1Sj6Hjc4MB4BSMTujn0nCBbdO-eEGFpmTJlJt8HoIXZWF2uCMhC4g_WtEDkfXgL4qOJK43L7sL6IAxA3hPo9FRppH2vUwdR5SvXKEQz8WxI"
"&code=RTSI"
"&apply=0"
"&df={v_df}&mf={v_mf}&yf={v_yf}"
"&from={v_from}"
"&dt={v_dt}&mt={v_mt}&yt={v_yt}"
"&to={v_to}"
"&p={v_p}"
"&f={v_f}&e=.csv"
"&cn=RTSI&dtf=4&tmf=4&MSOR=0&mstime=on&mstimever=1"
"&sep=3&sep2=1"
"&datf=1&at=1")

Measure.start()
f = wget.download(url, './data.txt')
print()
print(Measure.get())
wget.download(url)

# Measure.start()
# page = urllib.request.urlopen(url)
# print(page.headers)
# content = page.read()

# f = open("company_quotes.txt", "wb")
# f.write(content)
# f.close()
# print(Measure.get())


# filename, header = urllib.request.urlretrieve(url)
# params = cgi.parse_header(header)
# print(filename)
# print(params['filename'])