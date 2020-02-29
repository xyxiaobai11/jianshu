# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors


class JianshuPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf8')

    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(data)
        return item

    def close_spider(self, spider):
        self.file.close()

# 同步插入到数据库中
class JianshuMysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('192.168.227.129', 'root', '123456', 'jianshu', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = '''
            insert into article(title, author, url, content) values(%s, %s, %s, %s)
        '''
        #print(item['title'], item['url'], item['author'], item['content'])
        self.cursor.execute(insert_sql, (item['title'], item['author'], item['url'], item['content']))
        self.conn.commit()


# 异步插入数据库
class jianshuTwistMysqlPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        params = dict(
            host=settings.get('HOST'),
            db=settings.get('DBNAME'),
            user=settings.get('USER'),
            passwd=settings.get('PASSWD'),
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **params)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 将mysql插入变成异步操作
        query = self.dbpool.runInteraction(self.insert, item)
        query.addErrback(self.handle_error)

    def handle_error(self, failure):
        print(failure)

    def insert(self, cursor, item):
        insert_sql = '''
                    insert into article(title, author, url, content, look, num, favor, time) values(%s, %s, %s, %s,
                    %s, %s, %s, %s)
                '''
        cursor.execute(insert_sql, (item['title'], item['author'], item['url'], item['content'], item['look'], item['num'], \
                                    item['favor'], item['time']))