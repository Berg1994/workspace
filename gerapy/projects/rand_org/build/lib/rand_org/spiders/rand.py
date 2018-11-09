# -*- coding: utf-8 -*-
import hashlib
import re
import time

import scrapy

from ..items import RandOrgItem


class RandSpider(scrapy.Spider):
    name = 'rand'
    allowed_domains = ['rand.org']
    start_urls = ['https://www.rand.org/topics/']

    def parse(self, response):
        """
        获取所有导航链接
        :param response: 链接
        :return:
        """
        base_link = 'https://www.rand.org'
        result = response.xpath('//ul[@class="topic-list"]/li/ul/li/a/@href').extract()
        for url in result:
            classify_url = base_link + url
            yield scrapy.Request(url=classify_url, callback=self.parse_calssify)

    def parse_calssify(self, response):
        base_url = response.url
        page_url = base_url + '?page={}'.format(1)
        yield scrapy.Request(url=page_url, callback=self.parse_all_url, meta={'page': 1, 'url': base_url})

    def parse_all_url(self, response):
        """
        获取每页信息
        :param respones: 返回页面链接
        """

        res = response.xpath('//ul[@class="teasers list organic"]/li/div[2]/h3/a/@href').extract()
        if res:
            for detail_url in res:
                yield scrapy.Request(url=detail_url, callback=self.parse_html_detail)

            page = response.meta.get('page') + 1
            meta_url = response.meta.get('url')
            url = meta_url + '?page={}'.format(page)
            yield scrapy.Request(url=url, callback=self.parse_all_url, meta={'page': page, 'url': meta_url})

    def parse_html_detail(self, response):
        """
        获取页面详情
        """
        with open('test.txt', 'a') as f:
            f.write(response.url + '\n')

        item = RandOrgItem()
        # 标题
        item['title'] = response.xpath('//div[@id="content"]//h1//text()').extract_first()
        # 主站网址
        item['primarySite'] = 'https://www.rand.org/'
        # 当前网址
        item['currentUrl'] = response.url

        # 爬取时间
        item['createTime'] = time.time()
        # 导航类型
        item['classify'] = response.url.split('/')[3]
        #指纹
        item['fingerPrint'] = self.parse_fingerprint(response.url)

        ##############################################################################
        # 视频类
        # 视频链接

        videoUrl = response.xpath('//div[@id="content"]//video/source[@type="video/mp4"]/@src').extract_first()
        if videoUrl:
            item['videoUrl'] = videoUrl
        # 视频内容
        video_content = response.xpath('//div[@id="srch"]//p[@class=""]//text()').extract()
        if video_content:
            item['content'] = self.parse_content(video_content)
        ##############################################################################

        # 出版物
        if item['classify'] == 'pubs':
            # 出版物相关话题
            topics = response.xpath(
                '//div[@id="content"]//ul[@class="related-topics"]/li[position() > 1]//text()').extract()
            if topics:
                item['topics'] = ''.join(topics)

            # 出版物作者
            author = response.xpath('//*[@id="page-content"]//p[@class="authors"]//a//text()').extract()
            if author:
                item['author'] = author
            # 出版物图片
            image_url = response.xpath(
                '//div[@class="cover-image"]//img/@src').extract_first()
            if image_url:
                item['imagesUrl'] = image_url
            # 出版物二级标题
            pubs_second_title = response.xpath('//div[@id="content"]//h2[@class="subtitle"]//text()').extract()
            if pubs_second_title:
                item['bookInfo'] = pubs_second_title

            # 出版物说明
            pubs_detail = response.xpath('//aside[@class="document-details"]//ul/li//text()').extract()
            if pubs_detail:
                item['bookDetail'] = self.parse_content(pubs_detail)
            # 出版物内容
            content = response.xpath('//div[contains(@class,"product-main")]//text() |'
                                     '//div[@id="srch"]//p[not(@class="linkbar")]//text()').extract()
            item['content'] = self.parse_content(content)
            # 出版物出版时间
            pubs_publishtime = response.xpath(
                '//div[@class="eight columns"]//p[@class="publish-online"]//text()').extract()
            if pubs_publishtime:
                item['publishTime'] = pubs_publishtime
            # 出版物链接
            pubs_book_url = response.xpath('//div[@class="cover-image"]/a[@id="look-inside"]/@href |'
                                           ' //div[@class="section"]/a/@href').extract_first()
            if pubs_book_url:
                item['imagesUrl'] = pubs_book_url
            yield item

        ##############################################################################
        if item['classify'] == 'blog':
            # 博客相关话题
            item['topics'] = response.xpath('//aside/ul/li/a//text()').extract()

            # 博客作者
            author = response.xpath(
                '//*[@id="page-content"]//div[@class="body-text"]//p[@class="authors"]//a//text()').extract()
            if author:
                item['author'] = author

            # 博客内容
            content = response.xpath('//div[@class="body-text"]//p//text()').extract()
            item['content'] = self.parse_content(content)

            # 博客出版时间
            item['publishTime'] = response.xpath(
                '//*[@id="page-content"]/div[1]/div//p[@class="date"]//text()').extract_first()
            yield item

            ##############################################################################
        if item['classify'] == 'news':
            # 新闻
            # 新闻发布日期
            item['publishTime'] = response.xpath(
                '//*[@id="page-content"]//div[@class="newsicon"]/p[2]//text()').extract()
            # 内容
            content = response.xpath('//div[@class="eight columns"]//p//text()').extract()
            item['content'] = self.parse_content(content)
            # 相关话题
            item['topics'] = response.xpath('//div[@class="four columns"]//li[@class="related"]//text()').extract()

            yield item

        ##############################################################################
        if item['classify'] == 'about':
            # 专家
            # 专家头像
            expertIcon = response.xpath('//div[@class="basic-info"]/img/@src').extract_first()
            if expertIcon:
                item['expertIcon'] = expertIcon
            # 专家职称
            item['expertName'] = response.xpath('//div[@class="title"]//text()').extract()
            # 专家简介
            expertInfo = response.xpath('//div[@class="basic-info"]/div//text()').extract()
            item['expertInfo'] = self.parse_content(expertInfo)
            # 专家简历
            expertDV = response.xpath('//div[@class="basic-info"]/ul/li/a[@class="pdf"]/@href').extract()
            if expertDV:
                item['expertDV'] = expertDV
            # 专家详情
            expertDetail = response.xpath('//div[@id="onebio_overview"]//text()').extract()
            item['content'] = self.parse_content(expertDetail)
            yield item

    def parse_content(self, item):
        str_itme = ''.join(item)
        str_content = re.sub(r'\r|\n|\t\xa0', '', str_itme)
        return str_content

    def parse_fingerprint(self,url):
        hash_sha = hashlib.sha1(url.encode('utf8'))
        return hash_sha.hexdigest()