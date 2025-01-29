# JUFinance
[![PyPI Downloads](https://static.pepy.tech/badge/jufinance)](https://pepy.tech/projects/jufinance)  [![PyPI Downloads](https://static.pepy.tech/badge/jufinance/month)](https://pepy.tech/projects/jufinance)  [![PyPI Downloads](https://static.pepy.tech/badge/jufinance/week)](https://pepy.tech/projects/jufinance)

### All-in-one Python Package for all stock market data.

# Installation

You can install jufinance using the following methods:

### Using pip

The recommended way to install JUFinance is by using pip, the Python package manager. Open your command-line interface (CLI) and enter the following command:

```python
pip install jufinance
```

This will automatically download and install jufinance.

### From Source

If you prefer to install jufinance from its source code, you can clone the GitHub repository. First, navigate to the directory where you want to clone the repository and then use the following commands:

```python
git clone https://github.com/prkedia81/jufinance
cd jufinance
setup.py install
```

# Verifying Installation

After installation, you can verify if jufiance was installed successfully by opening a Python interpreter and trying to import it:

```python
import jufinance
print("jufinance version:", jufinance.__version__)
```

# Updating

To update jufinance to the latest version, you can use pip again:

```
pip install --upgrade jufinance
```

# Unistallation

If you ever need to uninstall jufinance, you can use pip as well:

```
pip uninstall jufinance
```

# Quote Details Retriever

The Quote class in this module allows you to retrieve various details about a stock quote, including its current price, company information, historical data, market depth, broker research, and more. It utilizes data from different sources such as Investing, MoneyControl, and Screener.

## Usage

To use the Quote class and retrieve stock details, follow these steps:

1. Import the required classes from the jufinance.scrapers module:

```python
    from jufinance.scrapers import Investing, MoneyControl, Screener
```

---

2. Create an instance of the Quote class, providing the stock ticker as an argument:

```python
    quote = Quote("TICKER")
```

**The value of "TICKER can be set from the key of the stocks present in "/scrapers/links.json"**

> **_Let TICKER be "HDFC" for example_** (Without Quotes)

---

3. You can then call various methods on the quote object to retrieve specific details:

- #### To get all available stock data:

```python
all_stock_data = quote.get_all_stock_data()
print(all_stock_data)
```

- #### To get the current price:

```python
current_price = quote.get_current_price()
print(current_price)
```

**Output :**

> 1577.75

- #### To get the stock's basic information:

```python
     basic_info = quote.get_basic_info()
     print(basic_info)
```

**Output:**

> {'Market Cap': '11,93,408', 'Current Price': '1,578', 'High / Low': '1,758', 'Stock P/E': '18.0', 'Book Value': '519', 'Dividend Yield': '1.20', 'ROCE': '6.24', 'ROE': '17.1', 'Face Value': '1.00'}

- #### To get the stock's description:

```python
     description = quote.get_stock_info()
     print(description)
```

**Output :**

> {'name': 'HDFC Bank Ltd', 'about': "The Housing Development Finance Corporation Limited (HDFC) was amongst the first to receive an 'in principle' approval from the Reserve Bank of India (RBI) to set up a bank in the private sector. HDFC Bank is a publicly held banking company, the bank was incorporated in August 1994 in the name of 'HDFC Bank Limited', with its registered office in Mumbai, India. It is engaged in providing a range of banking and financial services including retail banking, wholesale banking and treasury operations. It is promoted by HDFC Ltd. which has 19.32% stake as on September 30, 2020. Currently, HDFC Bank Ltd. (HBL) is the largest private sector bank in India.", 'link': 'http://www.hdfcbank.com', 'bse_link': 'https://www.bseindia.com/stock-share-price/hdfc-bank-ltd/HDFCBANK/500180/', 'nse_link': 'https://www.nseindia.com/get-quotes/equity?symbol=HDFCBANK', 'sector': 'Banks', 'industry': 'Banks - Private Sector'}

- #### To get the stock's historical data:

```python
     historical_data = quote.get_stock_historical_data()
     print(historic_data)
```
- #### To get the stock's DCF Valuation using industry discount rates:

```python
     dcf_valuation = quote.get_dcf_value()
     print(dcf_valuation)
```

- #### To get the stock's price change:

```python
     price_change = quote.get_stock_price_change()
     print(price_change)
```

**Output :**

> {'amount_change': 16.25, 'percent_change': 1.04}

- #### To get the market depth:

```python
     market_depth = quote.get_market_depth()
     print(market_depth)
```

**Output :**

> {'buy': [{'qty': '441', 'price': '1577.00'}, {'qty': '1', 'price': '1576.90'}, {'qty': '73', 'price': '1576.10'}, {'qty': '1194', 'price': '1576.00'}, {'qty': '73', 'price': '1575.90'}], 'sell': [{'qty': '1311', 'price': '1577.90'}, {'qty': '270', 'price': '1578.00'}, {'qty': '100', 'price': '1578.30'}, {'qty': '39', 'price': '1578.40'}, {'qty': '15', 'price': '1578.95'}]}

- #### To get broker research data:

```python
     broker_research = quote.get_broker_research()
     print(broker_research)
```

**Output :**

> [{'name': 'Motilal Oswal', 'date': '27 Jul, 2023', 'reco_price': 1673.65, 'target_price': 2070.0, 'link': 'https://images.moneycontrol.com/static-mcnews/2023/07/HDFC-Bank-28-07-2023-moti.pdf'}, {'name': 'Geofin Comtrade', 'date': '25 Jul, 2023', 'reco_price': 1696.4, 'target_price': 1964.0, 'link': 'https://images.moneycontrol.com/static-mcnews/2023/07/HDFC-Bank-25-07-2023-geo.pdf'}, {'name': 'Motilal Oswal', 'date': '17 Jul, 2023', 'reco_price': 1679.2, 'target_price': 2070.0, 'link': 'https://images.moneycontrol.com/static-mcnews/2023/07/HDFC-Bank-18-07-2023-moti.pdf'}, {'name': 'Prabhudas Lilladher', 'date': '18 Jul, 2023', 'reco_price': 1677.2, 'target_price': 2025.0, 'link': 'https://images.moneycontrol.com/static-mcnews/2023/07/HDFC-Bank-18-07-2023-prabhu.pdf'}, {'name': 'LKP Securities Limited', 'date': '18 Jul, 2023', 'reco_price': 1677.2, 'target_price': 2074.0, 'link': 'https://images.moneycontrol.com/static-mcnews/2023/07/HDFC-Bank-18-07-2023-lkp.pdf'}, {'name': 'Axis Securities Limited ', 'date': '18 Jul, 2023', 'reco_price': 1677.2, 'target_price': 2050.0, 'link': 'https://images.moneycontrol.com/static-mcnews/2023/07/HDFC-Bank-18-07-2023-axis.pdf'}]

- #### To get the pros and cons of the stock:

```python
     pros_and_cons = quote.get_pros_and_cons()
     print(pros_and_cons)
```

**Output :**

> {'pros': ['Company is expected to give good quarter', 'Company has delivered good profit growth of 19.9% CAGR over last 5 years', 'Company has been maintaining a healthy dividend payout of 19.0%'], 'cons': ['Stock is trading at 3.04 times its book value', 'Company has low interest coverage ratio.', 'Contingent liabilities of Rs.18,22,393 Cr.', 'Company might be capitalizing the interest cost', 'Working capital days have increased from -7.26 days to 92.2 days']}

- #### To get the financial statements:

```python
     financials = quote.get_financials()
     print(financials)
```

**Output:**

> {'bs': {'id': 'balance-sheet', 'title': 'Balance Sheet', 'content': {'Share Capital\xa0+': [{'Mar 2012': '469'}, {'Mar 2013': '476'}, {'Mar 2014': '480'}, {'Mar 2015': '501'}, {'Mar 2016': '506'}, {'Mar 2017': '513'}, {'Mar 2018': '519'}, {'Mar 2019': '545'}, {'Mar 2020': '548'}, {'Mar 2021': '551'}, {'Mar 2022': '555'}, {'Mar 2023': '558'}], 'Reserves': [{'Mar 2012': '29,741'}, {'Mar 2013': '36,167'}, {'Mar 2014': '43,687'}, {'Mar 2015': '62,653'}, {'Mar 2016': '73,798'}, {'Mar 2017': '91,281'}, {'Mar 2018': '109,080'}, {'Mar 2019': '153,128'}, {'Mar 2020': '175,810'}, {'Mar 2021': '209,259'}, {'Mar 2022': '246,772'}, {'Mar 2023': '288,880'}], 'Borrowings\xa0+': [{'Mar 2012': '272,874'}, {'Mar 2013': '335,588'}, {'Mar 2014': '416,677'}, {'Mar 2015': '509,762'}, {'Mar 2016': '649,587'}, {'Mar 2017': '741,550'}, {'Mar 2018': '944,817'}, {'Mar 2019': '1,080,235'}, {'Mar 2020': '1,333,041'}, {'Mar 2021': '1,511,418'}, {'Mar 2022': '1,784,970'}, {'Mar 2023': '2,139,212'}], 'Other Liabilities\xa0+': [{'Mar 2012': '37,971'}, {'Mar 2013': '35,492'}, {'Mar 2014': '42,776'}, {'Mar 2015': '34,181'}, {'Mar 2016': '38,321'}, {'Mar 2017': '59,000'}, {'Mar 2018': '48,770'}, {'Mar 2019': '58,898'}, {'Mar 2020': '71,430'}, {'Mar 2021': '78,279'}, {'Mar 2022': '90,639'}, {'Mar 2023': '101,783'}], 'Total Liabilities': [{'Mar 2012': '341,055'}, {'Mar 2013': '407,723'}, {'Mar 2014': '503,620'}, {'Mar 2015': '607,097'}, {'Mar 2016': '762,212'}, {'Mar 2017': '892,344'}, {'Mar 2018': '1,103,186'}, {'Mar 2019': '1,292,806'}, {'Mar 2020': '1,580,830'}, {'Mar 2021': '1,799,507'}, {'Mar 2022': '2,122,934'}, {'Mar 2023': '2,530,432'}], 'Fixed Assets\xa0+': [{'Mar 2012': '2,378'}, {'Mar 2013': '2,773'}, {'Mar 2014': '3,026'}, {'Mar 2015': '3,225'}, {'Mar 2016': '3,667'}, {'Mar 2017': '4,000'}, {'Mar 2018': '4,008'}, {'Mar 2019': '4,369'}, {'Mar 2020': '4,776'}, {'Mar 2021': '5,248'}, {'Mar 2022': '6,432'}, {'Mar 2023': '8,431'}], 'CWIP': [{'Mar 2012': '0'}, {'Mar 2013': '0'}, {'Mar 2014': '0'}, {'Mar 2015': '0'}, {'Mar 2016': '0'}, {'Mar 2017': '0'}, {'Mar 2018': '0'}, {'Mar 2019': '0'}, {'Mar 2020': '0'}, {'Mar 2021': '0'}, {'Mar 2022': '0'}, {'Mar 2023': '0'}], 'Investments': [{'Mar 2012': '96,795'}, {'Mar 2013': '110,960'}, {'Mar 2014': '119,571'}, {'Mar 2015': '149,454'}, {'Mar 2016': '193,634'}, {'Mar 2017': '210,777'}, {'Mar 2018': '238,461'}, {'Mar 2019': '289,446'}, {'Mar 2020': '389,305'}, {'Mar 2021': '438,823'}, {'Mar 2022': '449,264'}, {'Mar 2023': '511,582'}], 'Other Assets\xa0+': [{'Mar 2012': '241,882'}, {'Mar 2013': '293,989'}, {'Mar 2014': '381,023'}, {'Mar 2015': '454,417'}, {'Mar 2016': '564,912'}, {'Mar 2017': '677,567'}, {'Mar 2018': '860,717'}, {'Mar 2019': '998,991'}, {'Mar 2020': '1,186,750'}, {'Mar 2021': '1,355,435'}, {'Mar 2022': '1,667,238'}, {'Mar 2023': '2,010,419'}], 'Total Assets': [{'Mar 2012': '341,055'}, {'Mar 2013': '407,723'}, {'Mar 2014': '503,620'}, {'Mar 2015': '607,097'}, {'Mar 2016': '762,212'}, {'Mar 2017': '892,344'}, {'Mar 2018': '1,103,186'}, {'Mar 2019': '1,292,806'}, {'Mar 2020': '1,580,830'}, {'Mar 2021': '1,799,507'}, {'Mar 2022': '2,122,934'}, {'Mar 2023': '2,530,432'}]}}, 'pnl': {'id': 'profit-loss', 'title': 'Profit & Loss', 'content': {'Revenue': [{'Mar 2012': '28,193'}, {'Mar 2013': '35,861'}, {'Mar 2014': '42,555'}, {'Mar 2015': '50,666'}, {'Mar 2016': '63,162'}, {'Mar 2017': '73,271'}, {'Mar 2018': '85,288'}, {'Mar 2019': '105,161'}, {'Mar 2020': '122,189'}, {'Mar 2021': '128,552'}, {'Mar 2022': '135,936'}, {'Mar 2023': '170,754'}, {'TTM': '184,648'}], 'Interest': [{'Mar 2012': '15,106'}, {'Mar 2013': '19,695'}, {'Mar 2014': '23,445'}, {'Mar 2015': '27,288'}, {'Mar 2016': '34,070'}, {'Mar 2017': '38,042'}, {'Mar 2018': '42,381'}, {'Mar 2019': '53,713'}, {'Mar 2020': '62,137'}, {'Mar 2021': '59,248'}, {'Mar 2022': '58,584'}, {'Mar 2023': '77,780'}, {'TTM': '87,376'}], 'Expenses\xa0+': [{'Mar 2012': '10,858'}, {'Mar 2013': '12,631'}, {'Mar 2014': '13,508'}, {'Mar 2015': '16,164'}, {'Mar 2016': '20,055'}, {'Mar 2017': '23,856'}, {'Mar 2018': '29,532'}, {'Mar 2019': '34,856'}, {'Mar 2020': '45,459'}, {'Mar 2021': '52,457'}, {'Mar 2022': '56,557'}, {'Mar 2023': '63,042'}, {'TTM': '68,837'}], 'Financing Profit': [{'Mar 2012': '2,229'}, {'Mar 2013': '3,534'}, {'Mar 2014': '5,602'}, {'Mar 2015': '7,214'}, {'Mar 2016': '9,037'}, {'Mar 2017': '11,374'}, {'Mar 2018': '13,374'}, {'Mar 2019': '16,592'}, {'Mar 2020': '14,593'}, {'Mar 2021': '16,848'}, {'Mar 2022': '20,795'}, {'Mar 2023': '29,932'}, {'TTM': '28,435'}], 'Financing Margin %': [{'Mar 2012': '8%'}, {'Mar 2013': '10%'}, {'Mar 2014': '13%'}, {'Mar 2015': '14%'}, {'Mar 2016': '14%'}, {'Mar 2017': '16%'}, {'Mar 2018': '16%'}, {'Mar 2019': '16%'}, {'Mar 2020': '12%'}, {'Mar 2021': '13%'}, {'Mar 2022': '15%'}, {'Mar 2023': '18%'}, {'TTM': '15%'}], 'Other Income\xa0+': [{'Mar 2012': '5,992'}, {'Mar 2013': '7,133'}, {'Mar 2014': '8,298'}, {'Mar 2015': '9,546'}, {'Mar 2016': '11,212'}, {'Mar 2017': '12,905'}, {'Mar 2018': '16,057'}, {'Mar 2019': '18,947'}, {'Mar 2020': '24,879'}, {'Mar 2021': '27,333'}, {'Mar 2022': '31,759'}, {'Mar 2023': '33,912'}, {'TTM': '36,837'}], 'Depreciation': [{'Mar 2012': '554'}, {'Mar 2013': '663'}, {'Mar 2014': '689'}, {'Mar 2015': '680'}, {'Mar 2016': '738'}, {'Mar 2017': '886'}, {'Mar 2018': '967'}, {'Mar 2019': '1,221'}, {'Mar 2020': '1,277'}, {'Mar 2021': '1,385'}, {'Mar 2022': '1,681'}, {'Mar 2023': '2,345'}, {'TTM': '0'}], 'Profit before tax': [{'Mar 2012': '7,667'}, {'Mar 2013': '10,004'}, {'Mar 2014': '13,211'}, {'Mar 2015': '16,079'}, {'Mar 2016': '19,511'}, {'Mar 2017': '23,393'}, {'Mar 2018': '28,464'}, {'Mar 2019': '34,318'}, {'Mar 2020': '38,195'}, {'Mar 2021': '42,796'}, {'Mar 2022': '50,873'}, {'Mar 2023': '61,498'}, {'TTM': '65,272'}], 'Tax %': [{'Mar 2012': '31%'}, {'Mar 2013': '31%'}, {'Mar 2014': '34%'}, {'Mar 2015': '33%'}, {'Mar 2016': '34%'}, {'Mar 2017': '35%'}, {'Mar 2018': '35%'}, {'Mar 2019': '35%'}, {'Mar 2020': '29%'}, {'Mar 2021': '26%'}, {'Mar 2022': '25%'}, {'Mar 2023': '25%'}, {'TTM': ''}], 'Net Profit\xa0+': [{'Mar 2012': '5,277'}, {'Mar 2013': '6,903'}, {'Mar 2014': '8,768'}, {'Mar 2015': '10,703'}, {'Mar 2016': '12,821'}, {'Mar 2017': '15,317'}, {'Mar 2018': '18,561'}, {'Mar 2019': '22,446'}, {'Mar 2020': '27,296'}, {'Mar 2021': '31,857'}, {'Mar 2022': '38,151'}, {'Mar 2023': '46,149'}, {'TTM': '48,935'}], 'EPS in Rs': [{'Mar 2012': '11.18'}, {'Mar 2013': '14.44'}, {'Mar 2014': '18.22'}, {'Mar 2015': '21.32'}, {'Mar 2016': '25.32'}, {'Mar 2017': '29.81'}, {'Mar 2018': '35.66'}, {'Mar 2019': '41.00'}, {'Mar 2020': '49.70'}, {'Mar 2021': '57.74'}, {'Mar 2022': '68.62'}, {'Mar 2023': '82.44'}, {'TTM': '87.43'}], 'Dividend Payout %': [{'Mar 2012': '19%'}, {'Mar 2013': '19%'}, {'Mar 2014': '19%'}, {'Mar 2015': '19%'}, {'Mar 2016': '19%'}, {'Mar 2017': '18%'}, {'Mar 2018': '18%'}, {'Mar 2019': '18%'}, {'Mar 2020': '5%'}, {'Mar 2021': '11%'}, {'Mar 2022': '23%'}, {'Mar 2023': '23%'}, {'TTM': ''}]}}, 'cashflow': {'id': 'cash-flow', 'title': 'Cash Flows', 'content': {'Cash from Operating Activity\xa0+': [{'Mar 2012': '-19,381'}, {'Mar 2013': '-5,847'}, {'Mar 2014': '4,211'}, {'Mar 2015': '-21,281'}, {'Mar 2016': '-34,435'}, {'Mar 2017': '17,282'}, {'Mar 2018': '17,214'}, {'Mar 2019': '-62,872'}, {'Mar 2020': '-16,869'}, {'Mar 2021': '42,476'}, {'Mar 2022': '-11,960'}, {'Mar 2023': '20,814'}], 'Cash from Investing Activity\xa0+': [{'Mar 2012': '-662'}, {'Mar 2013': '-902'}, {'Mar 2014': '-1,099'}, {'Mar 2015': '-800'}, {'Mar 2016': '-837'}, {'Mar 2017': '-1,146'}, {'Mar 2018': '-842'}, {'Mar 2019': '-1,503'}, {'Mar 2020': '-1,403'}, {'Mar 2021': '-1,823'}, {'Mar 2022': '-2,051'}, {'Mar 2023': '-2,992'}], 'Cash from Financing Activity\xa0+': [{'Mar 2012': '11,380'}, {'Mar 2013': '13,105'}, {'Mar 2014': '9,270'}, {'Mar 2015': '18,694'}, {'Mar 2016': '37,815'}, {'Mar 2017': '-5,893'}, {'Mar 2018': '57,378'}, {'Mar 2019': '23,131'}, {'Mar 2020': '24,394'}, {'Mar 2021': '-7,321'}, {'Mar 2022': '48,124'}, {'Mar 2023': '23,941'}], 'Net Cash Flow': [{'Mar 2012': '-8,663'}, {'Mar 2013': '6,356'}, {'Mar 2014': '12,382'}, {'Mar 2015': '-3,387'}, {'Mar 2016': '2,542'}, {'Mar 2017': '10,242'}, {'Mar 2018': '73,750'}, {'Mar 2019': '-41,244'}, {'Mar 2020': '6,122'}, {'Mar 2021': '33,332'}, {'Mar 2022': '34,113'}, {'Mar 2023': '41,762'}]}}, 'common_ratios': {'id': 'ratios', 'title': 'Ratios', 'content': {'ROE %': [{'Mar 2012': '19%'}, {'Mar 2013': '21%'}, {'Mar 2014': '22%'}, {'Mar 2015': '20%'}, {'Mar 2016': '19%'}, {'Mar 2017': '18%'}, {'Mar 2018': '18%'}, {'Mar 2019': '17%'}, {'Mar 2020': '16%'}, {'Mar 2021': '16%'}, {'Mar 2022': '17%'}, {'Mar 2023': '17%'}]}}}

- #### To get the annual reports:

```python
     annual_reports = quote.get_annual_reports()
     print(annual_reports)
```

**Output:**

> {'Financial Year 2023from bse': 'https://www.bseindia.com/xml-data/corpfiling/AttachHis/\\0fb0e6bd-7110-44c3-a750-76933ddf105c.pdf', 'Financial Year 2022from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/73256500180.pdf', 'Financial Year 2021from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/68609500180.pdf', 'Financial Year 2020from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800320.pdf', 'Financial Year 2019from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800319.pdf', 'Financial Year 2018from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800318.pdf', 'Financial Year 2017from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800317.pdf', 'Financial Year 2016from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800316.pdf', 'Financial Year 2015from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800315.pdf', 'Financial Year 2014from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800314.pdf', 'Financial Year 2013from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800313.pdf', 'Financial Year 2012from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800312.pdf', 'Financial Year 2012from nse': 'https://archives.nseindia.com/annual_reports/AR_HDFCBANK_2011_2012_20062012100212.zip', 'Financial Year 2011from bse': 'https://www.bseindia.com/bseplus/AnnualReport/500180/5001800311.pdf', 'Financial Year 2011from nse': 'https://archives.nseindia.com/annual_reports/AR_HDFCBANK_2010_2011_14072011105623.zip'}

- #### To get the top news:

```python
     top_news = quote.get_top_news()
     print(top_news)
```

**Output:**

> [{'name': 'Market corrects post RBI MPC outcome| Bet on these top 10 rate-sensitive stocks', 'link': 'https://www.moneycontrol.com/news/business/markets/market-corrects-post-rbi-ups-inflation-forecast-icrr-bet-on-these-top-10-rate-sensitive-stocks-ideas-11142611.html', 'date': 'Aug 10 2023 01:08 PM'}, {'name': 'Analyst Call Tracker | Banks dare margin pressure, dominate optimism list', 'link': 'https://www.moneycontrol.com/news/business/stocks/analyst-call-tracker-banks-dare-margin-pressure-dominate-optimism-list-11139671.html', 'date': 'Aug 10 2023 10:08 AM'}, {'name': 'FTSE to implement upweight of HDFC Bank in three tranches starting September', 'link': 'https://www.moneycontrol.com/news/business/markets/ftse-to-implement-upweight-of-hdfc-bank-in-three-tranches-starting-september-11117231.html', 'date': 'Aug 07 2023 08:08 PM'}, {'name': 'Fitch Glitch: Investors lose Rs 3.56 lakh cr as Dalal Street joins global selloff', 'link': 'https://www.moneycontrol.com/news/business/markets/fitch-glitch-investors-lose-rs-3-56-lakh-cr-as-dalal-street-joins-global-selloff-11083331.html', 'date': 'Aug 02 2023 04:08 PM'}]

# Documentation

For a detailed overview of each method and its parameters, refer to the class definition and method comments in the quote.py file.

# Dependencies

jufinance (installable via pip)

# Attribution

This module uses data from Investing, MoneyControl, and Screener APIs. Make sure to comply with their respective terms of use and API documentation.
