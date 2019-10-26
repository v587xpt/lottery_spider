# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class LotterySpiderPipeline(object):
    def __init__(self):
        print("爬虫开始......")
        self.fp = open("daletou.json", 'w', encoding='utf-8')  # 打开一个json文件

    def process_item(self, item, spider):
        item_json = json.dumps(dict(item), ensure_ascii=False)      #注意此处的item，需要dict来进行序列化；
        self.fp.write(item_json + '\n')
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束......")
