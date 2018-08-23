# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class Kr36Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapyProject.Field()
    fullname = Field()
    brief = Field()
    scale = Field()
    cityStr = Field()
    operName = Field()
    partners = Field()
    startDate = Field()
    registCapi = Field()
    industryStr = Field()
    intro = Field()
    phase = Field()
    fundsAmount = Field()
    website = Field()