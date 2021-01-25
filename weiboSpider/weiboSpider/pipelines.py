# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

class WeibospiderPipeline:
    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = os.path.dirname(__file__) + '/spiders/test.csv'
        # 打开(创建)文件
        self.file = open(store_file, 'a+',encoding='utf-8')
        # csv写法
        self.writer = csv.writer(self.file)
        #self.writer.writerow(('时间','标签（标题)','内容','转发数','点赞数','评论数','热评链接'))
        self.writer.writerow(('时间', '热评链接' , '评论内容', '点赞数'))

    def process_item(self, item, spider):
        # 判断字段值不为空再写入文件
        if item['content']:
            #self.writer.writerow((item['time'],item['tag'],item['content'],item['numR'],item['numF'],item['numC'],item['commentsURL']))
            self.writer.writerow((item['time'], item['commentsURL'], item['content'], item['numF']))

        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
