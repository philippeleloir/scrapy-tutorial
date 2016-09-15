# -*- coding: utf-8 -*-

import scrapy
##from scrapy.loader import ItemLoader

from dmoztuto.items import DmoztutoItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
			"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
			"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
			]

	def parse(self, response):
		for sel in response.xpath('//div[contains(@class, "title-and-desc")]'):
			item = DmoztutoItem()
			item['title'] = sel.xpath('a/div[contains(@class, "site-title")]/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('normalize-space(div[contains(@class, "site-descr ")]/text())').extract()
			yield item
