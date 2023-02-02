from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from PIL import Image
from urllib.parse import quote_plus
import requests
for i in range(11):
    url = "https://cloudinary.images-iherb.com/image/upload/f_auto,q_auto:eco/images/now/now04014/v/52.jpg"
    img_data = requests.get(url).content
    with open(f'files/img{i+1}' + '.jpg', 'wb') as handler:
        handler.write(img_data)