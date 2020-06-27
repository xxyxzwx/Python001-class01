# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyanspider.items import MaoyanspiderItem
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    '''
    headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36"
    } 

    def start_requests(self):
        return [scrapy.Request(url = self.start_urls[0], headers = self.headers, callback = self.parse)]
    '''
    def parse(self, response):
        movies = Selector(response=response).xpath('//dd[position()<=10]')
        i = 1
        for movie in movies:
            url = movie.xpath('./div[1]/div[2]/a/@href').extract()[0]
            info_url = 'https://maoyan.com'+url
            #print(url)
            if i <= 10:
                yield scrapy.Request(url = info_url, callback=self.parse2)
                i = i + 1
            else:
                break
    
    def parse2(self,response):
        item = MaoyanspiderItem()
        name = response.xpath('//h1[@class="name"]/text()').extract()[0]
        label = "".join(response.xpath('//html/body/div[3]/div/div[2]/div[1]/ul/li/a/text()').extract()).replace(' ','')
        time = response.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()').extract()[0]
        item['name'] = name
        item['label'] = label
        item['time'] = time
        print(name,label,time)
        yield item
