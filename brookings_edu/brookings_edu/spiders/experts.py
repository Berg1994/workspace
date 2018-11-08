# -*- coding: utf-8 -*-
import hashlib
import re
import time
from urllib.parse import urljoin

import scrapy

from ..items import ExpertItem


class ExpertsSpider(scrapy.Spider):
    name = 'experts'
    allowed_domains = ['brookings.edu']
    base_url = 'https://www.brookings.edu/experts/page/{}/'
    start_urls = ['https://www.brookings.edu/']

    def parse(self, response):
        """
        主页解析
        :param response:返回专家导航链接
        """
        experts_navi = response.xpath('//*[@id="menu-item-20631"]/a/@href').extract_first()
        experts__navi_url = urljoin(response.url, experts_navi)
        yield scrapy.Request(experts__navi_url, callback=self.parse_expert)

    def parse_expert(self, response):
        """
        专家页面解析
        :param response: 专家详情链接
        """

        experts_urls = response.xpath(
            '//div[@class="list-content"]/article/div[@class="expert-image"]/a/@href').extract()
        if experts_urls:
            for experts_url in experts_urls:
                yield scrapy.Request(experts_url, callback=self.parse_expert_detail)

            page = response.meta.get('page') if response.meta.get('page') else 1
            next_page = self.base_url.format(page)
            yield scrapy.Request(next_page, callback=self.parse_expert, meta={'page': page + 1})

    def parse_expert_detail(self, response):
        """
        专家详情解析
        """
        item = ExpertItem()
        # 专家页面链接
        item['primarySite'] = response.url
        # 专家头像
        item['expertIcon'] = response.xpath('//div[@class="expert-image"]/img/@data-src').extract_first().split('?')[0]
        # 专家名字
        item['expertName'] = response.xpath('//div[@class="expert-info"]/h1/text()').extract_first()
        # 专家简介
        # item['expertInfo'] = response.xpath('//div[@class="expert-info"]//h3//text()').extract()
        item['expertInfo'] = response.xpath('//div[@class="expert-grid"]//font/text()').extract()
        # 专家详情
        content = response.xpath('//div[contains(@class,"expert-intro-text ")]/p/text()').extract()
        item['expertDetail'] = self.pase_content(content)
        # 专家简历
        expertCV = response.xpath('//div[contains(@class,"download")]/ul/li[1]/a/@href').extract_first()
        if expertCV:
            item['expertCV'] = expertCV
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
        str_content = re.sub(r'\r|\n|\t|\xa0', '', str_items)
        return str_content
