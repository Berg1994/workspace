# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChathamhouseOrgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #内容
    content = scrapy.Field()
    #作者
    author = scrapy.Field()
    #出版日期
    publishTime = scrapy.Field()
    #爬取时间
    createTime = scrapy.Field()
    #主站地址
    primarySite = scrapy.Field()
    #导航类型
    classify = scrapy.Field()
    #指纹
    fingerPrint = scrapy.Field()
    #视频链接
    videoUrl = scrapy.Field()
    #相关领域
    topics = scrapy.Field()
    #地区
    regons = scrapy.Field()
    #地址
    address = scrapy.Field()

