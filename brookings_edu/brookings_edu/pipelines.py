# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

from .items import BrookingsEduItem, AboutUsItem, ExpertItem


class BrookingsEduPipeline(object):
    """
    用于保存Item数据
    """

    def __init__(self):
        self.MONGODB_HOST = settings['MONGODB_HOST']
        self.MONGODB_PORT = settings['MONGODB_PORT']
        self.MONGODB_DB = settings['MONGODB_DB']

        conn = pymongo.MongoClient(host=self.MONGODB_HOST,
                                   port=self.MONGODB_PORT)

        self.db = conn[self.MONGODB_DB]

    def process_item(self, item, spider):
        # if spider == 'brookings':
            if isinstance(item, BrookingsEduItem):
                self.collections = self.db[BrookingsEduItem.collections]
                self.collections.update({'fingerPrint': item['fingerPrint']}, {'$set': item}, True)
                return item
        # if spider == 'about_us':
            if isinstance(item, AboutUsItem):
                self.collections = self.db[AboutUsItem.collections]
                self.collections.update({'primarySite': item['primarySite']}, {'$set': item}, True)
                return item
        # if spider == 'experts':
            if isinstance(item, ExpertItem):
                self.collections = self.db[ExpertItem.collections]
                self.collections.update({'primarySite': item['primarySite']}, {'$set': item}, True)
                return item
