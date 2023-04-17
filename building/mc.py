import json

import requests
from bs4 import BeautifulSoup

# URL = "https://www.moneycontrol.com/india/stockpricequote/diversified/itc/ITC"
URL = "https://www.moneycontrol.com/india/stockpricequote/paintsvarnishes/bergerpaintsindia/BPI02"
response = requests.get(URL).text
soup = BeautifulSoup(response, 'html.parser')

# Top News

# Community Sentiments

# Broker Research

# Peers

# stock name
stock = soup.find('div', class_='name_left topsel_tab')
stock_name = stock.find('div', {'id': 'stockName'}, class_='inid_name').text
stonks = stock_name.split('.')
final_stock_name = stonks[0].strip()
# print(final_stock_name)

price = soup.find('div', class_='indimprice')
stock_price = price.find('div', {'id': 'nsecp'}, class_='inprice1 nsecp').text
# print(stock_price)


# percentage change
change = soup.find('div', class_='indimprice')
price_change = change.find(
    'div', {'id': 'nsechange'}, class_='pricupdn nsechange grn').text.replace(' ', '')
final_result = price_change.split("(")
change = {
    "amount_change": float(final_result[0]),
    "percent_change": float(final_result[1][:-2])
}

# market depth
order = soup.find('div', class_='div_market_depth_table')
order_table = order.find('table', id='best_5_box_table')
order_rows = order_table.findAll("tr")
order_book = {'buy': [], 'sell': []}
for i in range(2, len(order_rows) - 1):
    row_elements = order_rows[i].findAll('td')
    order_book['buy'].append(
        {'qty': row_elements[0].text, 'price': row_elements[1].text})
    order_book['sell'].append(
        {'qty': row_elements[3].text, 'price': row_elements[2].text})


# broker research
all_broker_research = []
whole_list = soup.find('div', class_='brrs_stock')
new_variable = whole_list.findChildren('div', recursive=False)
broker_cards = new_variable[0].findChildren('div', recursive=False)
for card in broker_cards:
    broker_research = {}
    date_info_div = card.findChildren('div', recursive=False)
    price_div = card.findChildren('table', recursive=False)
    report_date = date_info_div[0].text
    info_div = date_info_div[1]
    call = card.findChildren('button', recursive=False)[0].text
    name_link = info_div.findChildren('div', recursive=False)
    name = name_link[0].findChildren('h3', recursive=False)[0].text
    link = name_link[1].findChildren('a', recursive=False)[0].get('href')
    table_items = card.find_all('table')[0].find_all('td')
    reco_price = float(table_items[0].text.split('Reco Price')[1].strip())
    target_price = float(table_items[1].text.split('Target Price')[1].strip())
    broker_research["name"] = name
    broker_research["date"] = report_date
    broker_research["reco_price"] = reco_price
    broker_research["target_price"] = target_price
    broker_research["link"] = link
    all_broker_research.append(broker_research)
