# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExpertItem(scrapy.Item):
    collections = 'experts'
    # 专家链接
    primarySite = scrapy.Field()
    # 头像
    expertIcon = scrapy.Field()
    # 专家姓名
    expertName = scrapy.Field()
    # 专家职位及研究方向
    expertInfo = scrapy.Field()
    # 专家详情
    expertDetail = scrapy.Field()
    # 专家简历
    expertCV = scrapy.Field()
    # 爬取时间
    createTime = scrapy.Field()


class AboutUsItem(scrapy.Item):
    collections = 'aboutUs'
    # 内容
    content = scrapy.Field()
    # 网站图标
    logo = scrapy.Field()
    # 爬取时间
    createTime = scrapy.Field()
    # 主站地址
    primarySite = scrapy.Field()


class BrookingsEduItem(scrapy.Item):
    collections = 'topics'

    # 主站地址
    primarySite = scrapy.Field()
    # 截图
    picture = scrapy.Field()
    # 涉及领域
    topics = scrapy.Field()
    # 文章标题
    title = scrapy.Field()
    # 文章内容
    content = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
    # 爬取时间
    createTime = scrapy.Field()
    # 作者
    auenue = scrapy.Field()
    # 关键字
    keyWords = scrapy.Field()
    # 发布机构名称
    orgName = scrapy.Field()
    # 视频链接
    videoUrl = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 图片链接
    imageUrl = scrapy.Field()
    # 脚注
    footNote = scrapy.Field()
    # 音频链接
    audioUrl = scrapy.Field()
    # 类别
    classify = scrapy.Field()
    # 书籍说明
    bookInfo = scrapy.Field()
    # 指纹摘要
    fingerPrint = scrapy.Field()

