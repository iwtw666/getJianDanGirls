import requests
import os
from bs4 import BeautifulSoup
import re


def get_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    img_arr = soup.find_all('img')
    try:
        next_page = 'https:' + soup.find('a', class_='previous-comment-page')['href'].split('#')[0]
    except:
        next_page = ''

    download_jpg(img_arr, next_page)


def download_jpg(images, next_html=''):
    for img in images:
        img_url = 'https:' + img['src']
        img_name = img['src'].split('/')[-1]
        img_extension = img_url[-3:]
        if img_extension.lower() != 'jpg' and img_extension.lower() != 'png':
            continue
        save_name = 'photos/{}'.format(img_name)
        img_info = requests.get(img_url).content
        create_folder(save_name)
        with open(save_name, 'wb') as f:
            f.write(img_info)
        print(img_name)
    if len(next_html):
        get_url(next_html)


def create_folder(folder_name):
    path = os.path.split(folder_name)[0]
    if path != '' and not os.path.exists(path):
        os.makedirs(path)


def start():
    url1 = "https://jandan.net/girl"
    get_url(url1)


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(e)
    finally:
        print('end\n')
