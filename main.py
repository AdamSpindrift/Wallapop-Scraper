from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://es.wallapop.com/app/search?category_ids=12900&keywords=nintendo&latitude=41.38804&longitude=2.17001&filters_source=quick_filters&object_type_ids=10088")

driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

html = driver.page_source

time.sleep(10)
driver.quit()

soup = BeautifulSoup(html,"html.parser")

items = soup.find_all("div", class_="ItemCard__data--with-description")
price = soup.find_all("span", class_="ItemCard__price--bold")
description = soup.find_all("p", class_="ItemCard__title")
img = soup.find_all("img",class_="ng-star-inserted")


extracted_prices = []
extracted_descriptions = []
extracted_img = []
extracted_items = []


for p in price:
    extracted_prices.append(p.get_text())
    
for d in description:
    extracted_descriptions.append(d.get_text())
    
for s in img:
    extracted_img.append(s["src"])
    

time.sleep(5)


for idx, i in enumerate(extracted_prices):
    p = i
    d = extracted_descriptions[idx]
    image_url = extracted_img[idx]
    b = {
        "description":d,
        "price":p,
        "img":image_url,}
    
    extracted_items.append(b.copy())
    
time.sleep(5)
    
print(extracted_items)



