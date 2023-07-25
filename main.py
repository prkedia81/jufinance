from efinance import Quote

tickers = ["INFY", "RELIANCE", "HDFCBANK", "HDFC"]
quote = Quote(tickers[1])

# quote.get_stock_info()

# quote.get_current_price()

# quote.get_pros_and_cons()

# quote.get_basic_info()

# quote.get_financials()

# quote.get_annual_reports()

# quote.get_market_depth()

# quote.get_stock_price_change()

# quote.get_broker_research()

# quote.get_top_news()

quote.get_stock_historical_data()
