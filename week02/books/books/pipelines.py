# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class BooksPipeline:    

    def process_item(self, item, spider):
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = 'mysql456$%^',
            db = 'scrapy'
        )
        
        self.cur = self.conn.cursor()
        values = (item['name'], item['price'], item['des'], item['id'])
        try:
            sql = 'insert into book value(%s,%s,%s,%s);'
            #sql1 = 'select * from book;'
            #self.cur.execute(sql1)
            self.cur.execute(sql,values)
            #print(self.cur.fetchall())
            self.cur.close()
            self.conn.commit()
        except Exception as e:
            print('failed',e)
            self.conn.rollback()
        self.conn.close()
    