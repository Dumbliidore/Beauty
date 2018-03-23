# -*-coding:utf-8-*-

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from Mycrawl.items import GupiaoItem
import requests



class MovieSpider(Spider):
    # 爬虫名字，重要
    name = 'gupiao2'
    # 反爬措施
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    # url = 'https://movie.douban.com/top250'
    allow_domains = ['quotes.money.163.com']
    start_urls = ['http://quotes.money.163.com/hkstock/cwsj_00700.html']

    '''
    def start_requests(self):
        # url = 'https://movie.douban.com/top250'
        yield Request(self.url, headers=self.headers, callback=self.parse)
    '''

    def parse(self, response):
        item = GupiaoItem()
        selector = Selector(response)
        datas1 = selector.xpath('//table[@class="mod-table2 column"]')
        contents = selector.xpath('//table[@class="mod-table2 thWidth205"]')
        content1 = contents[2].xpath('tbody/tr/td[1]/div')
        content2 = contents[2].xpath('tbody/tr/td[2]/div')
        content3 = contents[2].xpath('tbody/tr/td[3]/div')
        data = datas1[2].xpath('tr/td')
        for i, each in enumerate(data):
            name = each.xpath('text()').extract()
            frist = content1.xpath('text()').extract()
            second = content2.xpath('text()').extract()
            thrid = content3.xpath('text()').extract()
            item['dataname'] = name[0]
            item['fristdata'] = frist[0]
            item['secondata'] = second[0]
            item['thridata'] = thrid[0]

            yield item
        '''
        nextpage = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextpage:
            nextpage = nextpage[0]

            yield Request(self.url+str(nextpage), headers=self.headers, callback=self.parse)
        '''
