'''
author: BlueMrD
time: 2018\3\22
CSDN: https://blog.csdn.net/Mr_blueD/article/list
wechat: PiscesDZH
'''


# -*- coding: utf-8 -*-


# urllib模块
import urllib.request
import os
import re
import time

def url_open(url):
    # 创建一个 Request对象 req
    req = urllib.request.Request(url)

    # 通过 add_header( )方法添加请求头，防止基本的网站反爬策略
    req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/\
                    537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")

    # 将获取的网页信息通过read()方法读取出来
    response = urllib.request.urlopen(req).read()
    return response

# 另一种方法获取网页
'''
def url_open(url):
    req = urllib.request.Request(url)
    header = ('User-Agent', "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/\
                    537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    )
    # 创建opner对象
    opener = urllib.request.build_opener()

    # 给该对象添加请求头
    opener.addheaders = [header]

    # 用open方法获取网页并读取
    response = opener.open(url).read()
    return response
'''

def find_imgs(url):
    # 将网页内容进行解码，网页编码是GBK，就换成gbk
    html = url_open(url).decode('utf-8')

    # 使用正则表达式获取目标数据
    p = r'<img src="([^"]+\.jpg)"'
    img_addrs = re.findall(p, html)

    return img_addrs

def download_mm(folder='OOXX'):
    os.mkdir(folder)
    os.chdir(folder)

    page_num = 1  # 设置为从第一页开始爬取，可以自己改
    x = 0  # 自命名图片
    img_addrs = []  # 防止图片重复

    # 只爬取前两页的图片，可改，同时给图片重命名
    while page_num <= 2:
        page_url = url + 'a/more_' + str(page_num) + '.html'
        addrs = find_imgs(page_url)
        print(len(addrs))
        # img_addrs = []
        for i in addrs:
            if i in img_addrs:
                continue
            else:
                img_addrs.append(i)
        print(len(img_addrs))
        for each in img_addrs:
            print(each)
        page_num += 1
        time.sleep()
        # x = (len(2img_addrs)+1)*(page_num-1)
    for each in img_addrs:
        filename = str(x) + '.' + each.split('.')[-1]
        x += 1
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)
        # page_num += 1

if __name__ == '__main__':
    url = 'http://www.meizitu.com/'
    download_mm()






# requests模块
import requests
import os
import re
import time


def url_open(url):

    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
    }  # 以字典的形式添加请求头

    response = requests.get(url, headers=header)  # 使用get方法发送请求获取网页源码
    return response


def find_imgs(url):

    html = url_open(url).text
    p = r'<img src="([^"]+\.jpg)"' # 正则获取图片地址
    img_addrs = re.findall(p, html)

    return img_addrs


def download_mm(url, folder='OOXX'):
    os.mkdir(folder)
    os.chdir(folder)
    page_num = 1  # 设置为从第一页开始爬取，可以自己改
    x = 0  # 自命名图片
    img_addrs = []  # 防止图片重复

    # 只爬取前两页的图片，可改，同时给图片重命名
    while page_num <= 2:
        page_url = url + 'a/more_' + str(page_num) + '.html'
        addrs = find_imgs(page_url)
        # print(len(addrs))

        for i in addrs:
            if i in img_addrs:
                continue
            else:
                img_addrs.append(i)
        '''
        print(len(img_addrs))
        for each in img_addrs:
            print(each)
        '''

    for each in img_addrs:
        filename = str(x) + '.' + each.split('.')[-1]
        x += 1
        with open(filename, 'wb') as f:
            img = url_open(each).content
            f.write(img)



if __name__ == '__main__':
    url = 'http://www.meizitu.com/'
    download_mm(url)