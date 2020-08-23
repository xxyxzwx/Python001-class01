import scrapy
from scrapy.selector import Selector
from aaaa.items import AaaaItem
from .analysis import dataAnalysis

class QipaoshuiSpider(scrapy.Spider):
    name = 'qipaoshui'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['http://www.smzdm.com/fenlei/qipaoshui/']

    def parse(self, response):
        urLList = response.xpath('//ul[@id="feed-main-list"]/li[position()<=10]//h5/a/@href').extract()
        for urL in urLList:
            #meta传递参数给callback中的函数
            yield scrapy.Request(url = urL, callback=self.checkpage, meta={'url': urL})

    def checkpage(self, response):
        pageList = response.xpath('//*[@id="comment"]/div[1]/ul[@class="pagination"]/li[position()<last()-2]/a/@href').extract()
        if len(pageList)!=0:
            for page in pageList:
                yield scrapy.Request(url = page, callback=self.getinfor)
        else:
            #dont_filter跳过判断是否重复请求
            yield scrapy.Request(url = response.meta['url'], callback=self.getinfor, dont_filter=True)

    def getinfor(self, response):
        productType = response.xpath('//section/div/a[6]/span/text()').extract()[0]
        productName = response.xpath('//article//h1/text()').extract()[0].replace(' ','').replace('\n','')
        comments = response.xpath('//div[@id="commentTabBlockNew"]//li/div[2]')
        item = AaaaItem()
        for pinglun in comments:
            username = pinglun.xpath('.//a[@class="a_underline user_name"]/span/text()').extract()[0]
            comment_time = pinglun.xpath('.//div[@class="time"]/meta/@content').extract()[0]
            comment_content = pinglun.xpath('./div[@class="comment_conWrap"]/div[1]/p/span/text()').extract()[0]
            print(productType,productName,username,comment_content,comment_time)
            item['productType'] = productType
            item['productName'] = productName
            item['username'] = username
            item['comment_content'] = comment_content
            item['sentiments'] = dataAnalysis(comment_content)
            item['comment_time'] = comment_time
            yield item
