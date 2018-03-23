# -*-coding:utf-8-*-

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from Mycrawl.items import BookItem
import requests
import random


class BookSpider(Spider):
    # 爬虫名字，重要
    name = 'book'
    # 反爬措施
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    # url = "https://www.qidian.com/rank/yuepiao?style=1"
    allow_domains = ['qidian.com']
    start_urls = ["https://www.qidian.com/rank/yuepiao?style=1"]

    '''
    def start_requests(self):
        # url = "https://www.qidian.com/rank/yuepiao?style=1"
        yield Request(self.url, headers=self.headers, callback=self.parse)
    '''

    def parse(self, response):
        item = BookItem()
        selector = Selector(response)
        books = selector.xpath('//div[@class="book-mid-info"]')
        for book in books:
            name = book.xpath('h4/a/text()').extract()
            author = book.xpath('p[@class="author"]/a[@class="name"]/text()').extract()
            type = book.xpath('p[@class="author"]/a[@data-eid="qd_C42"]/text()').extract()
            state = book.xpath('p[@class="author"]/span/text()').extract()
            intro = book.xpath('p[@class="intro"]/text()').extract()
            update = book.xpath('p[@class="update"]/a[@target="_blank"]/text()').extract()
            href = book.xpath('p[@class="update"]/a/@href').extract()
            _time = book.xpath('p[@class="update"]/span/text()').extract()

            item['book_name'] = name[0]
            item['author'] = author[0]
            item['book_type'] = type[0]
            item['book_state'] = state[0]
            item['book_update'] = update[0]
            item['book_time'] = _time[0]
            item['new_href'] = 'https:' + href[0]
            item['book_intro'] = ''.join(intro).replace(' ','').replace('\n','')
            yield item

        # time.sleep(3)
        '''
        i = 2
        while i <= 25:
            nexturl = self.url + '&page=' + str(i)
            # yield Request(nexturl, headers=self.headers, callback=self.parse)
            yield Request(nexturl, callback=self.parse)
            i += 1
        '''
