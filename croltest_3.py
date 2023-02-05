
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyautogui 
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import select
url = "http://www.iros.go.kr/re1/intro.jsp?smsgubun=N&sysid=PL"


driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
time.sleep(2)
# driver.switch_to.frame("iframeResult")
data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')
driver.find_element(By.XPATH,'//*[@id="user_id"]').send_keys('adsads32')
pyautogui.press('tab')
time.sleep(1)
# pyautogui.press('q')
# pyautogui.press('m')
# pyautogui.press('7')
# pyautogui.press('4')
# pyautogui.press('5')
# pyautogui.press('8')
# pyautogui.press('p')
# pyautogui.press('s')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('qm7458ps@')
driver.find_element(By.XPATH,'//*[@id="content2"]/div[1]/form/div[2]/div/div[1]/a/img').click() #로그인
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="cenS"]/div[2]/ul/li[1]/div/ul/li[4]/a/span/img').click() #통합전자등기
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="id_wrt_cs_inq_area"]/div[3]/button[1]').click() #신규작성
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="sel_rgs_type"]').click()
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="id_btn_real_input"]').click()
time.sleep(30)

# select.select_by_value('')
# select.find_element("class","btn_log4").click()
