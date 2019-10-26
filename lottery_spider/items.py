# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LotterySpiderItem(scrapy.Item):
    qihao = scrapy.Field()
    bule_ball = scrapy.Field()
    red_ball = scrapy.Field()