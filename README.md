# JUFinance

[![PyPI Downloads](https://static.pepy.tech/badge/jufinance)](https://pepy.tech/projects/jufinance) [![Monthly Downloads](https://static.pepy.tech/badge/jufinance/month)](https://pepy.tech/projects/jufinance) [![Weekly Downloads](https://static.pepy.tech/badge/jufinance/week)](https://pepy.tech/projects/jufinance)

> **A comprehensive Python package for Indian stock market data analysis and financial research**

JUFinance provides seamless access to real-time stock prices, company fundamentals, financial statements, analyst research, and market depth data from multiple reliable sources including MoneyControl, Screener, and Investing.com.

## 🚀 Quick Start

### Installation

```bash
# Recommended: Install via pip
pip install jufinance

# Development: Install from source
git clone https://github.com/prkedia81/jufinance
cd jufinance
python setup.py install
```

### Verify Installation

```python
import jufinance
print(f"JUFinance version: {jufinance.__version__}")
```

### Basic Usage

```python
from jufinance.scrapers import Quote

# Initialize with stock ticker
hdfc = Quote("HDFC")

# Get current stock price
price = hdfc.get_current_price()
print(f"Current Price: ₹{price}")

# Get comprehensive stock data
all_data = hdfc.get_all_stock_data()
```

## 📊 Core Features

### Real-Time Market Data
- **Current Prices**: Live stock prices with price change indicators
- **Market Depth**: Buy/sell order book with quantities and prices
- **Historical Data**: Time series data for technical analysis

### Company Intelligence
- **Fundamental Analysis**: P/E ratios, book value, dividend yields
- **Financial Statements**: Balance sheet, P&L, cash flow statements
- **Valuation Models**: DCF analysis using industry discount rates

### Research & Analysis
- **Broker Research**: Latest analyst reports with target prices
- **News Feed**: Real-time news affecting stock performance
- **Pros & Cons**: AI-powered investment thesis analysis

## 🛠️ API Reference

### Quote Class

The `Quote` class is your gateway to comprehensive stock analysis. Initialize it with any valid stock ticker from the Indian market.

```python
from jufinance.scrapers import Quote

# Available tickers are defined in /scrapers/links.json
quote = Quote("TICKER_SYMBOL")
```

#### Market Data Methods

##### `get_current_price()`
Returns the latest stock price as a float.

```python
price = quote.get_current_price()
# Returns: 1577.75
```

##### `get_stock_price_change()`
Get price movement with absolute and percentage changes.

```python
change = quote.get_stock_price_change()
# Returns: {'amount_change': 16.25, 'percent_change': 1.04}
```

##### `get_market_depth()`
Access live order book data with buy/sell queues.

```python
depth = quote.get_market_depth()
# Returns detailed buy/sell order information
```

#### Company Information

##### `get_basic_info()`
Retrieve key financial metrics and ratios.

```python
info = quote.get_basic_info()
# Returns: Market cap, P/E ratio, book value, dividend yield, etc.
```

##### `get_stock_info()`
Get comprehensive company profile and sector information.

```python
profile = quote.get_stock_info()
# Returns: Company description, website, exchange links, sector classification
```

#### Financial Analysis

##### `get_financials()`
Access complete financial statements with multi-year data.

```python
financials = quote.get_financials()
# Returns: Balance sheet, P&L, cash flow statements, and key ratios
```

##### `get_dcf_value()`
Get intrinsic value using Discounted Cash Flow analysis.

```python
valuation = quote.get_dcf_value()
# Returns: DCF-based fair value estimate
```

##### `get_pros_and_cons()`
AI-powered analysis of investment opportunities and risks.

```python
analysis = quote.get_pros_and_cons()
# Returns: {'pros': [...], 'cons': [...]}
```

#### Research & News

##### `get_broker_research()`
Latest analyst reports with price targets and recommendations.

```python
research = quote.get_broker_research()
# Returns: Broker name, date, recommendation price, target price, report link
```

##### `get_top_news()`
Recent news articles affecting the stock.

```python
news = quote.get_top_news()
# Returns: Article title, link, publication date
```

##### `get_annual_reports()`
Direct links to official annual reports from BSE and NSE.

```python
reports = quote.get_annual_reports()
# Returns: Dictionary of year-wise annual report links
```

#### Comprehensive Data

##### `get_all_stock_data()`
Retrieve all available data in a single call.

```python
complete_data = quote.get_all_stock_data()
# Returns: All methods' data combined in a structured format
```

##### `get_stock_historical_data()`
Time series data for charting and technical analysis.

```python
historical = quote.get_stock_historical_data()
# Returns: Historical price and volume data
```

## 💡 Usage Examples

### Portfolio Analysis
```python
from jufinance.scrapers import Quote

# Analyze multiple stocks
portfolio = ['HDFC', 'RELIANCE', 'TCS', 'INFY']
analysis = {}

for ticker in portfolio:
    stock = Quote(ticker)
    analysis[ticker] = {
        'price': stock.get_current_price(),
        'change': stock.get_stock_price_change(),
        'pe_ratio': stock.get_basic_info()['Stock P/E'],
        'target_price': stock.get_broker_research()[0]['target_price']
    }

print(analysis)
```

### Investment Research Workflow
```python
# Comprehensive stock research
def research_stock(ticker):
    stock = Quote(ticker)
    
    # Get basic metrics
    basics = stock.get_basic_info()
    profile = stock.get_stock_info()
    
    # Analyze pros and cons
    thesis = stock.get_pros_and_cons()
    
    # Check analyst sentiment
    research = stock.get_broker_research()
    avg_target = sum([r['target_price'] for r in research]) / len(research)
    
    # Get DCF valuation
    intrinsic_value = stock.get_dcf_value()
    
    return {
        'company': profile['name'],
        'sector': profile['sector'],
        'current_price': stock.get_current_price(),
        'analyst_target': avg_target,
        'dcf_value': intrinsic_value,
        'investment_thesis': thesis
    }

# Research a stock
report = research_stock('HDFC')
```

## 🔧 Configuration

### Ticker Symbols
Valid ticker symbols are defined in `/scrapers/links.json`. Common examples include:
- `HDFC` - HDFC Bank
- `RELIANCE` - Reliance Industries
- `TCS` - Tata Consultancy Services
- `INFY` - Infosys Limited

### Data Sources
JUFinance aggregates data from multiple sources:
- **MoneyControl**: Financial statements, news, broker research
- **Screener**: Company fundamentals and ratios
- **Investing.com**: Real-time prices and market data

## 📋 Requirements

- Python 3.6+
- Internet connection for real-time data
- Dependencies automatically installed via pip

## 🔄 Updates & Maintenance

```bash
# Update to latest version
pip install --upgrade jufinance

# Uninstall if needed
pip uninstall jufinance
```

## ⚖️ Legal & Compliance

This package aggregates publicly available financial data. Users must comply with:
- Terms of service of underlying data providers
- Local regulations regarding financial data usage
- Rate limiting and fair use policies

## 🤝 Contributing

We welcome contributions! Please check our GitHub repository for:
- Bug reports and feature requests
- Code contributions and improvements
- Documentation enhancements

## 📞 Support

- **Documentation**: Comprehensive API reference and examples
- **Issues**: Report bugs on GitHub
- **Community**: Join discussions and share insights

---

**Disclaimer**: This package is for educational and research purposes. Always verify financial data from official sources before making investment decisions.
