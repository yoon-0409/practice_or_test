
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyautogui 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import clipboard
# from selenium.webdriver.common.by import select
shi_do_list = {'서울':'서울특별시','부산':'부산광역시','대구':'대구광역시','인천':'인천광역시','광주':'광주광역시','대전':'대전광역시','울산':'울산광역시','세종':'세종특별자치도','경기':'경기도','강원':'강원도','충북':'충청북도','충남':'충청남도','전북':'전라북도','전남':'전라남도','경북':'경상북도','경남':'경상남도','제주':'제주특별자치도'}
#딕셔너리 형으로 해둠 엑셀 나오는게 경북 이런식이길래
#이제 주소를 리스트에 담아서 이차원 배열로 담을거임
# adr1 = '경북 포항시 북구 장성동'
# adr2 = '경북 포항시 북구 흥해읍 이안리 424'
# adr3 = '경북 경주시 북구 성건동 631-18'
# adr1 = adr1.split(' ')
# adr2 = adr2.split(' ')
# adr3 = adr3.split(' ')
# address = []
# address.append(adr1)
# address.append(adr2)
# address.append(adr3)
#[['경북', '포항시', '북구', '장성동', '1455-1'], ['경북', '포항시', '북구', '흥해읍', '이안리', '424'], ['경북', '경주시', '북구', '성건동', '631-18']]

# for i in address:
#     if i[0] in shi_do_list:
#         print(shi_do_list[i[0]])
# 경상북도
# 경상북도
# 경상북도
# 이런식으로 가능해질것
# select.select_by_value(shi_dolist[i[0]])
# 이렇게 시나리오가 흐르면 되겠죠?
# 까지 기억해두고 감
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
#입력창 진입 -----------------------
# driver.find_element(By.XPATH,'').click()

iframe = driver.find_element(By.XPATH,'/html/body/div[3]/iframe') #팝업 창 스위치
driver.switch_to.frame(iframe)
# data = driver.page_source
# soup = BeautifulSoup(data,'html.parser')
select = Select(driver.find_element(By.XPATH,'//*[@id="sel_regt_name"]'))
select.select_by_value('1717') #대구법원 포항등기소
driver.find_element(By.XPATH,'//*[@id="id_chk_rel_regt"]').click() #타관할
select = Select(driver.find_element(By.XPATH,'//*[@id="real_gubun"]/table/tbody/tr/td/select[2]'))
select.select_by_value('경기도')
# time.sleep(5)
# pyautogui.press(['tab','tab','tab','tab','tab','tab','tab','tab','tab','enter','enter'])
pyautogui.press(['tab','tab'])
clipboard.copy('정자동') 
pyautogui.hotkey('ctrl', 'v')
# pyautogui.typewrite('대도동', interval=0.25)
driver.find_element(By.XPATH,'//*[@id="id_txt_lot_no"]').send_keys(215)
# pyautogui.typewrite('215', interval=0.25)
driver.find_element(By.XPATH,'//*[@id="content1"]/div[2]/button[1]').click() #입력
time.sleep(5)
data = driver.page_source
soup = BeautifulSoup(data,'html.parser')
tabindex = soup.select('#Image')
print(tabindex)
# pyautogui.press('tab')
# pyautogui.press('enter')
# driver.find_element(By.XPATH,'//*[@id="id_txt_lot_no"]').send_keys('101-17')
print('done')
time.sleep(10)


adr1 = '경북 포항시 북구 장성동'
adr2 = '경북 포항시 북구 흥해읍 이안리 424'
adr3 = '경북 경주시 북구 성건동 631-18'
adr1 = adr1.split(' ')
adr2 = adr2.split(' ')
adr3 = adr3.split(' ')
address = []
address.append(adr1)
address.append(adr2)
address.append(adr3)

if i in address:
    if i in shi_do_list:
        print(i)