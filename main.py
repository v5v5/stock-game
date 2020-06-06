# link to download data
# https://www.finam.ru/profile/mirovye-indeksy/rts/export/?market=6&em=95&token=&code=RTSI&apply=0&df=4&mf=5&yf=2020&from=04.06.2020&dt=4&mt=5&yt=2020&to=04.06.2020&p=7&f=RTSI_200604_200604&e=.txt&cn=RTSI&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1
# request to download
# http://export.finam.ru/export9.out?market=6&em=95&token=03AGdBq26wCFtnU2koW48zWpyij4m149u0Dz7zTyg0rjHp6GXg7uBgyfxe3_hhMh0MXT4HiWt2uUlH5Ip4_0b1spURQRGSr5CnFWfhtmeN6pjlUdZHgDllTrkFEal3KqV70O42reEpuR5mMHUx16onlfB2E_z446U2fsVP9ZTBpXq_GF48lqDv9kUvb7ji-HSHfCVc0DzBu7weCPm_yShHMqKJXWYdzSojnMNr8UwtYDNFSzDncb7rFplfxIPtMoVk9Umu-LMc3VyWe2Adkyjr0mJ6h4Kar1KXo6gKu6k33WJB4t_zkFQ8A2hXJVdmQGruGHN9d7E-QBF2GdpQ8gz0nAH6iGqveOAu1Ol73etKtyUC2dKEo2vueuVZQ-NEapr681hJugLI25aa&code=RTSI&apply=0&df=3&mf=5&yf=2019&from=03.06.2019&dt=4&mt=5&yt=2020&to=04.06.2020&p=7&f=RTSI_190603_200604_60&e=.csv&cn=RTSI&dtf=4&tmf=4&MSOR=0&mstime=on&mstimever=1&sep=3&sep2=1&datf=1&at=1

import csv
import numpy as np
import random
import datetime

path_to_data_file = "./RTSI_190603_200604_60.csv"
max_count_of_days = 1
DATE = '<DATE>'
TIME = '<TIME>'
OPEN = '<OPEN>'
CLOSE = '<CLOSE>'

class csv_dialect(csv.excel):
    """Describe the usual properties of Excel-generated CSV files."""
    delimiter = ';'

def read_input_data(path_to_file):
    current_date = None
    previous_date = None
    with open(path_to_file, newline='') as csvfile:
        block_of_days = []
        block_of_day = []
        reader = csv.DictReader(csvfile, dialect = csv_dialect)

        for row in reader:
            current_date = row[DATE]
            if current_date is not None and previous_date != None and current_date != previous_date:
                block_of_days.append(block_of_day.copy())
                block_of_day.clear()
                if len(block_of_days) > max_count_of_days - 1:
                    return block_of_days
            previous_date = current_date

            block_of_day.append(row)
        return block_of_days

def print_input_data_of_day(input_data_of_day):
    for row in input_data_of_day:
        for _, value in row.items():
            print(value, end=' ')
        print()

def print_input_data(input_data):
    for input_data_of_day in input_data:
        print(input_data.index(input_data_of_day))
        print_input_data_of_day(input_data_of_day)
        print()

def alalysis_input_data_of_day(input_data_of_day):
    set_sequence = calculate_sets_sequence(input_data_of_day)
    maxx = max(max(set_sequence.values()))[0]
    minn = min(min(set_sequence.values()))[0]
    for key, value in set_sequence.items():
        print(key)
        for _ in range(0,10):
            value[0].append(random.uniform(minn, maxx))
            value[1].append(random.uniform(minn, maxx))
        r = np.corrcoef(value[0], value[1])
        print(r)

def alalysis_input_data_of_days(input_data):
    set_sequence = calculate_sets_sequence(input_data[0])
    for input_data_of_day in input_data:
        calculate_sets_sequence(input_data_of_day)
        pass

def calculate_sets_sequence(input_data_of_day):
    data = input_data_of_day
    l = len(data)
    count = 0
    set_sequence = {}
    for i_in_open in range(0, l):
        for i_in_close in range(i_in_open, l):
            for i_out_open in range(i_in_close + 1, l):
                for i_out_close in range(i_out_open, l):
                    set_name = (
                        f'in{data[i_in_open][TIME]}-'
                        f'in{data[i_in_close][TIME]}-'
                        f'out{data[i_out_open][TIME]}-'
                        f'out{data[i_out_close][TIME]}'
                        )
                    
                    set_sequence[set_name] = ([],[])
                    data_in = ((float(data[i_in_close][CLOSE]) - float(data[i_in_open][OPEN])) /
                        float(data[i_in_open][OPEN]))
                    data_out = ((float(data[i_out_close][CLOSE]) - float(data[i_out_open][OPEN])) /
                        float(data[i_out_open][OPEN]))
                    set_sequence[set_name][0].append(data_in)
                    set_sequence[set_name][1].append(data_out)
                    count += 1
    # print(count)
    return set_sequence

random.seed(datetime.datetime.now())
input_data = read_input_data(path_to_data_file)
alalysis_input_data_of_day(input_data[0])
# print()
# alalysis_input_data_of_day(input_data[1])

alalysis_input_data_of_days(input_data)

# print_input_data(input_data)

