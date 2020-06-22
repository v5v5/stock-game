import requests
from lxml import html

path_to_parameters = "//td[@class='rowTitle']"
subpath_to_value = "./../td[1<position() and position()<7]"

ticker = 'momo'

urls = {
    'Income Statement': 'https://www.marketwatch.com/investing/stock/' + ticker + '/financials',
    'Balance Sheet': 'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/balance-sheet',
    'Cash Flow Statement': 'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/cash-flow'
}

def get_list_params():
    for key, url in urls.items():
        print(" "*80)
        print(key)
        print(" "*80)
        page = requests.get(url)
        source_code = html.fromstring(page.content)

        parameters = source_code.xpath(path_to_parameters)
        for p in parameters:
            parameter_name = p.text_content().strip()
            print(parameter_name)

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

def get_list_values():
    valueCells = {}
    for _, url in urls.items():
        print('*'*80)
        page = requests.get(url)
        source_code = html.fromstring(page.content)

        parameters = source_code.xpath(path_to_parameters)
        for _, p in enumerate(parameters):
            parameter_name = p.text_content().strip()
            print(parameter_name)
            valueCells[parameter_name] = []

            values = p.xpath(subpath_to_value)
            for value in values:
                v = value.text_content()
                v = format_value(v)
                print(' '*5, v)
                valueCells[parameter_name].append(v)
    return valueCells

# get_list_values()