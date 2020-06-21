import requests
from lxml import html
from string import Template
import matplotlib.pyplot as plt
from typing import List
import numpy as np
import math
import datetime

path_to_parameters = "//td[@class='rowTitle']"
path_to_value = Template("""//td[@class='rowTitle' and text()="$params"]/../td[1<position() and position()<7]""")

ticker = 'momo'

urls = {
    'https://www.marketwatch.com/investing/stock/' + ticker + '/financials',
    'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/balance-sheet',
    'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/cash-flow'
}

def format_value(value: str) -> float:
    value = value.replace('M', '000000')
    value = value.replace('B', '000000000')
    value = value.replace(',', '')
    value = value.replace('.', '')
    value = value.replace('%', '')
    value = value.replace('(', '-')
    value = value.replace(')', '')
    f = None
    try:
        f = float(value)
    except Exception:
        pass
    return f

valueCells = {}

for url in urls:
    print('*'*80)
    page = requests.get(url)
    source_code = html.fromstring(page.content)

    parameters = source_code.xpath(path_to_parameters)
    for i, p in enumerate(parameters):
        # parameter_name = p.text_content().strip()
        parameter_name = p.text_content()
        print(parameter_name)
        valueCells[parameter_name] = []
        path_to_values = path_to_value.substitute(params=parameter_name)
        
        values = source_code.xpath(path_to_values)
        for value in values:
            v = value.text_content()
            v = format_value(v)
            print(' '*5, v)
            valueCells[parameter_name].append(v)

now = datetime.datetime.now()
graph_name = " Total Shareholders' Equity"
y = valueCells[graph_name]
x = np.arange(now.year - len(y), now.year, 1)
plt.plot(x, y) 
plt.xlabel('Years') 
plt.xticks(range(min(x), math.ceil(max(x))+1))
plt.ylabel('Values') 
plt.title(graph_name) 
plt.show() 