# data source https://www.marketwatch.com/investing/stock/ccl/financials

import requests
from lxml import html

## Income Statement
# get Revenue - выручка
# get Cost of Goods Sold - себестоимость продаж
# get Gross Income - валовая прибыль - нетто-выручка
# get EBITDA - прибыль до вычета расходов по выплате процентов, налогов, износа и начисленной амортизации
# get EBIT - прибыль до уплаты процентов и налогов - включает неоперационную (прочую) прибыль (неоперационные доходы и расходы)
# get Pretax Income - предналоговая прибыль
# get Consolidated Net Income - прибыль основного филиала в сумме с дочерними
# get Net Income - чистая прибыль

# calculate EPS

## Balance Sheet
# ...

## Cash Flow Statement
# ...

locators = {
    'Sales/Revenue': '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[1]/td[6]',
    'Cost of Goods Sold': '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[3]/td[6]',
    'Depreciation & Amortization Expense': '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[5]/td[6]',
    'Gross Income': '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[9]/td[6]',
    'SG&A Expense': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[1]/td[6]',
    'EBIT after Unusual Expense': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[7]/td[6]',
    'Interest Expense': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[11]/td[6]',
    'Pretax Income': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[15]/td[6]',
    'Consolidated Net Income': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[26]/td[6]',
    'Net Income': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[28]/td[6]',
    'EPS (Basic)': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[38]/td[6]',
    'EPS (Diluted)': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[41]/td[6]',
    'EBITDA': '//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[44]/td[6]',
    }

ticker = 'momo'
url_income_statement = "https://www.marketwatch.com/investing/stock/" + ticker + "/financials"

path_revenue = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[1]/td[6]'
path_cost_of_goods_sold = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[3]/td[6]'
path_gross_income = '//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[9]/td[6]'

page = requests.get(url_income_statement)
source_code = html.fromstring(page.content) 

# revenue = source_code.xpath(path_revenue)
# print(revenue[0].text)

# cost_of_goods_sold = source_code.xpath(path_cost_of_goods_sold)
# print(cost_of_goods_sold[0].text)

# gross_income = source_code.xpath(path_gross_income)
# print(gross_income[0].text)

for key, value in locators.items():
    print(key, ':', source_code.xpath(value)[0].text)
