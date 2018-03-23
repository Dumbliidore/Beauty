# -*-coding:utf-8-*-

import random
from Mycrawl.settings import UAPOOL
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class MyUAmid(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        Myua = random.choice(UAPOOL)
        print('当前使用的User-Agent是%s'%Myua)
        request.headers.setdefault('User-Agent', Myua)
