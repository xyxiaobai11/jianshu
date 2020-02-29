import MySQLdb
import requests
import re
import datetime
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/77.0.3865.90 Safari/537.36'}
# #url = 'https://www.zhihu.com/'
# url = 'https://www.zhihu.com/people/xioabai-24'
#
# response = requests.get(url, headers=headers, allow_redirects=False)
# print(response.status_code)
# print(response.text)

def get_num(text):
    pattern = re.match('.*?(\d+).*', text)
    if pattern:
        nums = int(pattern.group(1))
    else:
        nums = 0
    return nums
from selenium import webdriver
from lxml.etree import HTML
# driver = webdriver.Chrome()
# driver.get('https://www.jianshu.com/p/ec1109bea8f0')
# data = HTML(driver.page_source)
# title = data.xpath("//div[@class='_gp-ck']//h1/text()")
# num = data.xpath("//div[@class='s-dsoj']/span[2]/text()")
# look = data.xpath("//div[@class='s-dsoj']/span[3]/text()")
# author = data.xpath("//span[@class='_22gUMi']/text()")
# favor = data.xpath("//span[@class='_1LOh_5']/text()")
# time = data.xpath("//time/text()")
# content = data.xpath("//article[@class='_2rhmJa']//text()")
# print(title)
# print(num, look, author, favor, time)
# print(content)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
datetime.datetime.strptime('2019.04.12 11:42:27', '%Y.%m.%d %H:%M:%S')