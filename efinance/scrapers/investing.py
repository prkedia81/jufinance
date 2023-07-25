import datetime as dt

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Investing:
    def __init__(self, ticker, start_time, end_time):
        # self.start_time = int(dt.datetime(start_time).timestamp())
        # self.end_time = int(dt.datetime(end_time).timestamp())
        self.ticker = ticker
        self.URL = f"https://in.investing.com/equities/larsen-toubro-infotech-ltd-historical-data?end_date={end_time}&st_date=-{start_time}"

    def page_html(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.get(self.URL)
        element_present = EC.presence_of_element_located((By.TAG_NAME, "table"))
        WebDriverWait(driver, 100).until(element_present)
        html = driver.page_source
        driver.quit()
        return html

    def historical_price(self):
        soup = BeautifulSoup(self.page_html(), "html.parser")
        table = soup.find("table", class_="common-table medium js-table")
        rows = table.find_all("tr", class_="common-table-item u-clickable")

        historical_data = {
            "date": [],
            "price": [],
            "open": [],
            "high": [],
            "low": [],
            "volume": [],
            "change": [],
        }

        for row in rows:
            cols = row.find_all("td")
            historical_data["date"].append(cols[0].text.strip())
            historical_data["price"].append(self.string_to_num(str=cols[1].text))
            historical_data["open"].append(self.string_to_num(str=cols[2].text))
            historical_data["high"].append(self.string_to_num(str=cols[3].text))
            historical_data["low"].append(self.string_to_num(str=cols[4].text))
            historical_data["volume"].append(self.string_to_num(str=cols[5].text))
            historical_data["change"].append(self.string_to_num(str=cols[6].text))
        return historical_data
        # print(historical_data)

    def string_to_num(self, str):
        try:
            return float(str.strip().replace(",", "").replace("%", ""))
        except ValueError:
            return str
        except TypeError:
            return str
