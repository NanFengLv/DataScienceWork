# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    tag = scrapy.Field()
    numF = scrapy.Field()
    numC = scrapy.Field()
    numR = scrapy.Field()
    commentsURL = scrapy.Field()


