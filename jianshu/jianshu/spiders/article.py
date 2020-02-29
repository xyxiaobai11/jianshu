# -*- coding: utf-8 -*-
from urllib.parse import urljoin
import datetime
import scrapy
from scrapy.loader import ItemLoader
from jianshu.items import JianshuItem
from jianshu.items import ArticleItem
from selenium import webdriver
from scrapy import signals
from pydispatch import dispatcher

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['jianshu.com']
    #start_urls = ['https://www.jianshu.com/trending_notes']

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.prefs = {'profile.managed_default_content_settings.images':2}
        self.options.add_experimental_option('prefs', self.prefs)
        self.driver = webdriver.Chrome(options=self.options)
        super(ArticleSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self):
        self.driver.quit()

    def start_requests(self):
        for page in range(1, 50):
            data = {'page': str(page)}
            url = 'https://www.jianshu.com/trending_notes'
            #print('正在下载解析第%d页-----'%page)
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)


    def parse(self, response):
        href_list = response.xpath("//div[@class='content']/a[@class='title']/@href").extract()
        for href in href_list:
            url = urljoin(response.url, href)
            #print(url)
            yield scrapy.Request(url=url, callback=self.parse_html)


    def parse_html(self, response):
        loader = ArticleItem(item=JianshuItem(), response=response)
        loader.add_xpath('title', "//div[@class='_gp-ck']//h1/text()")
        loader.add_xpath('num', "//div[@class='s-dsoj']/span[2]/text()")
        loader.add_xpath('look', "//div[@class='s-dsoj']/span[3]/text()")
        loader.add_xpath('author', "//span[@class='_22gUMi']/text()")
        loader.add_xpath('favor', "//span[@class='_1LOh_5']/text()")
        loader.add_xpath('time', "//time/text()")
        loader.add_xpath('content', "//article[@class='_2rhmJa']//text()")
        loader.add_value('url', response.url)

        article_item = loader.load_item()

        yield article_item

