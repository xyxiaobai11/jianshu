# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader.processors import MapCompose, Join, TakeFirst
from scrapy.loader import ItemLoader
from datetime import datetime
def get_num(text):
    pattern = re.match('.*?(\d+).*', text)
    if pattern:
        nums = int(pattern.group(1))
    else:
        nums = 0
    return nums

def remove_blank(value):
    return [value.strip() for value in values if value is not None and value != ' ']

def convert_time(date):
    return datetime.strptime(date, '%Y.%m.%d %H:%M:%S')

# input_processor是在收集数据的过程中所做的处理，output_processor是数据yield之后进行的处理
class ArticleItem(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()   # 标题
    author = scrapy.Field()  # 作者
    num = scrapy.Field(
        input_processor = MapCompose(get_num)
    )     # 字数
    favor = scrapy.Field(
        input_processor = MapCompose(get_num)
    )   # 点赞
    look = scrapy.Field(
        input_processor = MapCompose(get_num)
    )    # 观看数量
    content = scrapy.Field(
            output_processor = Join('')
        )
    url = scrapy.Field()     # 文章url
    url_id = scrapy.Field()  # url指纹
    time = scrapy.Field(
        input_processor = MapCompose(convert_time)
    )    # 时间


