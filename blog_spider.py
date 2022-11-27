# -*- coding: utf-8 -*-
# @Time : 2022-11-28 0:01
# @Author : ZZZZZHHHHH
# @FileName: blog_spider.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup

urls =[
    f"https://www.cnblogs.com/#p{page}" for page in range(1, 1000)
]

def craw(url):
    r = requests.get(url)
    return r.text
    # print(url, len(r.text))


def parse(html):
    # class="post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.text) for link in links]


if __name__ == '__main__':
    for result in parse(craw(urls[2])):
        print(result)