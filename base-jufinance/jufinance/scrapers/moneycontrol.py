import requests
from bs4 import BeautifulSoup


class MoneyControl:
    def __init__(self, ticker):
        # print("Invoked Money Control Module")
        self.ticker = ticker

    def get_soup(self):
        self.mc_URL = "https://www.moneycontrol.com/india/stockpricequote/paintsvarnishes/bergerpaintsindia/BPI02"
        api_response = requests.get(self.mc_URL).text
        self.soup = BeautifulSoup(api_response, "html.parser")

    def current_price(self):
        """
        Returns the current price of a stock.

        This function uses web scraping to find the current price of a stock. It searches for a specific HTML element 
        using the BeautifulSoup library and extracts the text value of that element. The stock price is then returned.

        Parameters:
            self (object): The instance of the class.

        Returns:
            str: The current price of the stock as a string.
        """
        price = self.soup.find("div", class_="indimprice")
        stock_price = price.find("div", {"id": "nsecp"}, class_="inprice1 nsecp").text
        return stock_price

    def market_depth(self):
        """
        Retrieves the market depth data from the HTML soup object.

        Returns:
            dict: A dictionary containing the buy and sell order book.
                The buy order book is represented as a list of dictionaries,
                where each dictionary contains the quantity and price of a buy order.
                The sell order book is also represented as a list of dictionaries,
                where each dictionary contains the quantity and price of a sell order.
        """
        order = self.soup.find("div", class_="div_market_depth_table")
        order_table = order.find("table", id="best_5_box_table")
        order_rows = order_table.findAll("tr")
        order_book = {"buy": [], "sell": []}
        for i in range(2, len(order_rows) - 1):
            row_elements = order_rows[i].findAll("td")
            order_book["buy"].append(
                {"qty": row_elements[0].text, "price": row_elements[1].text}
            )
            order_book["sell"].append(
                {"qty": row_elements[3].text, "price": row_elements[2].text}
            )
        return order_book

    def price_change(self):
        """
        Retrieves the price change information from the website.

        Returns:
            change (dict): A dictionary containing the amount change and percent change.

        Raises:
            AttributeError: If the website structure has changed and the required elements cannot be found.
        """
        change = self.soup.find("div", class_="indimprice")
        price_change = change.find(
            "div", {"id": "nsechange"}, class_="pricupdn nsechange grn"
        ).text.replace(" ", "")
        final_result = price_change.split("(")
        change = {
            "amount_change": float(final_result[0]),
            "percent_change": float(final_result[1][:-2]),
        }
        return change

    def broker_research(self):
        """
        Retrieves broker research data from a webpage and returns a list of dictionaries containing the research information.

        Returns:
            all_broker_research (list): A list of dictionaries, where each dictionary represents a broker research report.
                Each dictionary contains the following keys:
                - name (str): The name of the broker.
                - date (str): The date of the research report.
                - reco_price (float): The recommended price mentioned in the report.
                - target_price (float): The target price mentioned in the report.
                - link (str): The link to the full research report.
        """
        all_broker_research = []
        whole_list = self.soup.find("div", class_="brrs_stock")
        new_variable = whole_list.findChildren("div", recursive=False)
        broker_cards = new_variable[0].findChildren("div", recursive=False)
        for card in broker_cards:
            broker_research = {}
            date_info_div = card.findChildren("div", recursive=False)
            price_div = card.findChildren("table", recursive=False)
            report_date = date_info_div[0].text
            info_div = date_info_div[1]
            call = card.findChildren("button", recursive=False)[0].text
            name_link = info_div.findChildren("div", recursive=False)
            name = name_link[0].findChildren("h3", recursive=False)[0].text
            link = name_link[1].findChildren("a", recursive=False)[0].get("href")
            table_items = card.find_all("table")[0].find_all("td")
            reco_price = float(table_items[0].text.split("Reco Price")[1].strip())
            target_price = float(table_items[1].text.split("Target Price")[1].strip())
            broker_research["name"] = name
            broker_research["date"] = report_date
            broker_research["reco_price"] = reco_price
            broker_research["target_price"] = target_price
            broker_research["link"] = link
            all_broker_research.append(broker_research)
        return all_broker_research

    def top_news(self):
        """
        Retrieves the top news from the webpage.

        Returns:
            list: A list of dictionaries containing the name, link, and date of each top news item.
        """
        li_list = self.soup.select("#news > div.news_list.clearfix > ul > li")
        top_news = []
        for item in li_list:
            news = {}
            name = item.find("img").attrs["title"]
            link = item.find("a").attrs["href"]
            date = item.find("span").text.strip()
            news["name"] = name
            news["link"] = link
            news["date"] = date
            top_news.append(news)
        return top_news
