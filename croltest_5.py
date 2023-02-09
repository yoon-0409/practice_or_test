
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyautogui 
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import select
url = "https://idexuae.ae/exhibit/exhibitor-list/"


driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
time.sleep(7)
# driver.switch_to.frame("iframeResult")
data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')
print(soup)
f = open("html.txt", "w" , encoding='mbcs')
f.write(soup)
f.close
driver.find_element(By.XPATH,'//*[@id="app"]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[3]/div/div/div[1]/div/div[1]/div[3]/a[1]').click

print('click')
time.sleep(5)