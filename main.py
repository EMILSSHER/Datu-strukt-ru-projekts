import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url="https://www.ss.com/lv/transport/cars/"

print("ievadiet marku")
marka = input().strip().title()
if marka == "Bmw":
    marka = "BMW"
    print("ievadiet modeli ievērojot atstarpes un garumzīmes")
    modelis = input().title()
else:
    print("ievadiet modeli")
    modelis = input().strip().title()
    print("ievadiet max tilpumu")
    max_tilpums = input()
    print("ievadiet min tilpumu")
    min_tilpums = input()
    print("ievadiet gadu no")
    min_gads = input()
    print("ievadiet gadu līdz")
    max_gads = input()

driver.get(url)
find = driver.find_element(By.LINK_TEXT, marka) # atrod marku pec teksta
find.click()
time.sleep(2)

dropdowns = driver.find_elements(By.CLASS_NAME, 'filter_sel')
modelis_drop = Select(dropdowns[11]) # modelim nav koda vai id tadel atrod modeli pec dropdown indeksa
time.sleep(1)
modelis_drop.select_by_visible_text(modelis)
time.sleep(2.5)

min_tilp_drop = Select(driver.find_element(By.NAME, 'topt[15][min]'))
time.sleep(1)
min_tilp_drop.select_by_visible_text(min_tilpums)
time.sleep(1.1)
max_tilp_drop = Select(driver.find_element(By.NAME, 'topt[15][max]')) # atrod min un max laukus
time.sleep(1.3)
max_tilp_drop.select_by_visible_text(max_tilpums)
time.sleep(1.2)

min_gads_drop = Select(driver.find_element(By.NAME, 'topt[18][min]'))
time.sleep(0.7)
min_gads_drop.select_by_visible_text(min_gads)
time.sleep(0.8)
max_gads_drop = Select(driver.find_element(By.NAME, 'topt[18][max]'))
time.sleep(1.1)
max_gads_drop.select_by_visible_text(max_gads)
time.sleep(1.5)
