# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class MongoDdPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(host="localhost",port=27017)
        self.db = self.client['Jingzhun']
        self.collection = self.db['CompanyInfo11']

    def process_item(self,item,spider):
        self.collection.insert(dict(item))

    def close_spider(self,spider):
        self.client.close()