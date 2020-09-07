# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class QuotexmlSpider(XMLFeedSpider):
    name = 'quotexml'
    allowed_domains = ['http://quotes.toscrape.com']
    start_urls = ['http://http://quotes.toscrape.com/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly
    # sitemap_urls = ['']
    # sitemap_rules = [
    #     (regex, callback)
    # ]
    def sitemap_filter(self, entries):
        pass


    def parse_node(self, response, selector):
        item = {}
        #item['url'] = selector.select('url').get()
        #item['name'] = selector.select('name').get()
        #item['description'] = selector.select('description').get()
        return item
