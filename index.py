from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import lxml 
import csv
import time
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36' ) 
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(  options=options)
 
 
driver.get("https://www.nseindia.com")

market_data =  driver.find_element(By.ID,"link_2")
ActionChains(driver).move_to_element(market_data).perform()

pre_open_market = driver.find_element(By.XPATH,'//*[@id="main_navbar"]/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a')
pre_open_market.click()

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')
data = [] 
 
final_prices = soup.find("tbody" ).findAll('tr') 
for  each in final_prices:
    name = each.findAll('td')[1].text
    price = each.findAll('td')[6].text
    item = [name,price]
    data.append(item)
    
column_names = ['name', 'price']
df = pd.DataFrame(data,columns=column_names)

    
     
 
seconds = time.time()
local_time = str(time.ctime(seconds)).replace(":", "-")  # Replacing ':' with '-' for valid filename
df.to_csv('nseindia ' + local_time+'.csv')

driver.get("https://www.nseindia.com")
niftyBank =  driver.find_element('id',"NIFTY BANK")
niftyBank.click()
time.sleep(1)
element = driver.find_element(By.TAG_NAME, "body")

element.send_keys( Keys.PAGE_DOWN)
time.sleep(1)
viewAll =  driver.find_element(By.LINK_TEXT,"View All")
viewAll.click()
time.sleep(2)
selector = driver.find_element(By.ID,'equitieStockSelect')
selector.click()
time.sleep(2)
selector.send_keys(Keys.CONTROL + Keys.END)
time.sleep(2)
selector = driver.find_element(By.ID,'equitieStockSelect')
selector.click()
alpha50 = driver.find_element(By.XPATH,'//*[contains(text(), "NIFTY ALPHA 50")]')
alpha50.click()

time.sleep(2)

driver.quit()

 