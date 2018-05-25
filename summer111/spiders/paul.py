# -*- coding: utf-8 -*-
#用于数据的爬取

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from summer111.items import Summer111Item


class paul(CrawlSpider):
    # 爬虫名字
    name = 'paul'
    # 运行爬取的域名
    #allowed_domains = ['xiaozhu.com']
    # 开始爬取的URL
    start_urls = ['http://bj.xiaozhu.com/fangzi/11136241760.html']

    # 爬取函数
    def parse(self, response):
        # xpath 解析response内容，提取数据
        # //*[@id="post-110769"]/div[1]/h1
        item = Summer111Item()
        selector = Selector(response)
        title = selector.xpath('//h4/em/text()').extract()[0]
        address = selector.xpath('//p/span/text()').extract()[0].strip()
        price = selector.xpath('//*[@id="pricePart"]/div[1]/span/text()').extract()[0]
        lease_type = selector.xpath('//*[@id="introduce"]/li[1]/h6/text()').extract()[0]
        suggestion = selector.xpath('//*[@id="introduce"]/li[2]/h6/text()').extract()[0]
        bed = selector.xpath('//*[@id="introduce"]/li[3]/h6/text()').extract()[0]

        item['title'] = title
        item['address'] = address
        item['price'] = price
        item['lease_type'] = lease_type
        item['suggestion'] = suggestion
        item['bed'] = bed

        yield item
