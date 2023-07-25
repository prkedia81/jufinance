# Get the quote details
# - current price, company info, etc.

from efinance.scrapers import Investing, MoneyControl, Screener


class Quote:
    def __init__(self, ticker):
        # print("Invoked Quote module...")
        self.screener = Screener(ticker=ticker)
        self.screener.get_soup()
        self.mc = MoneyControl(ticker=ticker)
        self.mc.get_soup()
        self.investing = Investing(
            ticker=ticker, start_time=1070343000, end_time=1681671410
        )

    def get_all_stock_data(self):
        all_data = {
            "current_price": self.get_current_price(),
            "basic_info": self.get_basic_info(),
            "description": self.get_stock_info(),
            "historical_data": self.get_historical_data(),
            "price_change": self.get_price_change(),
            "market_depth": self.get_market_depth(),
            "broker_research": self.get_broker_research(),
            "pros_and_cons": self.get_pros_and_cons(),
            "financials": self.get_financials(),
            "annual_reports": self.get_annual_reports(),
            "top_news": self.get_top_news(),
        }

        return all_data

    def get_current_price(self):
        # print("Getting current price")
        return self.mc.current_price()

    def get_stock_info(self):
        # print("Getting company information")
        return self.screener.stock_information()  # only gets company desc

    def get_stock_historical_data(self):
        # print("Getting stock historical data")
        return self.investing.historical_price()

    def get_stock_price_change(self):
        # print("Getting stock price change")
        return self.mc.price_change()

    def get_market_depth(self):
        # print("Getting market depth")
        return self.mc.market_depth()

    def get_broker_research(self):
        # print("Getting broker research")
        return self.mc.broker_research()

    def get_pros_and_cons(self):
        # print("Getting pros and cons")
        return self.screener.pros_and_cons()

    def get_basic_info(self):
        # print("Getting basic info")
        return self.screener.basic_info()

    def get_financials(self):
        # print("Getting financials")
        financials = {
            "pnl": self.screener.profit_loss_statement(),
            "cashflow": self.screener.cash_flow_statement(),
        }
        return financials

    def get_annual_reports(self):
        # print("Getting annual reports")
        return self.screener.annual_reports()

    def get_top_news(self):
        # print("Getting top news")
        return self.mc.top_news()
