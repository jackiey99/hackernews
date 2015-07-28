# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
from hackerbot.items import HackerbotItem
from hackernews.models import News


class HackerbotPipeline(object):
	def process_item(self, item, spider):
		try: 
			HackerbotItem.django_model.objects.get(title = item['title'])
		except (KeyError, News.DoesNotExist):
			item.save()
			return item 
		else:
			raise DropItem("Duplicate item found: %s" % item['title'])
