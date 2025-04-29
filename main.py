import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
print("ievadiet marku")
marka = input()
print("ievadiet modeli")
modelis = input()
print("ievadiet tilpumu")
tilpums = input()
print("ievadiet gadu")
gads = input()
url="https://www.ss.com/lv/transport/cars/"
driver.get(url)
time.sleep(2)
find = driver.find_element(By.LINK_TEXT, marka)
find.click()
time.sleep(2)

input()
