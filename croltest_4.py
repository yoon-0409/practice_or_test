
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
url = "https://auth.danawa.com/login?url=https%3A%2F%2Fwww.danawa.com%2F%3Fsrc%3Dadwords%26kw%3DGA0000020%26gclid%3DCj0KCQjwtb_bBRCFARIsAO5fVvHiMT12s8TWgA6HQTOn3F4AvKuwOP55bI2TV0ZNXhsg2kxTq3KRFl8aAgrFEALw_wcB"


driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
time.sleep(2)
# driver.switch_to.frame("iframeResult")
data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')
driver.find_element(By.XPATH,'//*[@id="danawa-member-login-input-id"]').send_keys('12345')
driver.find_element(By.XPATH,'//*[@id="danawa-member-login-input-pwd"]').send_keys('a1b2c3')
driver.find_element(By.XPATH,'//*[@id="danawa-member-login-loginButton"]').click()
time.sleep(5)

# select.select_by_value('')
# select.find_element("class","btn_log4").click() 