from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

 
import csv
import time

 
driver = webdriver.Chrome( )

# Зайти на сайт
driver.get("https://www.nseindia.com")

# Наведение курсора на MARKET DATA
market_data = driver.find_element_by_xpath("//a[@title='MARKET DATA']")
ActionChains(driver).move_to_element(market_data).perform()

# Клик на Pre-Open Market
pre_open_market = driver.find_element_by_xpath("//a[@title='Pre-Open Market']")
pre_open_market.click()

# Пауза для загрузки данных
time.sleep(5)

# Спарсить данные Final Price
final_prices = driver.find_elements_by_xpath("//td[@class='number finalprice']")
data = [(item.text,) for item in final_prices]

# Закрыть браузер
driver.quit()

# Запись данных в CSV файл
with open('pre_open_market_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Final Price'])
    writer.writerows(data)
