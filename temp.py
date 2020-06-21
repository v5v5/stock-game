import requests
from lxml import html
from string import Template

path_to_parameters = "//td[@class='rowTitle']"
path_to_value = Template("""//td[@class='rowTitle' and text()="$params"]/../td[1<position() and position()<7]""")

ticker = 'momo'

urls = {
    'https://www.marketwatch.com/investing/stock/' + ticker + '/financials',
    'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/balance-sheet',
    'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/cash-flow'
}

for url in urls:
    print('*'*80)
    page = requests.get(url)
    source_code = html.fromstring(page.content)

    parameters = source_code.xpath(path_to_parameters)
    for i, p in enumerate(parameters):
        # parameter_name = p.text_content().strip()
        parameter_name = p.text_content()
        print(parameter_name)
        path_to_values = path_to_value.substitute(params=parameter_name)
        
        values = source_code.xpath(path_to_values)
        for value in values:
            print(' '*5, value.text_content())