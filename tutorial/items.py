# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SyncItem(scrapy.Item):
    title = scrapy.Field()
    key = scrapy.Field()
    time = scrapy.Field()
    pass
