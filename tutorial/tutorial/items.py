# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


def add_site_prefix(value):
    return 'https://www.google.pl'+value

class GoogleSearchBlockData(scrapy.Item):
    """
    items template:

     name = scrapy.Field(
         input_processor=MapCompose(some functions to process after scraped item),
         output_processor=Join()
    )
    """
    name = scrapy.Field()
    url = scrapy.Field()

    next_site = scrapy.Field(
        input_processor=MapCompose(add_site_prefix)
    )
