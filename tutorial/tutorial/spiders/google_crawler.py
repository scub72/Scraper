# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import GoogleSearchBlockData


class GoogleTwoSpider(scrapy.Spider):
    name = 'google_crawler'
    #    allowed_domains = ['www.google.pl']
    download_delay = 5
    start_urls = ['https://www.google.com/search?q=zawory+blokujące']

    def parse(self, response):
        load_data = ItemLoader(item=GoogleSearchBlockData(), response=response)
        load_data.add_xpath('name', '//div[@class="BNeawe vvjwJb AP7Wnd"]/text()')
        load_data.add_xpath('url', '//div[@class="kCrYT"]//a/@href')
        load_data.add_xpath('next_site', '//a[@class="nBDE1b G5eFlf"]/@href')
        next_page = load_data.get_collected_values('next_site')

        try:
            next_page = next_page[next_page.__len__()-1]
            yield load_data.load_item()
            yield scrapy.Request(next_page, callback=self.parse)
        except IndexError:
            self.log('\n\n Moj LOGGER: \n'+ 'Zakończono pobieranie'+'\n\n')


