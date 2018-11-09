# -*- coding: utf-8 -*-
import re
from urllib.parse import urljoin

import scrapy


class ChathamhouseSpider(scrapy.Spider):
    name = 'chathamhouse'
    allowed_domains = ['chathamhouse.org']
    page = 0
    base_url = 'https://www.chathamhouse.org/research/topics/all?page={}'
    start_urls = ['https://www.chathamhouse.org/research/topics/all?page=0']

    def parse(self, response):
        """
        二级导航类型
        :param response:分类导航详情
        """
        # print(response.url)
        classify_urls = response.xpath('//div[@class="view-content"]//a/@href').extract()
        for classify_url in classify_urls:
            classify_detail_url = urljoin(response.url, classify_url)
            yield scrapy.Request(classify_detail_url, callback=self.parse_latest__detail)
        total_page = response.xpath('//li[contains(@class,"pager-last")]/a/@href').extract_first()
        if total_page:
            total_page = total_page.split('=')[-1]
            for page_num in range(1, int(total_page) + 1):
                next_page = self.base_url.format(page_num)
                yield scrapy.Request(next_page, callback=self.parse)

    def parse_latest__detail(self, response):
        # print(response.url)
        # 对当前页面修改拼接
        page = 0
        # 最新最新链接
        page_detail_urls = []

        classify_latest_urls = response.xpath('//div[@id="fragment-0"]/div/a/@href').extract()
        if classify_latest_urls:
            for classify_latest_url in classify_latest_urls:
                classify_latest = urljoin(response.url, classify_latest_url)
                yield scrapy.Request(classify_latest)

        classify_video_audio_urls = response.xpath('//div[@id="fragment-4"]/div/a/@href').extract()
        if classify_video_audio_urls:
            for classify_video_audio_url in classify_video_audio_urls:
                classify_video_audio = urljoin(response.url, classify_video_audio_url)
                page_detail_urls.append(classify_video_audio)

        next_pager = response.xpath(
            '//div[@id="fragment-0"]//li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = urljoin(response.url, next_pager)
            yield scrapy.Request(next_page, callback=self.parse_latest__detail)
        fragment3 = response.xpath('//div[@class="item-list"]/ul/li//a[@id="ui-id-4"]/@href').extract_first()
        if fragment3:
            fragment3_url = response.url + '#fragment-3'
            yield scrapy.Request(fragment3_url, callback=self.parse_fragment3,
                                 meta={'base_url': response.url})

    def parse_fragment3(self, response):

        classify_past_urls = response.xpath('//div[@id="fragment-3"]/div/a/@href').extract()
        if classify_past_urls:
            for classify_past_url in classify_past_urls:
                classify_past = urljoin(response.url, classify_past_url)
                yield scrapy.Request(classify_past)

        next_pager = response.xpath(
            '//div[@id="fragment-3"]//li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = urljoin(response.url, next_pager)
            yield scrapy.Request(next_page, callback=self.parse_fragment3)
        fragment4 = response.xpath('//div[@class="item-list"]/ul/li//a[@id="ui-id-5"]/@href').extract_first()
        if fragment4:
            fragment4_url = response.url + '#fragment-4'
            yield scrapy.Request(fragment4_url, callback=self.parse_fragment4,
                                 meta={'base_url': response.url})

    def parse_fragment4(self, response):

        classify_past_urls = response.xpath('//div[@id="fragment-4"]/div/a/@href').extract()
        if classify_past_urls:
            for classify_past_url in classify_past_urls:
                classify_past = urljoin(response.url, classify_past_url)
                yield scrapy.Request(classify_past)

        next_pager = response.xpath(
            '//div[@id="fragment-4"]//li[contains(@class,"pager-next")]/a/@href').extract_first()
        if next_pager:
            next_page = urljoin(response.url, next_pager)
            yield scrapy.Request(next_page, callback=self.parse_fragment4)
