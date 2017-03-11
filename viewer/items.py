# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # the default field names, set IMAGES_URLS_FIELD and/or IMAGES_RESULT_FIELD settings to override them
    image_urls = scrapy.Field()
    images = scrapy.Field()
    from_url = scrapy.Field()
