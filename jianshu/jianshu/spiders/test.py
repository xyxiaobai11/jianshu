from pprint import pprint

import requests
from lxml.etree import HTML
#url = 'https://www.jianshu.com/p/4f1850bac09b'
url = 'https://www.jianshu.com/trending_notes'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/77.0.3865.90 Safari/537.36',
            #'x-csrf-token': 'uindOeqExLavnGAc8ISVPN8r9LaGdUnxoX6AsinAalZFhv1Sn+UoAGbn9X9ZVl/0F9DL61b/666nyyCrL2BmLw==',
           #'referer': 'https://www.jianshu.com/',
           'x-pjax': 'true'}

response = requests.get(url, headers=headers)
# with open('./aa.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)

data = {'page': '4'}
response = requests.post(url, headers=headers, data=data)
html = HTML(response.text)
href = html.xpath("//div[@class='content']/a[@class='title']/@href")
print(href)

html = HTML(response.text)
# with open('./bb.txt', 'w', encoding='utf8') as f:
#    f.write(response.text)
title = html.xpath("//div[@class='_gp-ck']//h1/text()")
#print(title)


author = html.xpath("//span[@class='_22gUMi']/text()")
time = html.xpath("//time/text()")
num = html.xpath("//div[@class='s-dsoj']/span[2]/text()")
look = html.xpath("//div[@class='s-dsoj']/span[3]/text()")
favor  = html.xpath("//span[@class='_1LOh_5']/text()")
content = html.xpath("//article[@class='_2rhmJa']//text()")
#print(author, time, num, look, favor)
#print(content)
