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

#stock name
stock = soup.find('div', class_='name_left topsel_tab')
stock_name = stock.find('div', {'id': 'stockName'}, class_='inid_name').text
stonks = stock_name.split('.')
final_stock_name = stonks[0]

# print(final_stock_name)
price = soup.find('div', class_='indimprice')
stock_price = price.find('div', {'id': 'nsecp'}, class_='inprice1 nsecp').text
# print(stock_price)

#percentage change
change = soup.find('div', class_='indimprice')
price_change = change.find(
    'div', {'id': 'nsechange'}, class_='pricupdn nsechange grn').text.replace(' ', '')
# print(price_change)

#market depth
order = soup.find('div', class_='div_market_depth_table')
order_table = order.find('table', id='best_5_box_table')
order_rows = order_table.findAll("tr")
# final_rows=[]
order_book = {'buy': [], 'sell': []}
for i in range(2, 7):
    # final_rows= final_rows.append(order_rows[i])
    # print(order_rows[i])
    row_elements = order_rows[i].findAll('td')
    print(row_elements)
    # for j in range(0,5):
    order_book['buy'].append(
        {'qty': row_elements[i][0].text, 'price': row_elements[i][1].text})
    order_book['sell'].append(
        {'qty': row_elements[i][2].text, 'price': row_elements[i][3].text})
    print(order_book)
    # break
# print(len(order_rows))


#broker research
broker_research = {'Name': [],
                   'Reco_price': [],
                   'Target': [],
                   'Date': [],
                   'Link': []
                   }
whole_list = soup.find('div', class_='brrs_stock')
new_variable = whole_list.findChildren('div', recursive=False)
# print(len(new_variable))
broker_cards = new_variable[0].findChildren('div', recursive=False)
# print(len(broker_cards))
for card in broker_cards:
    # date_info_div=card.findChildren('div',recursive=False)
    # price_div=card.findChildren('table',recursive=False)
    # #print(len(date_info_div))
    # report_date=date_info_div[0].text
    # info_div=date_info_div[1]
    # #print(date_div.text)
    # #print(info_div.text)
    # name_link=info_div.findChildren('div',recursive=False)
    # #print(len(name_link))
    # name=name_link[0].findChildren('h3',recursive=False)[0].text
    # link=name_link[1].findChildren('a',recursive=False)[0].get('href')
    # print(name)
    # print(link)
    # print(report_date)
    table_items = card.find_all('table')[0].find_all('td')
    print(table_items)
    exit(0)
# basic=whole_list.find('div',class_='brrs_bx grey_bx')
# name=whole_list.find_all('div',class_='brstk_name')
# date=whole_list.find_all('div',class_='br_date')
# link=whole_list.find_all('div',class_='download_report')
# f_link=link
# print(link)
# print(name)
# print(date)
# for var in range(0,len(name)):
    # broker_research['Name'].append(name[var])
    # broker_research['Date'].append(date[var])
# print(broker_research)
