# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RandOrgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    #当前页面
    primarySite = scrapy.Field()
    #领域类型
    topics = scrapy.Field()
    #标题/名称
    title = scrapy.Field()
    #内容
    content= scrapy.Field()
    #发布时间
    publishTime = scrapy.Field()
    #作者
    author = scrapy.Field()
    #指纹
    fingerPrint = scrapy.Field()
    #类型
    classify = scrapy.Field()
    #网站名称
    orgName = scrapy.Field()
    #视频链接
    videoUrl = scrapy.Field()
    #爬取时间
    createTime = scrapy.Field()
    #图片链接
    imagesUrl = scrapy.Field()
    #书籍说明
    bookInfo = scrapy.Field()
    #地址
    address = scrapy.Field()
    #专家头像
    expertIcon = scrapy.Field()
    #专家名称
    expertName = scrapy.Field()
    #职位及研究方向
    expertInfo = scrapy.Field()
    #专家详情
    expertDetail = scrapy.Field()
    #网站logo
    logo = scrapy.Field()
