# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import hashlib
import time

from PIL import Image
from scrapy import signals


class BrookingsEduSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BrookingsEduDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
from logging import getLogger


class SeleniumMiddleware(object):
    def __init__(self, timeout=200):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.PhantomJS()
        self.browser.maximize_window()
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.image_urls = []

    def __del__(self):
        self.browser.close()

    def process_response(self, request, response, spider):
        """
        使用phantomjs抓取页面
        :param request: Request对象
        :param spider: SPider对象
        :return: HtmlResponse
        """
        if spider.name == 'brookings':

            # self.logger.debug('Phantomjs is Starting')
            try:
                if response.xpath('//figure[contains(@class,"simplechart-widget")]'):
                    self.browser.get(response.url)

                    svg_image = self.browser.find_elements_by_css_selector('.simplechart-widget')

                    self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'nvd3-svg')))
                    self.browser.save_screenshot(r'./photo.png')
                    #此处使用for循环无效
                    # for image in svg_image:
                    while svg_image:
                        pop_image = svg_image.pop()

                        left = pop_image.location['x']
                        top = pop_image.location['y']
                        width = left + pop_image.size['width']
                        height = top + pop_image.size['height']
                        image = Image.open(r'./photo.png')
                        image = image.crop((left, top, width, height))
                        image_name = self.filename_fingerprint(pop_image.id.split(':')[-1] + time.strftime('%Y%m%d%H%M'))
                        image_filename = 'F:\images\\' + image_name + '.png'
                        image.save(image_filename)
                        self.image_urls.append(image_filename)
                        request.meta['picture'] = self.image_urls
                    return HtmlResponse(url=response.url, body=self.browser.page_source, request=request,
                                        encoding='utf-8', status=200)
                else:
                    return response
            except TimeoutException as e:

                return response
        else:
            return response

    def filename_fingerprint(self,filename):
        hash_filename = hashlib.md5(filename.encode('utf8'))
        return hash_filename.hexdigest()
