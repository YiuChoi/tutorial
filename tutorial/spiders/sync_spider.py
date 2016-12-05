# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import SyncItem

index = 0


class SyncSpider(scrapy.Spider):
    name = "sync"
    allowed_domains = ["btsynckeys.com"]
    start_urls = ["http://btsynckeys.com"]

    def parse(self, response):
        global index
        if not response.xpath('//tbody/tr').extract():
            exit()
        index += 1
        for sel in response.xpath('//tbody/tr'):
            item = SyncItem()
            item['title'] = sel.xpath('td[1]/text()').extract()
            item['key'] = sel.xpath('td[2]/text()').extract()
            item['time'] = sel.xpath('td[4]/text()').extract()
            yield item
        yield scrapy.Request("http://btsynckeys.com/" + str(index) + "0", callback=self.parse)
