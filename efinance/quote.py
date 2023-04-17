# Get the quote details
# - current price, company info, etc.

from scrapers.investing import Investing
from scrapers.moneycontrol import MoneyControl
from scrapers.screener import Screener


class Quote:
    def __init__(self, ticker):
        print("Invoked Quote module...")
        self.screener = Screener(ticker=ticker)
        self.screener.get_soup()
        self.mc = MoneyControl(ticker=ticker)
        self.mc.get_soup()
        self.investing = Investing(
            ticker=ticker, start_time=1070343000, end_time=1681671410)

    def get_current_price(self):
        print("Getting current price")
        self.mc.current_price()

    def get_stock_info(self):
        print("Getting company information")
        self.screener.stock_information()  # only gets company desc

    def get_stock_historical_data(self):
        print("Getting stock historical data")
        self.investing.historical_price()

    def get_stock_price_change(self):
        print("Getting stock price change")
        self.mc.price_change()

    def get_market_depth(self):
        print("Getting market depth")
        self.mc.market_depth()

    def get_broker_research(self):
        print("Getting broker research")
        self.mc.broker_research()

    def get_pros_and_cons(self):
        print("Getting pros and cons")
        self.screener.pros_and_cons()

    def get_basic_info(self):
        print("Getting basic info")
        self.screener.basic_info()

    def get_financials(self):
        print("Getting financials")
        self.screener.profit_loss_statement()
        self.screener.cash_flow_statement()

    def get_annual_reports(self):
        print("Getting annual reports")
        self.screener.annual_reports()

    def get_top_news(self):
        print("Getting top news")
        self.mc.top_news()
