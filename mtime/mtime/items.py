# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtimeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # store information

    # name
    name = scrapy.Field()

    # ID
    per_id = scrapy.Field()

    # information
    information = scrapy.Field()

    # introduction
    introduction = scrapy.Field()

    # relationship
    relationship = scrapy.Field()

    # experience
    experience = scrapy.Field()

    pass
