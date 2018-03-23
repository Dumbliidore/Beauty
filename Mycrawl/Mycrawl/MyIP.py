# -*-coding:utf-8-*-

import random
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
import requests
# from selenium import webdriver
from bs4 import BeautifulSoup
# import time
# import telnetlib


class Myip(HttpProxyMiddleware):

    def process_response(self, request, response, spider):
        if response.status != 200:
            Myip = random.choice(self.find_ip())
            print('当前使用的ip是%s' % Myip)
            request.meta['proxy'] = 'http://' + Myip
            return request
        return response

    def process_request(self, request, spider):
        Myip = random.choice(self.find_ip())
        print('当前使用的ip是%s'% Myip)
        request.meta['proxy'] = 'http://'+Myip

    def find_ip(self):
        url = random.choice(['http://www.xicidaili.com/nn/','https://www.kuaidaili.com/free/'])
        headers = {'User-Agent':
                'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
                   }
        response = requests.get(url, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        ip_content = soup.findAll('tr')
        myip = []
        for x in range(1, len(ip_content)):
            ip = ip_content[x]
            tds = ip.findAll("td")
            if url == 'http://www.xicidaili.com/nn/':
                ip_temp = tds[1].contents[0] + ":" + tds[2].contents[0]
            else:
                ip_temp = tds[0].contents[0] + ":" + tds[1].contents[0]
            try:
                requests.get('http://www.baidu.com', proxies={'http':'http//'+ip_temp})
            except:
                print('failed')
            else:
                myip.append(ip_temp)
            if len(myip) > 5:
                break
        return myip
