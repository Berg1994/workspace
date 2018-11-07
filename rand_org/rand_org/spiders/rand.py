# -*- coding: utf-8 -*-
import re
import time

import scrapy


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
        # print(response.url)
        # 标题
        title = response.xpath('//div[@id="content"]//h1//text()').extract_first()
        # 爬取时间
        createTime = time.time()
        ##############################################################################
        # 视频类
        # 视频链接
        videoUrl = response.xpath('//div[@id="content"]//video/source[@type="video/mp4"]/@src').extract_first()
        # 视频内容
        video_content = response.xpath('//div[@id="srch"]//p[@class=""]//text()').extract()
        ##############################################################################

        # 出版物
        # 出版物相关话题
        topics = response.xpath(
            '//div[@id="content"]//ul[@class="related-topics"]/li[position() > 1]//text()').extract()
        # 出版物作者作者
        author = response.xpath('//*[@id="page-content"]//p[@class="authors"]//a//text()').extract()
        # 出版物图片
        pubs_image = response.xpath('//div[@class="eight columns"]//div[@class="cover-image"]//img/@src').extract()
        # 出版物二级标题
        pubs_second_title = response.xpath('//div[@id="content"]//h2[@class="subtitle"]//text()').extract()
        # 出版物说明
        pubs_info = response.xpath('//aside[@class="document-details"]//ul/li//text()')
        # 出版物内容
        pubs_content = response.xpath('//div[contains(@class,"product-main")]//text()').extract()
        # 出版物出版时间
        pubs_publishtime = response.xpath('//div[@class="eight columns"]//p[@class="publish-online"]//text()').extract()
        if pubs_publishtime:
            pass
        # 出版物链接
        pubs_book_url = response.xpath('//div[@class="cover-image"]/a[@id="look-inside"]/@href |'
                                       ' //div[@class="section"]/a/@href').extract_first()
        ##############################################################################

        # 博客相关话题
        pubs_topics = response.xpath('//aside/ul/li/a/font/font/text()').extract()

        # 博客作者
        author = response.xpath(
            '//*[@id="page-content"]//div[@class="body-text"]//p[@class="authors"]//a//text()').extract()
        # 博客内容
        blog_content = response.xpath('//div[@class="body-text"]/p[not(@class="authors")]//text()').extract()

        # 博客出版时间
        blog_publishtime = response.xpath('//*[@id="page-content"]/div[1]/div//p[@class="date"]').extract()
        ##############################################################################

        # 新闻

        ##############################################################################

        #专家
        #专家头像
        expert_icon = response.xpath('//div[@class="basic-info"]/img/@src').extract_first()
        #专家职称
        expert_title = response.xpath('//div[@class="title"]//text()').extract()
        #专家学历
        expert_education = response.xpath('//div[@class="education"]/p/text()').extract_first()
        #内容
        expert_content = response.xpath('//div[@id="onebio_overview"]//text()').extract_first()
        #地址
        expert_adr = response.xpath('//div[@class="adr"]/div[@class="locality"]//text()').extract_first()


    def parse_content(self, item):
        str_itme = ''.join(item)
        str_content = re.sub(r'\r|\n|\t\xa0', '', str_itme)
        return str_content
