# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import urlparse

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item[u'image_urls']:
            from_url = item[u'from_url'][0]
            image_url = urlparse.urljoin(from_url, image_url)
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x[u'path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem(u"Item contains no images")
        item[u'image_paths'] = image_paths
        return item
