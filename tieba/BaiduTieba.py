
'''
author: BlueMrD
time: 2018\3\22
CSDN: https://blog.csdn.net/Mr_blueD/article/list
wechat: PiscesDZH
'''


# -*-coding:utf-8 -*-


# urllib模块
import urllib.request
import re
import os

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    response = urllib.request.urlopen(req).read()

    return response

def find_img(url):
    html = open_url(url).decode('utf-8')
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    img_addrs = re.findall(p, html)

    for each in img_addrs:
        print(each)
    for each in img_addrs:
        file = each.split("/")[-1]
        with open(file, "wb") as f:
            img = open_url(each)
            f.write(img)

def get_img():
    os.mkdir("TieBaTu")
    os.chdir("TieBaTu")
    find_img(url)

if __name__ == "__main__":
    url = 'https://tieba.baidu.com/p/5085123197'
    get_img()




#  requests模块
import requests
import re
import os


def open_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url, headers=headers)
    return response


def find_img(url):
    html = open_url(url).text
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    img_addrs = re.findall(p, html)
    for each in img_addrs:
        print(each)
    for each in img_addrs:
        file = each.split("/")[-1]
        with open(file, "wb") as f:
            img = open_url(each).content
            f.write(img)


def get_img():
    os.mkdir("TieBaTu")
    os.chdir("TieBaTu")
    find_img(url)


if __name__ == "__main__":
    url = 'https://tieba.baidu.com/p/5085123197'
    get_img()