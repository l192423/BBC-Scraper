# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbcItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    titleImage = scrapy.Field()
    author = scrapy.Field()
    createdPublishDate = scrapy.Field()
    updatedPublishDate = scrapy.Field()
    leadtext = scrapy.Field()
    description = scrapy.Field()
    htmlDescription = scrapy.Field()
    images = scrapy.Field()
    topics = scrapy.Field()
    
