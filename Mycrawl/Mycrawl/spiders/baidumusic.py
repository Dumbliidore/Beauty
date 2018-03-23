# -*-coding:utf-8-*-

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from Mycrawl.items import MusicItem
import requests



class MusicSpider(Spider):
    # 爬虫名字，重要
    name = 'music'
    # 反爬措施
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    # url = 'https://movie.douban.com/top250'
    allow_domains = ['music.baidu.com']
    start_urls = ['http://music.baidu.com/']

    '''
    def start_requests(self):
        # url = 'https://movie.douban.com/top250'
        yield Request(self.url, headers=self.headers, callback=self.parse)
    '''

    def parse(self, response):
        item = MusicItem()
        selector = Selector(response)
        title = selector.xpath('//div[@class="hd"]/h2[@class="title"]/text()').extract()
        musics = selector.xpath('//div[@class="bd"]/ul[@class="song-list"]/li')
        for i,music in enumerate(musics):
            top = music.xpath('div[@class="index"]/text()').extract()
            name = music.xpath('div[@class="song-info"]/div[@class="info"]/div[@class="song"]/a/@title').extract()
            songer = music.xpath('div[@class="song-info"]/div[@class="info"]/div[@class="song"]\
                                 /span[@class="artist"]/span/@title').extract()
            if songer == []:
                songer = music.xpath('div[@class="song-info"]/div[@class="info"]/div[@class="song"]/\
                                     span[@class="artist"]/''span[@class="author_list"]/a/@title').extract()
            item['top'] = title[i//10] + top[0]
            item['music_name'] = '《' + name[0] + '》'
            if songer:
                item['songer'] = songer[0]
            else:
                item['songer'] = ''
            yield item