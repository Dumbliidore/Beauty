# -*-coding:utf-8-*-

from scrapy.spiders import Spider
from scrapy import FormRequest
from scrapy.selector import Selector
from Mycrawl.items import LagouItem

import random
import json
import time


class LagouSpider(Spider):
    # 爬虫名字，重要
    name = 'lagou'
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=1'}
    allow_domains = ['lagou.com']
    url = "https://www.lagou.com/jobs/positionAjax.json?" # &needAddtionalResult=true&isSchoolJob=0"
    page = 1
    allpage = 0

    def start_requests(self):

        yield FormRequest(self.url, headers=self.headers,
                                formdata={
                                    'first': 'false',
                                    'pn': str(self.page),
                                    'kd': 'Python',
                                    'city':'广州'

                                }, callback=self.parse
                              )

    def parse(self, response):
        # print(response.body)
        item = LagouItem()
        data = json.loads(response.body.decode('utf-8'))
        result = data['content']['positionResult']['result']
        totalCount = data['content']['positionResult']['totalCount']
        resultSize = data['content']['positionResult']['resultSize']
        for each in result:
            item['city'] = each['city']
            item['companyFullName'] = each['companyFullName']
            item['companySize'] = each['companySize']
            item['district'] = each['district']
            item['education'] = each['education']
            item['linestaion'] = each['linestaion']
            item['positionName'] = each['positionName']
            item['jobNature'] = each['jobNature']
            item['salary'] = each['salary']
            item['createTime'] = each['createTime']
            item['workYear'] = each['workYear']
            yield item
        time.sleep(random.randint(5, 20))

        if int(resultSize):
            self.allpage = int(totalCount) / int(resultSize) + 1
            if self.page < self.allpage:
                self.page += 1
                yield FormRequest(self.url, headers=self.headers,
                                    formdata={
                                        'first': 'false',
                                        'pn': str(self.page),
                                        'kd': 'Python',
                                        'city':'广州'
                                    }, callback=self.parse
                                  )
