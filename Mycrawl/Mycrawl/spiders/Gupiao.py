# -*-coding:utf-8-*-


from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from Mycrawl.items import GupiaoItem


class MovieSpider(Spider):
    # 爬虫名字，重要
    name = 'gupiao'
    allow_domains = ['quotes.money.163.com']
    start_urls = ['http://quotes.money.163.com/hkstock/cwsj_00700.html']


    def parse(self, response):

        item = GupiaoItem()
        selector = Selector(response)
        datas = selector.xpath('//table[@class="mod-table2 column"]')
        contents = selector.xpath('//table[@class="mod-table2 thWidth205"]')
        titles = selector.xpath('//div[@class="titlebar3"]/span/text()').extract()
        # 共四张表，i 从 0 开始
        for i, each1 in enumerate(contents):
            # 第 i+1 张表的第二列所有数据
            content1 = each1.xpath('tbody/tr/td[1]/div')
            # 第 i+1 张表的第三列所有数据
            content2 = each1.xpath('tbody/tr/td[2]/div')
            # 第 i+1 张表的第四列所有数据
            content3 = each1.xpath('tbody/tr/td[3]/div')
            # 第 i+1 张表的第一列所有数据
            data = datas[i].xpath('tr/td')

            for j, each2 in enumerate(data):
                name = each2.xpath('text()').extract()
                frist = content1[j].xpath('text()').extract()
                second = content2[j].xpath('text()').extract()
                thrid = content3[j].xpath('text()').extract()
                item['title'] = titles[i]
                item['dataname'] = name[0]
                item['fristdata'] = frist[0]
                item['secondata'] = second[0]
                item['thridata'] = thrid[0]

                yield item

