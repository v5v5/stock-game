# link to download data
# https://www.finam.ru/profile/mirovye-indeksy/rts/export/?market=6&em=95&token=&code=RTSI&apply=0&df=4&mf=5&yf=2020&from=04.06.2020&dt=4&mt=5&yt=2020&to=04.06.2020&p=7&f=RTSI_200604_200604&e=.txt&cn=RTSI&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=1&sep2=1&datf=1&at=1

import csv

path_to_data_file = "./RTSI_190603_200604_60.csv"
max_count_of_days = 2
column_name_date = '<DATE>'

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
            current_date = row[column_name_date]
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

def alalysis_input_data_of_day(income_of_day):
    # print_input_data_of_day(income_of_day)
    ...

input_data = read_input_data(path_to_data_file)
alalysis_input_data_of_day(input_data[0])
print()
alalysis_input_data_of_day(input_data[1])

print_input_data(input_data)

