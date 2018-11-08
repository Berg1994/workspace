# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings

from .items import RandOrgItem


class RandOrgPipeline(object):

    def __init__(self):
        self.MONGODB_HOST = settings['MONGODB_HOST']
        self.MONGODB_PORT = settings['MONGODB_PORT']
        self.MONGODB_DB = settings['MONGODB_DB']

        conn = pymongo.MongoClient(self.MONGODB_HOST,
                                   self.MONGODB_PORT)
        self.db = conn[self.MONGODB_DB]

    def process_item(self, item, spider):
        self.collection = self.db[RandOrgItem.collections]
        self.collection.update({'fingerPrint': item['fingerPrint']}, {'$set': item}, True)
        return item
