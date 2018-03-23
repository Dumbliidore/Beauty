# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import pymongo

'''
class MycrawlPipeline(object):
    def process_item(self, item, spider):
        return item
'''

'''
class MoviePipeline(object):
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1likePython',
                                    db='TESTDB', charset='utf8')
        # 建立游标对象
        self.cursor = self.conn.cursor()
        self.cursor.execute('truncate table Movie')
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into Movie (name,movieInfo,star,number,quote) \
            VALUES (%s,%s,%s,%s,%s)", (item['movie_name'],item['movie_message'],item['movie_star'],
                                       item['number'], item['movie_quote']))
            self.conn.commit()
        except pymysql.Error:
            print("Error%s,%s,%s,%s,%s" % (item['movie_name'],item['movie_message'],item['movie_star'],
                                       item['number'], item['movie_quote']))
        return item

class BookPipeline(object):
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1likePython',
                                    db='TESTDB', charset='utf8')
        # 建立游标对象
        self.cursor = self.conn.cursor()
        self.cursor.execute('truncate table Book')
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into Book (book_name,author,book_type,book_state,book_update,book_time,new_href,book_intro) \
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (item['book_name'], item['author'], item['book_type'],
                                                   item['book_state'], item['book_update'], item['book_time'],
                                                   item['new_href'], item['book_intro']))
            self.conn.commit()
        except pymysql.Error:
            print("Error%s,%s,%s,%s,%s,%s,%s,%s" % (item['book_name'], item['author'], item['book_type'],
                                                   item['book_state'], item['book_update'], item['book_time'],
                                                   item['new_href'], item['book_intro']))
        return item

'''


# 存入Mysql数据库
class MycrawlPipeline(object):
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1likePython',
                                    db='TESTDB', charset='utf8')
        # 建立游标对象
        self.cursor = self.conn.cursor()
        # 清除表中所有数据，保留表结构。
        # self.cursor.execute('truncate table Movie')
        # self.cursor.execute('truncate table Book')
        # self.cursor.execute('truncate table Music')
        self.conn.commit()

    def process_item(self, item, spider):

        # 爬虫名为movie
        if spider.name == 'movie':
            try:
                self.cursor.execute("insert into Movie (name,movieInfo,star,number,quote) \
                VALUES (%s,%s,%s,%s,%s)", (item['movie_name'],item['movie_message'],item['movie_star'],
                                           item['number'], item['movie_quote']))
                self.conn.commit()
            except pymysql.Error:
                print("Error%s,%s,%s,%s,%s" % (item['movie_name'],item['movie_message'],item['movie_star'],
                                           item['number'], item['movie_quote']))
            return item

        # 爬虫名为book
        elif spider.name == 'book':
            try:
                self.cursor.execute("insert into Book (book_name,author,book_type,book_state,book_update,book_time,new_href,book_intro) \
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (item['book_name'], item['author'], item['book_type'],
                                                            item['book_state'], item['book_update'], item['book_time'],
                                                            item['new_href'], item['book_intro']))
                self.conn.commit()
            except pymysql.Error:
                print("Error%s,%s,%s,%s,%s,%s,%s,%s" % (item['book_name'], item['author'], item['book_type'],
                                                        item['book_state'], item['book_update'], item['book_time'],
                                                        item['new_href'], item['book_intro']))
            return item

        # 爬虫名为music
        elif spider.name == 'music':
            try:
                self.cursor.execute("insert into Music (top,music_name,songer) \
                        VALUES (%s,%s,%s)", (item['top'], item['music_name'], item['songer']))
                self.conn.commit()
            except pymysql.Error:
                print("Error%s,%s,%s" % (item['top'], item['music_name'], item['songer']))

            return item

        elif spider.name == 'maoyan':
            try:
                self.cursor.execute("insert into Maoyan (top,title,star,releasetime) \
                        VALUES (%s,%s,%s,%s)", (item['top'], item['title'], item['star'], item['releasetime']))
                self.conn.commit()
            except pymysql.Error:
                print("Error%s,%s,%s,%s" % (item['top'], item['title'], item['star'], item['releasetime']))
            return item

        # 爬虫名为gupiao
        elif spider.name == 'gupiao':
            try:
                self.cursor.execute("insert into GUPIAO (title, dataname,fristdata,secondata,thridata) \
                        VALUES (%s,%s,%s,%s,%s)", (item['title'], item['dataname'], item['fristdata'], item['secondata'], item['thridata']))
                self.conn.commit()
            except pymysql.Error:
                print("Error%s,%s,%s,%s,%s" % (item['title'], item['dataname'], item['fristdata'], item['secondata'], item['thridata']))
            return item

        # 爬虫名为lagou
        elif spider.name == 'lagou':
            try:
                self.cursor.execute("insert into Lagou (city, companyName, companySize, district, \
                 linestaion, positionName, jobNature, education, salary, workYear, showTime) \
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (item['city'], item['companyFullName'], \
                        item['companySize'], item['district'], item['linestaion'], item['positionName'], \
                        item['jobNature'], item['education'], item['salary'], item['workYear'], item['createTime']))
                self.conn.commit()
            except pymysql.Error:
                print("Error%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (item['city'], item['companyFullName'], \
                        item['companySize'], item['district'], item['linestaion'], item['positionName'],\
                        item['jobNature'], item['education'], item['salary'], item['workYear'], item['createTime']))
            return item




'''


# 存入MongoDB数据库
class MycrawlPipeline(object):
    def __init__(self):
        # 连接数据库
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        # 建立游标对象
        self.test = self.client['TESTDB']
        self.post1 = self.test['book']
        self.post2 = self.test['movie']
        self.post3 = self.test['music']
    def process_item(self, item, spider):
        # 起点小说
        if spider.name == 'book':
            data = dict(item)
            self.post1.insert(data)
            return item
        # 豆瓣电影
        elif spider.name == 'movie':
            data = dict(item)
            self.post2.insert(data)
            return item
        # 百度音乐
        elif spider.name == 'music':
            data = dict(item)
            self.post3.insert(data)
            return item

'''