#词频统计，对于阶段性文件整体的词频把握，本来用于整理心态词典，后选择机器学习方案，统计出的词频用于制作词云
import collections
import jieba
import jieba.posseg as pseg
import pandas as pd
import re

user_dict=[#根据词频文件优化的自定义词典项
           ('戴口罩','v'),('带口罩','v'),('难过','vd'),('心疼','vd'),( '痛苦','vd'),
           ('焦虑','ad'),('害怕','vd'),('担心','vd'),('想开学','v'),('隔离','vn'),
           ('核酸检测','n'),('遵守','v'),('怀疑','v'),('相信','v'),('不相信','v'),
           ('共同','ad'),('辛苦了','e'),('扛疫','vn'),('核酸','n'),('风险','n'),
           ('可怕','a'),('战胜','v'),('自觉','ad'),('自愿','ad'),('门禁','n'),
           ('健康码','n'),('医护人员','n'),('口罩','n'),('通行','a'),
           ('高风险地区','n'),('中风险地区','n'),('低风险地区','n'),('祝贺','v'),('祝福','v'),
           ('热干面','n'),('好起来','ad'),('炸酱面','n'),('严防','v'),('绝望','ad'),
           ('复工','vn'),('复产','vn'),('感动','vd'),('感恩','vd'),('感谢','v'),
           ('感激','v'),('致敬','v'),('停课','v'),('居家隔离','n'),('太难了','e'),
           ('卫生','n'),('境外输入','vn'),('抵制','v'),('抗议','v'),('严查','v'),
           ('疫苗','n'),('新冠','n'),('火神山','n'),('雷神山','n'),('方舱','n'),
           ('热搜','n'),('添乱','v'),('突发','vd'),('爆发','vd'),('发现','vn'),('新发','vd'),
           ('传染','vn'),('传播','vn'),('传谣','v'),('信谣','v'),('辟谣','v'),
           ('早日','ad'),('早发现','vd'),('早治疗','vd'),('太好了','e'),('快点','ad'),
           ('不作为','vd'),('发热','vn'),('物资','n'),('一级响应','n'),('战时','n'),
            ('背锅','v'),('病例','n'),('新增','vd'),('高风险','n')
           ]
for item in user_dict:
    jieba.add_word(item[0],tag=item[1])

stopwords1 = [line.rstrip() for line in
                  open('stopwords/stopwords-master/baidu_stopwords.txt', 'r', encoding='utf-8')]
stopwords2 = [line.rstrip() for line in
                  open('stopwords/stopwords-master/cn_stopwords.txt', 'r', encoding='utf-8')]
stopwords3 = [line.rstrip() for line in
                  open('stopwords/stopwords-master/hit_stopwords.txt', 'r', encoding='utf-8')]
stopwords4 = [line.rstrip() for line in
                  open('stopwords/stopwords-master/scu_stopwords.txt', 'r', encoding='utf-8')]
stopwords = stopwords1 + stopwords2 + stopwords3 + stopwords4
#加载停词表

filenames1=[#'20191208-20200122(c)',
           '20191208-20200122',
           #'20200123-20200207(c)',
           '20200123-20200207',
           #'20200208-20200305(c)',
           '20200208-20200305',
           #'20200306-20200618(c)',
           '20200306-20200618',
           ]
#阶段新闻文件
filenames2=['20191208-20200122(c)',
           #'20191208-20200122',
           '20200123-20200207(c)',
           #'20200123-20200207',
           '20200208-20200305(c)',
           #'20200208-20200305',
           '20200306-20200618(c)',
           #'20200306-20200618',
           ]
#阶段评论文件


def wordprocess(filename):
    filepath='scomments/'+filename+'.csv' #阶段评论路径，提取阶段新闻需切换至snews
    data = pd.read_csv(filepath, encoding='utf-8')
    #读入新闻模式
    #data.columns=['date','tag','content','numR','numF','numC','URL']
    data.columns = ['date', 'URL', 'content', 'numF']#读入评论模式
    newscontent=data['content'].drop_duplicates()#去重
    #newscontent = data['content'] 不去重
    #print(newscontent)

    list_news = newscontent.tolist()
    news_all = ""

    for i in range(len(list_news)):
        news_all = news_all + list_news[i]
    # 选取中文：使用正则表达式
    filter_pattern = re.compile('[^\u4E00-\u9FD5]+')

    chinese_only = filter_pattern.sub('', news_all)

    words_list = pseg.lcut(chinese_only)    #精确划分

    meaninful_words = []

    for word, flag in words_list:
        if word not in stopwords:   #停词库过滤
            meaninful_words.append((word,flag))

    word_counts = collections.Counter(meaninful_words)  # 对分词做词频统计

    words200 = word_counts.most_common(200)     #高频词前n位

    wordfilepath='wdc/'+filename+'200wdc.txt'   #写入词频统计类文件

    with open(wordfilepath, 'w+', encoding='utf-8') as wordc:
        for word, num in words200:
            wordc.write(str(word[0]) +" " +str(word[1])+" " + str(num) + '\n')



#for f in filenames2:
#    wordprocess(f)
wordprocess('availnews')