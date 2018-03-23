# -*-coding:utf-8-*-

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from Mycrawl.items import MovieItem
import requests



class MovieSpider(Spider):
    # 爬虫名字，重要
    name = 'movie'
    # 反爬措施
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    # url = 'https://movie.douban.com/top250'
    allow_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    '''
    def start_requests(self):
        # url = 'https://movie.douban.com/top250'
        yield Request(self.url, headers=self.headers, callback=self.parse)
    '''

    def parse(self, response):
        item = MovieItem()
        selector = Selector(response)
        movies = selector.xpath('//div[@class="info"]')
        for movie in movies:
            name = movie.xpath('div[@class="hd"]/a/span/text()').extract()
            message = movie.xpath('div[@class="bd"]/p/text()').extract()
            star = movie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            number = movie.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()
            quote = movie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['movie_name'] = ''.join(name)
            item['movie_message'] = ';'.join(message).replace(' ','').replace('\n','')
            item['movie_star'] = star[0]
            item['number'] = number[1].split('人')[0]
            item['movie_quote'] = quote
            yield item
        '''
        nextpage = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextpage:
            nextpage = nextpage[0]

            yield Request(self.url+str(nextpage), headers=self.headers, callback=self.parse)
        '''
