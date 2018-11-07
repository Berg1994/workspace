# -*- coding: utf-8 -*-
import hashlib
import re
import time

import scrapy

from ..items import BrookingsEduItem


class BrookingsSpider(scrapy.Spider):
    name = 'brookings'
    allowed_domains = ['brookings.edu']
    start_urls = ['https://www.brookings.edu/topics/']

    def parse(self, response):
        """
        解析主页面
        :param response: 二级导航链接
        """
        second_navi_urls = response.xpath(
            '//div[@class="post-linear-list term-list topic-list-wrapper"][1]//ul/li/a/@href').extract()
        for second_navi_url in second_navi_urls:
            yield scrapy.Request(second_navi_url, callback=self.parse_second_navi, meta={'base_url': second_navi_url})

    def parse_second_navi(self, response):
        """
        解析二级导航
        :param response: 返回二级导航链接
        """
        base_url = response.meta.get('base_url')
        clssify_urls = base_url + 'page/{}/'.format(2)
        yield scrapy.Request(clssify_urls, callback=self.parse_topic_page, meta={'page': 2, 'url': base_url})

    def parse_topic_page(self, response):
        """
        解析主题
        :param response: 返回分类下每页链接
        """
        classify_page_urls = response.xpath(
            '//div[@class="list-content"]/article/a/@href | //div[@class="list-content"]/article/div/h4/a/@href'
        ).extract()
        if classify_page_urls:
            for page_url in classify_page_urls:
                yield scrapy.Request(page_url, callback=self.parse_page_detail, meta={'get_image': True})
        page = response.meta.get('page') + 1
        meta_url = response.meta.get('url')
        page_next = meta_url + 'page/{}/'.format(page)
        yield scrapy.Request(page_next, callback=self.parse_topic_page,
                             meta={'page': page, 'url': meta_url, })

    def parse_page_detail(self, response):
        """
        解析页面详情
        :param response: 返回详情信息
        """
        item = BrookingsEduItem()
        # 主站网址
        # item['primarySite'] = 'https://www.brookings.edu/'
        # 当前网址
        item['primarySite'] = response.url
        # 类别
        item['classify'] = response.url.split('/')[3]
        # 发布机关名称
        item['orgName'] = 'Brookings'
        # 创建时间
        item['createTime'] = time.time()
        # content = response.xpath('//div[contains(@class,"post-body")]/child::*//text()').extract()
        content = response.xpath('//div[contains(@class,"post-body")]/p/text()').extract()
        # 内容
        item['content'] = self.pase_content(content)

        author = response.xpath('//span[@class="names"]/a//text()').extract()
        if author:
            # 作者
            item['author'] = author
        # 标题/书名
        item['title'] = response.xpath('//div[@class="headline-wrapper"]//h1/text()').extract_first()
        # 相关领域
        topics = response.xpath('//section[@class="related-topics"]/div/ul/li//text()').extract()
        if topics:
            item['topics'] = topics
        # 出版时间
        item['publishTime'] = response.xpath('//time[@class="date"]//text()').extract_first()
        # 图片链接
        image_url = response.xpath('//div[@class="image-wrapper"]/img//@data-src | '
                                   '//div[contains(@class,"post-body")]/div/img/@data-src').extract()
        if image_url:
            item['imageUrl'] = self.get_source_image(image_url)

        book_info = response.xpath('/html/body/div[2]/header/div/div[2]/h2//text()').extract_first()
        if book_info:
            # 书籍简介
            item['bookInfo'] = book_info

        if item['classify'] == 'events':
            name = response.xpath('//div[@itemprop="location"]//h4//text()').extract()
            # 会议名称
            self.pase_content(name)
            item['address'] = self.pase_content(name)
            audio_url = response.xpath(
                '//div[contains(@class,"past-event-secondary-wrapper")]//article[3]/a/@href').extract()
            if audio_url:
                # 音频链接
                item['audioUrl'] = audio_url
            video_url = response.xpath('//div[@class="vid-wrapper"]//@src').extract()
            if video_url:
                # 视频链接
                item['videoUrl'] = video_url

        if item['classify'] == 'the-avenue':
            foot_note = response.xpath('//section[@class="endnotes"]/div/ol/li//text()').extract()
            # 脚注
            if foot_note:
                item['footNote'] = self.pase_content(foot_note)

            # 作者注释
            # item['author_mark'] = response.xpath('/html/body/div[2]/section[1]/div/div[2]//text()').extract_first()
            # item['author_mark'] = ' '.join(author_mark.split())

        item['fingerPrint'] = self.create_fingerprint(response.url)

        picture = response.meta.get('picture')
        if picture:
            item['picture'] = picture

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

    def create_fingerprint(self, url):
        hash_md5 = hashlib.md5(url.encode('utf'))
        return hash_md5.hexdigest()

    def get_source_image(self, image_list):
        source_rul = []
        for image_url in image_list:
            image = image_url.split('?')[0]
            source_rul.append(image)
        return source_rul
