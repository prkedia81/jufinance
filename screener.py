from bs4 import BeautifulSoup
import requests
import json
import re

# import pandas as pd
response = requests.get(
    'https://www.screener.in/company/ITC/consolidated/').text
soup = BeautifulSoup(response, 'html.parser')

# financials : array of tables
financials = [
    {
        "id": "table_id",
        "title": "NAME",
        "content": {
            "row_header_1": [
                {"column_header": "cell_value"},
                {"column_header": "cell_value"}
            ],
            "row_header_2": [
                {"column_header": "cell_value"},
                {"column_header": "cell_value"}
            ]
        },
    },
    {
        "id": "table_id",
        "title": "Quarterly Financials",
        "content": {
            "Revenues": [
                {"Sept'21": 123},
                {"March'21": 456}
            ],
            "Expense": [
                {"Sept'21": 123},
                {"March'21": 456}]
        },
    },
    {},
]

# About the Company
about = soup.select('#top .company-info .company-profile p')[0].text

# Pros & Cons
pros = [item.text for item in soup.select('#analysis .pros li')]
cons = [item.text for item in soup.select('#analysis .cons li')]

# Top Ratios
ratios_html = soup.select('#top-ratios li')
ratios = {ratio.find_all(class_="name")[0].text.strip(): ratio.find_all(
    class_="number")[0].text.strip() for ratio in ratios_html}

# Peer Comparison
peer_html = soup.select('#peers')[0]
sector_industry = [term for term in re.split("\s\s", peer_html.find_all(class_='sub')[
    0].text.replace('\n', '').strip()) if term != ""]
sector = sector_industry[1]
industry = sector_industry[3]
# Cannot scrape peer data using screener.in

# Documents - announcements, annual reports, credit reports, concalls
documents = {}
announcements_li_items = soup.select("#company-announcements-tab li")
documents['company-announcements'] = {item.text.replace('\n', '').replace(
    '  ', '').strip(): item.a['href'] for item in announcements_li_items}

document_class = ['annual-reports', 'credit-ratings', 'concalls']
for class_name in document_class:
    document_html = soup.select(f'#documents .{class_name}')[0]
    title = document_html.h3.text.strip()
    li_items = document_html.find_all("li")
    document = {item.text.replace('\n', '').replace(
        '  ', '').strip(): item.a['href'] for item in li_items}

    documents[class_name] = document

print(documents)
with open('./documents.json', 'w') as fp:
    json.dump(documents, fp)

# Financials - Quarterly Report, P&L Statement, Balance Sheet, Cash Flow Statement, Financial Rations, Shareholding Pattern
table_ids = ['quarters', 'profit-loss', 'balance-sheet',
             'cash-flow', 'ratios', 'shareholding']
financials = []
for table_id in table_ids:
    title = soup.select(f'#{table_id} h2')[0].text.strip()  # Quarterly Results
    table = {
        "id": table_id,
        "title": title,
        "content": {},
    }

    th = soup.select(f'#{table_id} table thead tr th')  # [<td> </td>]
    # ['', 'September 2021', 'September 2023']
    th = [head.text.strip() for head in th]
    col_num = len(th)  # 14
    # ['Sales', 12,903', '1234234', '13234']
    td = soup.select(f'#{table_id} table tbody td')

    counter = 0
    row_head = ''
    for cell in td:
        item = cell.text.strip()
        if counter == 0:
            table['content'][item] = []
            row_head = item
            counter += 1
        elif counter == col_num:
            counter = 1
            table['content'][item] = []
            row_head = item
        else:
            table['content'][row_head].append({
                th[counter]: item
            })
            counter += 1

    financials.append(table)

with open('./financials.json', 'w') as fp:
    json.dump(financials, fp)
