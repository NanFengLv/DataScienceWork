#处理评论评论文件，追加有效项至availcomments
import csv

storefile='data/rmrbC.csv'
availfile='availfile/availcomments.csv'

origin= open (storefile,'r',encoding='utf-8')
ori_reader=csv.reader(origin)
with open(availfile,'a+',encoding='utf-8') as avail:

    avl_writer=csv.writer(avail)
    for row in ori_reader:
        print(row)
        if row==[] or row[0]=='时间':
            continue    #筛去时间为空
        if((row[0]!='None') and (row[2]!='None')):
            avl_writer.writerow(row)