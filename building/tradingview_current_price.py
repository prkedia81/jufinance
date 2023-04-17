from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://in.tradingview.com/symbols/NSE-ITC/'

# Initialize the WebDriver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(
    executable_path='./chromedriver.exe', options=options)
driver.get(URL)
element_selector = '#js-category-content > div.tv-category-symbol-header > div.js-symbol-page-header-root > div > div > div > div.quotesRow-pAUXADuj > div:nth-child(1) > div > div.lastContainer-JWoJqCpY > span.last-JWoJqCpY.js-symbol-last > span'
element_present = EC.presence_of_element_located(
    (By.CSS_SELECTOR, element_selector))
WebDriverWait(driver, 100).until(element_present)
element = driver.find_element(By.CSS_SELECTOR, element_selector)

current_price = element.text
print(current_price)
driver.quit()
