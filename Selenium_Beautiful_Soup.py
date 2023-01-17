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

driver.get("https://www.python.org/")

html = driver.page_source

#driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

#card_titles1 = driver.find_elements(By.CSS_SELECTOR, "div.shrubbery ul.menu li a")

#card_prices1 = driver.find_element(By.CSS_SELECTOR, "s.ItemCard__price")
# card_titles2 = driver.find_elements(By.CLASS_NAME, "ItemCard__title my-1")


driver.quit()

soup = BeautifulSoup(html,"html.parser")

menu = soup.find("div", class_="blog-widget")

links = menu.find_all("a")

for a in links:
    print(a.get_text())


#print(card_titles1.text)
#print(card_prices1.text)
# print(card_titles2)


# page = response.text

# soup = BeautifulSoup(page,"html.parser")

# paragraphs = soup.find_all("p", class_="ItemCard__title my-1")
# spans = soup.find_all("span", class_="ItemCard__price ItemCard__price--bold")

# print(paragraphs)
# print(spans)
# print(soup.prettify())

#<button id="onetrust-accept-btn-handler">Confirm suggested preferences</button>

#<span _ngcontent-wyh-c104="" class="ng-star-inserted">Regístrate o inicia sesión</span>


#<img _ngcontent-vsk-c104="" src="/assets/images/logo-wallapop-home-v2.svg" alt="Wallapop logo" class="topbar-logo-icon--full">