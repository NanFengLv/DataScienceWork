#处理新闻，评论文件，追加写进对应时间段文件
import pandas as pd
import csv

storefile='availfile/availnews.csv'
availfile='scomment/20200306-20200618(c).csv'

origin= open (storefile,'r',encoding='utf-8')
ori_reader=csv.reader(origin)
with open(availfile,'w+',encoding='utf-8') as avail:

    avl_writer=csv.writer(avail)
    for row in ori_reader:
        print(row)
        if row==[]:
            continue
        if row[0]=='时间':
            continue
        if((row[0]<='2020-06-18') and (row[0]>='2020-03-06')):#根据时间分类
            avl_writer.writerow(row)
