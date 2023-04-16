import json

from bs4 import BeautifulSoup

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


def string_to_num(str):
    try:
        return float(str.strip().replace(',', '').replace('%', ''))
    except ValueError:
        return str
    except TypeError:
        return str


# Setting additional request headers
# headers = requests.utils.default_headers()
# headers.update({
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#     "Host": "https://google.com",
#     "Referer": "https://www.google.com/",
#     "Sec-Ch-Ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
#     "Sec-Ch-Ua-Mobile": "?0",
#     "Sec-Ch-Ua-Platform": "\"macOS\"",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
#     "X-Amzn-Trace-Id": "Root=1-643171c8-490e89e074579f273d7202ce"
# })

URL = 'https://in.investing.com/equities/larsen-toubro-infotech-ltd-historical-data?end_date=1681671410&st_date=-1070343000'

# Initialize the WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# driver = webdriver.Chrome(
#     executable_path='./chromedriver.exe', options=options)
# driver.get(URL)
# element_present = EC.presence_of_element_located((By.TAG_NAME, 'table'))
# WebDriverWait(driver, 100).until(element_present)
# html = driver.page_source
# driver.quit()


# Soup Created
with open('./investing.html', 'r') as html:
    soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', class_='common-table medium js-table')
rows = table.find_all('tr', class_='common-table-item u-clickable')

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
    cols = row.find_all('td')
    historical_data["date"].append(cols[0].text.strip())
    historical_data["price"].append(string_to_num(cols[1].text))
    historical_data["open"].append(string_to_num(cols[2].text))
    historical_data["high"].append(string_to_num(cols[3].text))
    historical_data["low"].append(string_to_num(cols[4].text))
    historical_data["volume"].append(string_to_num(cols[5].text))
    historical_data["change"].append(string_to_num(cols[6].text))

with open('./historical_data.json', 'w') as fp:
    json.dump(historical_data, fp)

# new_var = table.findChildren('tr', recursive=False)
