from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from telegram_bot import send_telegram
from dotenv.main import load_dotenv
import os

load_dotenv()

# Telegram Environment Variables
token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["CHAT_ID"]

def wallapopScrape(url):
    

    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(20)

    try:
        
        driver.get(url)

        driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,"#btn-load-more > button").click()
        
    except(Exception):
        print("An error occurred loading the web page")
        send_telegram(token,chat_id,"An error occurred loading the web page")
        return([])
        
    finally:
        
        time.sleep(5)

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

        return(extracted_items)