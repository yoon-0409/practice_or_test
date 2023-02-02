from urllib.request import urlopen
from urllib.error import HTTPError
from selenium import webdriver
from urllib.error import URLError
import cv2
from bs4 import BeautifulSoup
import urllib.request
import requests
import time
url = 'https://kr.iherb.com/pr/now-foods-panax-ginseng-extract-250-veg-capsules/717'
# header = {"User-Agent": "나의 User-Agent"}
header = {"User-Agent" : "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'"}
# response = requests.get(url, headers=header)
response = requests.get(url, headers=header)
print(response.status_code)
# print(response.text)
urllib.request.urlretrieve(url,'C:/Users/USER/Desktop/vscpractice/python_practice/pill.jpg',)
# print(type(response))
if(response.status_code == 200):
    title = url
    # title = soup.select_one('#product-image > div.thumbnail-container > div.thumbnail-item.selected > img')
    print(title)
else:
    print('failed')
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
time.sleep(30)
data = driver.page_source
soup = BeautifulSoup(data, 'html.parser')
title = soup.select('#product-image > div.thumbnail-container > div.thumbnail-item.selected > img')
string = str(title[0])
string = string.split('data-large-img=')
string = string[1].split('height')
string = string[0].replace('"','')
url = string
# urllib.request.urlretrieve(url, "test.jpg")
print(string)
# soup = BeautifulSoup(data, 'html.parser')

# i = int(0)
# for i in range(30):
#     url = f'http://www.neodinvet.co.kr/sub04a.asp?Page={i}&bKind=3&a=4'
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         print(f'http e:{e}')
#         break
#         # null, break 등의 방법 사용
#     except URLError as e:
#         print(f'url e:{e}')
#         break
#     else:
#         print(f'{i}:{html}')
#     i = i+1
    # 프로그램 계속 실행