# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 豆瓣电影TOP250
class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名
    movie_name = scrapy.Field()

    # 电影信息
    movie_message = scrapy.Field()

    # 评分
    movie_star = scrapy.Field()

    # 经典名句
    movie_quote = scrapy.Field()

    # 评分人数
    number = scrapy.Field()
    pass


# 起点小说排行榜
class BookItem(scrapy.Item):

    # 小说名
    book_name = scrapy.Field()

    # 作者
    author = scrapy.Field()

    # 小说类型
    book_type = scrapy.Field()

    # 小说状态
    book_state = scrapy.Field()

    # 小说更新
    book_update = scrapy.Field()

    book_time = scrapy.Field()

    # 最新一章地址
    new_href = scrapy.Field()

    # 小说简介
    book_intro = scrapy.Field()
    pass

# 百度音乐各榜单
class MusicItem(scrapy.Item):
    # 音乐排名
    top = scrapy.Field()

    # 音乐名
    music_name = scrapy.Field()

    # 歌手
    songer = scrapy.Field()
    pass

# 猫眼电影排行榜
class MaoyanItem(scrapy.Item):

    top = scrapy.Field()
    title = scrapy.Field()
    star = scrapy.Field()
    releasetime = scrapy.Field()
    pass

# 腾讯控股股票信息
class GupiaoItem(scrapy.Item):
    # 数据标题
    title = scrapy.Field()

    # 数据名
    dataname = scrapy.Field()

    # 第一条数据
    fristdata = scrapy.Field()

    # 第二条数据
    secondata = scrapy.Field()

    # 第三条数据
    thridata = scrapy.Field()


# 拉钩职位信息
class LagouItem(scrapy.Item):
    # 城市
    city = scrapy.Field()

    # 公司
    companyFullName = scrapy.Field()

    # 公司规模
    companySize = scrapy.Field()

    # 地区
    district = scrapy.Field()

    # 教育程度
    education = scrapy.Field()

    # 地点
    linestaion = scrapy.Field()

    # 招聘职务
    positionName = scrapy.Field()

    # 招聘要求
    jobNature = scrapy.Field()

    # 工资
    salary = scrapy.Field()

    # 工作经验
    workYear = scrapy.Field()

    # 岗位发布时间
    createTime = scrapy.Field()


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_url = scrapy.Field()
