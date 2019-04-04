# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class H1BItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    employer = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    submit_date = scrapy.Field()
    start_date = scrapy.Field()
    case_status = scrapy.Field()



