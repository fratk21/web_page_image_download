from urllib.request import Request
import requests
from bs4 import BeautifulSoup
import os

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    requ = requests.get(url)
    soup = BeautifulSoup(requ.text, 'html.parser')
    images = soup.find_all('img',attrs={'class':'lozad'})
    for image in images:
        name = image['alt']
        link = "https://wallpapers.com/search" + image['data-src']       
        print(image['data-src'])
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)

imagedown('https://wallpapers.com/search/couple', 'couple')