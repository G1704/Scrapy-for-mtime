# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient
from mtime import settings

class MtimePipeline(object):
    def __init__(self):
        self.filename = open("mtime.json", "a+")

        # connect database
        # self.client = MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # # self.db.authenticate("admin", "123456")
        # self.db = self.client[settings['MONGO_DB']]
        # self.coll = self.db[settings['MONGO_COLL']]

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(text)
        with open('Store_urls.txt', 'a') as f2:
            store_url = 'http://people.mtime.com/%s/details.html'%str(item['per_id']) + '\n'
            f2.write(store_url)
            f2.close()
        # insert into database
        # self.coll.save(dict(item))
        return item

    def close_spider(self, spider):
        self.filename.close()
