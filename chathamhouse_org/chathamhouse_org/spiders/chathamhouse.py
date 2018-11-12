# -*- coding: utf-8 -*-
import re

import scrapy

from ..items import ChathamhouseOrgItem


class ChathamhouseSpider(scrapy.Spider):
    name = 'chathamhouse'
    # allowed_domains = ['chathamhouse.org']
    page = 0
    base_url = 'https://www.chathamhouse.org/research/topics/all?page={}'
    # start_urls = ['']

    def start_requests(self):
        url = 'https://www.chathamhouse.org/research/topics/all?page=0'
        scrapy.Request(url, callback=self.parse_second_navi)

    def parse_second_navi(self, response):
        """
        二级导航类型
        :param response:分类导航详情
        """
        # print(response.url)
        classify_urls = response.xpath('//div[@class="view-content"]//a/@href').extract()
        for classify_url in classify_urls:
            classify_detail_url = response.urljoin(classify_url)
            yield scrapy.Request(classify_detail_url, callback=self.parse_latest__detail)
        total_page = response.xpath('//li[contains(@class,"pager-last")]/a/@href').extract_first()
        if total_page:
            total_page = total_page.split('=')[-1]
            for page_num in range(1, int(total_page) + 1):
                next_page = self.base_url.format(page_num)
                yield scrapy.Request(next_page, callback=self.parse_second_navi)

    def parse_latest__detail(self, response):
        # print(response.url)
        # 对当前页面修改拼接

        # 最新最新链接

        # item = ChathamhouseOrgItem()
        # item['classify'] = response.url.split('/')[-1]
        # 最新事件
        fragment0 = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing-default")]').extract()
        if fragment0:
            fragment0_url = response.url + '#fragment-0'
            yield scrapy.Request(fragment0_url, callback=self.parse_fragment0)
        # 以往事件
        fragment3 = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing-block_2")]').extract()
        if fragment3:
            fragment3_url = response.url + '#fragment-3'
            yield scrapy.Request(fragment3_url, callback=self.parse_fragment3)
        # 影音
        fragment4 = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing_audio_and_video-default")]').extract()
        if fragment4:
            fragment4_url = response.url + '#fragment-4'
            yield scrapy.Request(fragment4_url, callback=self.parse_fragment4)
        #

    def parse_fragment0(self, response):
        """
        解析三级导航第一列最新事件
        :param response: 页面链接
        :return:
        """
        base_classify_urls = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing-default")]')
        classify_latest_urls = base_classify_urls.xpath('./div/a//@href').extract()
        if classify_latest_urls:
            for classify_latest_url in classify_latest_urls:
                classify_latest = response.urljoin(classify_latest_url)
                yield scrapy.Request(classify_latest, callback=self.parse_page_detail)

        next_pager = base_classify_urls.xpath(
            './/li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = response.urljoin(next_pager)
            yield scrapy.Request(next_page, callback=self.parse_fragment0)

    def parse_fragment3(self, response):
        base_fragment3_url = response.xpath('//div[contains(@class,"view-section_index_auto_content_listing-block_2")]')
        classify_past_urls = base_fragment3_url.xpath('./div/a/@href').extract()
        if classify_past_urls:
            for classify_past_url in classify_past_urls:
                classify_past = response.urljoin(classify_past_url)
                yield scrapy.Request(classify_past, callback=self.parse_page_detail)

        next_pager = base_fragment3_url.xpath(
            './/li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = response.urljoin(next_pager)
            yield scrapy.Request(next_page, callback=self.parse_fragment3)
        fragment4 = response.xpath(
            '//div[contains(@class,"view-section_index_auto_content_listing_audio_and_video-default")]')
        if fragment4:
            fragment4_url = response.url + '#fragment-4'
            yield scrapy.Request(fragment4_url, callback=self.parse_fragment4,
                                 meta={'base_url': response.url})

    def parse_fragment4(self, response):

        classify_past_urls = response.xpath('//div[@id="fragment-4"]/div/a/@href').extract()
        if classify_past_urls:
            for classify_past_url in classify_past_urls:
                classify_past = response.urljoin(classify_past_url)
                yield scrapy.Request(classify_past, callback=self.parse_page_detail)

        next_pager = response.xpath(
            '//div[@id="fragment-4"]//li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = response.urljoin(next_pager)
            yield scrapy.Request(next_page, callback=self.parse_fragment4)

    def parse_page_detail(self, response):
        # 获取项目对象
        item = response.meta['item']
        # 标题
        item['title'] = response.xpath('//section[contains(@class,"page__section__main")]//h1//text()').extract_first()
        # 发布时间
        publishTime = response.xpath('//div[contains(@class,"date")]/span//text()').extract()
        item['publishTime'] = ''.join(publishTime)
        # 内容
        content = response.xpath('//div[contains(@class,"rich-text")]//text()').extract()
        item['content'] = self.pase_content(content)
        # 作者/参与者
        author_name = response.xpath('//div[@class="group-authors"]//strong//text()').extract()
        if author_name:
            item['author'] = self.pase_content(author_name)
        # 活动地址
        address = response.xpath('//div[contains(@class,"meta--location")]//text()').extract_first()
        if address:
            item['address'] = self.pase_content(address)
        # 地理
        regions = response.xpath('//div[contains(@class,"regions")]/div//text()').extract()
        if regions:
            item['regons'] = self.pase_content(regions)
        # 相关话题
        topics = response.xpath('//div[contains(@class,"projects")]/div//text()').extract()
        if topics:
            item['classify'] = topics
        # 导航类型
        classify = response.xpath('//div[contains(@class,"topics")]/div//text()').extract()
        if classify:
            item['topics'] = self.pase_content(topics)

        yield item

    def pase_content(self, items):
        """
        对文本内容中的换行空格替换
        :param items: 节点获取的文本列表
        :return: 文本字符串
        """
        str_items = ''.join(items)
        str_content = re.sub(r'\r|\n|\t\xa0', '', str_items)
        return str_content

    def parse_video_url(self, url):
        base_video_url = re.findall(r'(http.*?)-', url)
        cons_url = base_video_url[0] + '.mp4'
        return cons_url
