# Get the quote details
# - current price, company info, etc.

from scrapers.screener import Screener


class Quote:
    def __init__(self, ticker):
        print("Invoked Quote module...")
        self.screener = Screener(ticker=ticker)
        self.screener.get_soup()

    def get_current_price(self):
        print("Getting current price")
        self.screener.latest_price()

    def get_stock_info(self):
        print("Getting company information")
        self.screener.stock_information()  # only gets company desc

    def get_stock_historical_data(self):
        print("Getting stock historical data")

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

    
