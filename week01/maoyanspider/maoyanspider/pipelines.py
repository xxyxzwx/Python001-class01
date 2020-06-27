# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class MaoyanspiderPipeline:
    def process_item(self, item, spider):
        csv_list = [item['name'], item['label'], item['time']]
        movie_csv = pd.DataFrame(data = csv_list)
        movie_csv.to_csv('./scrapy.csv', encoding = 'utf8',mode='a', index = False, header = False)
        return item
