# link to download data
# https://www.finam.ru/profile/mirovye-indeksy/rts/export/?market=6&em=95&token=&code=RTSI&apply=0&df=4&mf=5&yf=2020&from=04.06.2020&dt=4&mt=5&yt=2020&to=04.06.2020&p=7&f=RTSI_200604_200604&e=.txt&cn=RTSI&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1
# request to download
# http://export.finam.ru/export9.out?market=6&em=95&token=03AGdBq26wCFtnU2koW48zWpyij4m149u0Dz7zTyg0rjHp6GXg7uBgyfxe3_hhMh0MXT4HiWt2uUlH5Ip4_0b1spURQRGSr5CnFWfhtmeN6pjlUdZHgDllTrkFEal3KqV70O42reEpuR5mMHUx16onlfB2E_z446U2fsVP9ZTBpXq_GF48lqDv9kUvb7ji-HSHfCVc0DzBu7weCPm_yShHMqKJXWYdzSojnMNr8UwtYDNFSzDncb7rFplfxIPtMoVk9Umu-LMc3VyWe2Adkyjr0mJ6h4Kar1KXo6gKu6k33WJB4t_zkFQ8A2hXJVdmQGruGHN9d7E-QBF2GdpQ8gz0nAH6iGqveOAu1Ol73etKtyUC2dKEo2vueuVZQ-NEapr681hJugLI25aa&code=RTSI&apply=0&df=3&mf=5&yf=2019&from=03.06.2019&dt=4&mt=5&yt=2020&to=04.06.2020&p=7&f=RTSI_190603_200604_60&e=.csv&cn=RTSI&dtf=4&tmf=4&MSOR=0&mstime=on&mstimever=1&sep=3&sep2=1&datf=1&at=1

import csv
import numpy as np
import random
import datetime
import time
from typing import Dict, List

# path_to_data_file = "./RTSI_190603_200604_60.csv"
# path_to_data_file = "./RTSI_190603_200604_15.csv"
# path_to_data_file = "./RTSI_180603_200604_15.csv"
# path_to_data_file = "./RTSI_190603_200604_10.csv"
# path_to_data_file = "./RTSI_190603_200604_05.csv"
# path_to_data_file = "./RTSI_200522_200605_01.csv"
# path_to_data_file = "./RTSI_200601_200605_05.csv"
# path_to_data_file = "./RTSI_200522_200605_10.csv"
path_to_data_file = "./RTSI_200504_200612_10.csv"

max_count_of_days = 600
DATE = '<DATE>'
TIME = '<TIME>'
OPEN = '<OPEN>'
CLOSE = '<CLOSE>'

class csv_dialect(csv.excel):
    """Describe the usual properties of Excel-generated CSV files."""
    delimiter = ';'

def read_input_data(path_to_file) -> List[List[Dict[str, str]]]:
    print("reading file data is started...")
    current_date: str = None
    previous_date: str = None
    with open(path_to_file, newline='') as csvfile:
        block_of_days: List[List[Dict]]  = []
        block_of_day: List[Dict] = []
        reader = csv.DictReader(csvfile, dialect = csv_dialect)

        for row in reader:
            current_date = row[DATE]
            if current_date is not None and previous_date != None and current_date != previous_date:
                block_of_days.append(block_of_day.copy())
                block_of_day.clear()
                print(f"{len(block_of_days)} blocks is read")
                if len(block_of_days) > max_count_of_days - 1:
                    break
            previous_date = current_date

            block_of_day.append(row)
        else:
            block_of_days.append(block_of_day.copy())
            block_of_day.clear()
            print(f"{len(block_of_days)} blocks is read")
        print("reading file data is finished\r")
        return block_of_days

class CalculationData:
    # self.data_in: t.List[float] = []
    # self.data_out: t.List[float] = []
    # self.corrcoef: float = 0
    def __init__(self):
        self.data_in = []
        self.data_out = []
        self.corrcoef = 0

def analysis_input_data_of_day(data_of_day: List[Dict[str, str]], 
set_sequence: Dict[str, CalculationData]) -> Dict[str, CalculationData]:
    data = data_of_day
    l = len(data)
    for i_in_open in range(0, l):
        for i_in_close in range(i_in_open, l):
            for i_out_open in range(i_in_close + 1, l):
                for i_out_close in range(i_out_open, l):
                    set_name = (
                        f'inopen{data[i_in_open][TIME]}-'
                        f'inclose{data[i_in_close][TIME]}-'
                        f'outopen{data[i_out_open][TIME]}-'
                        f'outclose{data[i_out_close][TIME]}'
                        )
                    
                    if set_name not in set_sequence:
                        set_sequence[set_name] = CalculationData()
                    data_in = ((float(data[i_in_close][CLOSE]) - float(data[i_in_open][OPEN])) /
                        float(data[i_in_open][OPEN]))
                    data_out = ((float(data[i_out_close][CLOSE]) - float(data[i_out_open][OPEN])) /
                        float(data[i_out_open][OPEN]))
                    set_sequence[set_name].data_in.append(data_in)
                    set_sequence[set_name].data_out.append(data_out)
    return set_sequence

def analysis_input_data_of_days(input_data: List[List[Dict[str, str]]]) -> Dict[str, CalculationData]:
    print('data process is started...')
    count_calculation_days = 0
    set_sequence: Dict[str, CalculationData] = {}
    for input_data_of_day in input_data:
        # set_sequence = analysis_input_data_of_day(input_data_of_day, set_sequence)
        analysis_input_data_of_day(input_data_of_day, set_sequence)
        count_calculation_days += 1
        print('count calculated days ', count_calculation_days)
    print('data process is finished\r')

    print('correlation calculate is started...')
    for _, value in set_sequence.items():
        data_in = value.data_in
        data_out = value.data_out
        r = np.corrcoef(data_in, data_out)
        value.corrcoef = r
    print('correlation calculate is finished...\r')

    return set_sequence

# start of data process
start = time.time()

random.seed(datetime.datetime.now())
input_data = read_input_data(path_to_data_file)

# d = alalysis_input_data_of_day(input_data[0])
# for key, value in d.items():
#     print(key)
#     print(value.data_in)
#     print(value.data_out)
#     print(value.corrcoef)
# raise SystemExit
# d = alalysis_input_data_of_day(input_data[1])
# for key, value in d.items():
#     print(key)
#     print(value.data_in)
#     print(value.data_out)
#     print(value.corrcoef)
# raise SystemExit

set_sequence = analysis_input_data_of_days(input_data)
corrcoefs = tuple(map(lambda v: v.corrcoef[0,1], set_sequence.values()))
maxx = max(corrcoefs)
print('max:', maxx)
key_maxx = {k for k,v in set_sequence.items() if float(v.corrcoef[0,1]) == maxx}
# key_maxx = list(filter(lambda item: item[1].corrcoef[0,1] == maxx, set_sequence.items()))
print(f'trade range:{key_maxx}')
minn = min(corrcoefs)
print('min:', minn)
# key_minn = list(filter(lambda item: item[1].corrcoef[0,1] == minn, set_sequence.items()))
key_minn = {k for k,v in set_sequence.items() if float(v.corrcoef[0,1]) == minn}
print(f'trade range:{key_minn}\r', )

# end of data process
end = time.time()
print("calculation time:", end - start)
