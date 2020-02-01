# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
class WikispiderItem(scrapy.item):
    # 在此处定义item字段:
    # name = scrapy.Field()
    pass
"""

class Article(scrapy.Item):
    url = scrapy.Field
    title = scrapy.Field
    text = scrapy.Field
    lastUpdated = scrapy.Field