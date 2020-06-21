# data source https://www.marketwatch.com/investing/stock/ccl/financials

import requests
from lxml import html
from string import Template

## Income Statement
# get Revenue - выручка
# get Cost of Goods Sold - себестоимость продаж
# get Gross Income - валовая прибыль - нетто-выручка
# get SG&A Expense - операционные расходы
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
year_index = 6

locators_income_statement = {
    'Sales/Revenue': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[1]/td[$index]'),
    'Cost of Goods Sold': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[3]/td[$index]'),
    'Depreciation & Amortization Expense': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[5]/td[$index]'),
    'Gross Income': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[9]/td[$index]'),
    'SG&A Expense': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[1]/td[$index]'),
    'EBIT after Unusual Expense': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[7]/td[$index]'),
    'Interest Expense': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[11]/td[$index]'),
    'Pretax Income': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[15]/td[$index]'),
    'Consolidated Net Income': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[26]/td[$index]'),
    'Net Income': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[28]/td[$index]'),
    'EPS (Basic)': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[38]/td[$index]'),
    'EPS (Diluted)': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[41]/td[$index]'),
    'EBITDA': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[44]/td[$index]'),
    }

locators_balance_sheet = {
    # Assets
    'Cash & Short Term Investments': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[1]/td[$index]'),
    'Cash Only': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[2]/td[$index]'),
    'Short-Term Investments': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[3]/td[$index]'),
    'Total Accounts Receivable': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[6]/td[$index]'),
    'Accounts Receivables, Net': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[7]/td[$index]'),
    'Other Receivables': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[10]/td[$index]'),
    'Inventories': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[13]/td[$index]'),
    'Other Current Assets': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[18]/td[$index]'),
    'Total Current Assets': Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[20]/td[$index]'),
    'Net Property, Plant & Equipment': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[1]/td[$index]'),
    'Property, Plant & Equipment - Gross': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[2]/td[$index]'),
    'Accumulated Depreciation': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[7]/td[$index]'),
    'Total Investments and Advances': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[8]/td[$index]'),
    'Other Long-Term Investments': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[9]/td[$index]'),
    'Long-Term Note Receivable': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[10]/td[$index]'),
    'Intangible Assets': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[11]/td[$index]'),
    'Net Goodwill': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[12]/td[$index]'),
    'Net Other Intangibles': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[13]/td[$index]'),
    'Other Assets': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[14]/td[$index]'),
    'Tangible Other Assets': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[15]/td[$index]'),
    'Total Assets': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[16]/td[$index]'),
    # # Liabilities & Shareholders' Equity
    # 'ST Debt & Current Portion LT Debt'
    # 'Short Term Debt'
    # 'Current Portion of Long Term Debt'
    # 'Accounts Payable'
    # 'Income Tax Payable'
    # 'Other Current Liabilities'
    # 'Total Current Liabilities'
}

ticker = 'momo'

urls = {
    'Income Statement': 'https://www.marketwatch.com/investing/stock/' + ticker + '/financials',
    'Balance Sheet': 'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/balance-sheet',
    'Cash Flow Statement': 'https://www.marketwatch.com/investing/stock/' + ticker + '/financials/cash-flow'
}

url_key = 'Income Statement'
print('-'*5 + url_key + '-'*5)

page = requests.get(urls[url_key])
source_code = html.fromstring(page.content) 

for key, value in locators_income_statement.items():
    print(key, ':', source_code.xpath(value.substitute(index=year_index))[0].text)

url_key = 'Balance Sheet'
print('-'*5 + url_key + '-'*5)

page = requests.get(urls[url_key])
source_code = html.fromstring(page.content) 

for key, value in locators_balance_sheet.items():
    print(key, ':', source_code.xpath(value.substitute(index=year_index))[0].text)
