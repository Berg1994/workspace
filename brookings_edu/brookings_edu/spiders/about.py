# -*- coding: utf-8 -*-
import re
import time

import scrapy

from ..items import AboutUsItem


class AboutSpider(scrapy.Spider):
    name = 'about_us'
    allowed_domains = ['www.brookings.edu/about-us']
    start_urls = ['https://www.brookings.edu/about-us/']

    def parse(self, response):
        """
               解析关于我们页面信息
               :param response: html详情
               """
        item = AboutUsItem()
        # 主站网址
        item['primarySite'] = 'https://www.brookings.edu/'
        # 网站图标
        item['logo'] = response.xpath('/html/head/link[3]/@href').extract_first()
        # 内容
        content = response.xpath('//div[contains(@class,"post-body")]/p').extract()
        content_title = response.xpath('')

        item['content'] = self.pase_content(content)
        # 爬取时间
        item['createTime'] = time.time()
        yield item

    def pase_content(self, items):
        """
        对文本内容中的换行空格替换
        :param items: 节点获取的文本列表
        :return: 文本字符串
        """
        str_items = ''.join(items)
        str_content = re.sub(r'\r|\n|\t', '', str_items)
        return str_content
