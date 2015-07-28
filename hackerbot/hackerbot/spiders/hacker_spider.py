import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hackerbot.items import HackerbotItem

class HackerSpider(CrawlSpider):
	name = "hacker"
	start_urls = [
		"https://news.ycombinator.com/",
	]

	rules = (
		Rule(LinkExtractor(allow = r'news\?p=\d*'), callback='parse_item', follow=True),
	)

	def parse_start_url(self, response):
		for sel in response.xpath('//tr[@class="athing"]/td[3]'):
			item = HackerbotItem()
			item['title'] = sel.xpath('a/text()').extract()[0]
			item['link'] = sel.xpath('a/@href').extract()[0]
			yield item

	def parse_item(self, response):
		for sel in response.xpath('//tr[@class="athing"]/td[3]'):
			item = HackerbotItem()
			item['title'] = sel.xpath('a/text()').extract()[0]
			item['link'] = sel.xpath('a/@href').extract()[0]
			yield item