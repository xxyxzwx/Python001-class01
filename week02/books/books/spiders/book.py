# -*- coding: utf-8 -*-
import scrapy
from books.items import BooksItem
import re

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']
    starturl = 'http://books.toscrape.com/catalogue/'
    page = 1
    def parse(self, response):
        for i in range(1,21):
            bookuri = response.xpath(f'//li[{i}]//h3/a/@href').extract()[0]
            bookurl = BookSpider.starturl + bookuri
            #print(url)
            yield scrapy.Request(url = bookurl, callback=self.getinfo)
        BookSpider.page += 1
        pageurl = BookSpider.starturl+'page-'+str(BookSpider.page)+'.html'
        if BookSpider.page <=50:
            yield scrapy.Request(url = pageurl, callback=self.parse)

    def getinfo(self,response):
        item = BooksItem()
        bookname = response.xpath('//h1/text()').extract()[0]
        bookprice = response.xpath('//div/p/text()').extract()[0]
        #去除货币符号
        bookprice = ''.join(re.findall(r"[\d+\.\d+]", bookprice))
        bookdescription = response.xpath('//article/p/text()').extract()[0]
        bookid = response.xpath('//tr[1]/td/text()').extract()[0]
        item['name'] = bookname
        item['price'] = bookprice
        item['des'] = bookdescription
        item['id'] = bookid
        yield item
        #print(bookname,bookprice,bookid)

        