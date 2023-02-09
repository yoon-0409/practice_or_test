
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyautogui 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import clipboard
# from selenium.webdriver.common.by import select
url = "http://www.iros.go.kr/re1/intro.jsp?smsgubun=N&sysid=PL"


driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
time.sleep(5)
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
time.sleep(10)
main = driver.window_handles
print(main)
time.sleep(2)
for i in main:
    if i != main[0]:
        driver.switch_to.window(i)
        driver.close()
        print(i)
        time.sleep(0.5)
time.sleep(1)
driver.switch_to.window(main[0])
driver.find_element(By.XPATH,'//*[@id="cenS"]/div[2]/ul/li[1]/div/ul/li[4]/a/span/img').click() #통합전자등기
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="id_wrt_cs_inq_area"]/div[3]/button[1]').click() #신규작성
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="sel_rgs_type"]').click()
pyautogui.press('down')
pyautogui.press('enter') 
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="id_btn_real_input"]').click()
time.sleep(5)
# driver.find_element(By.XPATH,'').click()
pyautogui.press('tab','tab','down','down','enter','enter')
pyautogui.press(['tab','tab','tab','tab','tab'])
pyautogui.press('tab')
clipboard.copy('대도동') 
pyautogui.hotkey('ctrl', 'v')
# pyautogui.typewrite('대도동', interval=0.25)
pyautogui.press('tab')
pyautogui.typewrite('101-17', interval=0.25)
# driver.find_element(By.XPATH,'//*[@id="id_txt_lot_no"]').send_keys('101-17')

print('done')

# driver.find_element(By.XPATH,'//*[@id="id_txt_admin_regn3"]').send_keys('대도동')
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="id_txt_lot_no"]').send_keys('101-17')


time.sleep(10)
# select[2].
# select.select_by_index(3)
# driver.find_element(By.XPATH,'//*[@id="sel_regt_name"]/option[3]')


# select.select_by_value('')
# select.find_element("class","btn_log4").click()
# //*[@id="app"]/div/main/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[3]/div/div/div[2]/div/div[1]/div[3]/a[1]
# app > div > main > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div > div > div:nth-child(2) > div > div:nth-child(5) > div > div > div:nth-child(2) > div > div.layout.d-flex.flex-column.flex-grow-1 > div.grey.p-2.lighten-5.px-2 > a:nth-child(1)
# app > div > main > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div > div > div:nth-child(2) > div > div:nth-child(5) > div > div > div:nth-child(1) > div > div.layout.d-flex.flex-column.flex-grow-1 > div.grey.p-2.lighten-5.px-2 > a:nth-child(1)
# [<selenium.webdriver.remote.webelement.WebElement (session="30838640d98c54aa1716fcbff02ea817", element="83d3e39b-c04a-44bc-a203-ccb0924c79db")>, 
#  <selenium.webdriver.remote.webelement.WebElement (session="30838640d98c54aa1716fcbff02ea817", element="0501ecf3-b185-498d-9ff0-7b2f1e01150b")>, 
#  <selenium.webdriver.remote.webelement.WebElement (session="30838640d98c54aa1716fcbff02ea817", element="33bc87d5-12ad-4295-82d1-99b5decb959b")>, 
#  <selenium.webdriver.remote.webelement.WebElement (session="30838640d98c54aa1716fcbff02ea817", element="8a6ecd19-11db-4517-88d5-09c207458fa3")>, 
#  <selenium.webdriver.remote.webelement.WebElement (session="30838640d98c54aa1716fcbff02ea817", element="48e9a072-fd55-4658-bd22-4802ae716bee")>, 
#  <selenium.webdriver.remote.webelement.WebElement (session="30838640d98c54aa1716fcbff02ea817", element="a984265f-0877-4e90-8f91-7e7e98ac4930")>]