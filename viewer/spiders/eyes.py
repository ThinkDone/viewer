# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from viewer.items import ImageItem


class EyesSpider(CrawlSpider):
    name = u'eyes'

    def __init__(self, url, *args, **kwargs):
        super(EyesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    rules = (
        Rule(LinkExtractor(), callback=u'parse_item', follow=True),
    )

    def parse_item(self, response):
        loader = ItemLoader(item=ImageItem(), response=response)
        loader.add_value(u'from_url', response.url)
        loader.add_css(u'image_urls', u'img::attr(src)')
        return loader.load_item()
