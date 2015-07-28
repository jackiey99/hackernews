import scrapy
from hackerbot.items import HackerbotItem

class HackerSpider(scrapy.Spider):
	name = "hacker"
	start_urls = [
		"https://news.ycombinator.com/",
	]

	def parse(self, response):
		for sel in response.xpath('//tr[@class="athing"]/td[3]'):
			item = HackerbotItem()
			item['title'] = sel.xpath('a/text()').extract()[0]
			item['link'] = sel.xpath('a/@href').extract()[0]
			yield item