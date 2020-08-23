# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql, json

class AaaaPipeline:
    def process_item(self, item, spider):
        with open('/root/learnpython/mysql.json','r') as file:
            mysql_conf = json.load(file)
        self.conn = pymysql.connect(
            host = mysql_conf['host'],
            port = mysql_conf['port'],
            user = mysql_conf['user'],
            password = mysql_conf['passwd'],
            database = mysql_conf['db']
        )
        self.cur = self.conn.cursor()
        values = [item['productType'], item['productName'], item['username'], \
                 item['comment_content'], item['comment_time'], item['sentiments'], \
                 item['username'], item['productName']]
        try:
            sql = 'insert into product(productType, productName, username, \
                  comment_content, comment_time, sentiments) select \
                  %s,%s,%s,%s,%s,%s from dual where not \
                  exists(select username from product where username=(%s) \
                  and productName=(%s));'
            self.cur.execute(sql,values)
            self.cur.close()
            self.conn.commit()
        except Exception as e:
            print('failed',e)
            self.conn.rollback()
        self.conn.close()
