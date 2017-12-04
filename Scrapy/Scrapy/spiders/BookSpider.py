# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector


class BookSpider(Spider):
    name = 'book'
    allowed_domains = ['www.qisuu.com']
    start_urls = ['https://www.qisuu.com']

    def parse(self, response):
        sel = Selector(response)
        book_list = sel.css('.listBox > ul > li')
