#根据train中训练的模型对阶段性样本进行整体性预测分析，生成用于统计的数据

import pandas as pd
import re
import jieba.posseg as pseg
import jieba
import train
from  sklearn.svm import LinearSVC

def predict_file(filename):
    #调用train中的score方法，评估classfier模型，经过多次实验分析数据得知，在当前数量的训练数据集下，
    #LinearSVC模型和LogisticRegression模型的准确率最高，二者在多数情况下非常接近，选择LinearSVC进行训练
    classifier = train.score(LinearSVC())[1]

    user_dict = [('戴口罩', 'v'), ('带口罩', 'v'), ('难过', 'vd'), ('心疼', 'vd'), ('痛苦', 'vd'),
                 ('焦虑', 'ad'), ('害怕', 'vd'), ('担心', 'vd'), ('想开学', 'v'), ('隔离', 'vn'),
                 ('核酸检测', 'n'), ('遵守', 'v'), ('怀疑', 'v'), ('相信', 'v'), ('不相信', 'v'),
                 ('共同', 'ad'), ('辛苦了', 'e'), ('扛疫', 'vn'), ('核酸', 'n'), ('风险', 'n'),
                 ('可怕', 'a'), ('战胜', 'v'), ('自觉', 'ad'), ('自愿', 'ad'), ('门禁', 'n'),
                 ('健康码', 'n'), ('医护人员', 'n'), ('口罩', 'n'), ('通行', 'a'),
                 ('高风险地区', 'n'), ('中风险地区', 'n'), ('低风险地区', 'n'), ('祝贺', 'v'), ('祝福', 'v'),
                 ('热干面', 'n'), ('好起来', 'ad'), ('炸酱面', 'n'), ('严防', 'v'), ('绝望', 'ad'),
                 ('复工', 'vn'), ('复产', 'vn'), ('感动', 'vd'), ('感恩', 'vd'), ('感谢', 'v'),
                 ('感激', 'v'), ('致敬', 'v'), ('停课', 'v'), ('居家隔离', 'n'), ('太难了', 'e'),
                 ('卫生', 'n'), ('境外输入', 'vn'), ('抵制', 'v'), ('抗议', 'v'), ('严查', 'v'),
                 ('疫苗', 'n'), ('新冠', 'n'), ('火神山', 'n'), ('雷神山', 'n'), ('方舱', 'n'),
                 ('热搜', 'n'), ('添乱', 'v'), ('突发', 'vd'), ('爆发', 'vd'), ('发现', 'vn'), ('新发', 'vd'),
                 ('传染', 'vn'), ('传播', 'vn'), ('传谣', 'v'), ('信谣', 'v'), ('辟谣', 'v'),
                 ('早日', 'ad'), ('早发现', 'vd'), ('早治疗', 'vd'), ('太好了', 'e'), ('快点', 'ad'),
                 ('不作为', 'vd'), ('发热', 'vn'), ('物资', 'n'), ('一级响应', 'n'), ('战时', 'n'),
                 ('背锅', 'v'), ('病例', 'n'), ('新增', 'vd'), ('高风险', 'n')
                 ]
    for item in user_dict:
        jieba.add_word(item[0], tag=item[1])

    stopwords1 = [line.rstrip() for line in
                  open('stopwords/stopwords-master/baidu_stopwords.txt', 'r', encoding='utf-8')]
    stopwords2 = [line.rstrip() for line in
                  open('stopwords/stopwords-master/cn_stopwords.txt', 'r', encoding='utf-8')]
    stopwords3 = [line.rstrip() for line in
                  open('stopwords/stopwords-master/hit_stopwords.txt', 'r', encoding='utf-8')]
    stopwords4 = [line.rstrip() for line in
                  open('stopwords/stopwords-master/scu_stopwords.txt', 'r', encoding='utf-8')]
    stopwords = stopwords1 + stopwords2 + stopwords3 + stopwords4

    for f in filename:

        filepath = 'scomment/' + f + '(c).csv'
        data = pd.read_csv(filepath, encoding='utf-8')

        # data.columns=['date','tag','content','numR','numF','numC','URL']
        data.columns = ['date', 'URL', 'content', 'numF']

        ccontent = data['content']
        # newscontent = data['content']
        # print(ccontent)
        list_comments = ccontent.tolist()

        filter_pattern = re.compile('[^\u4E00-\u9FD5]+')
        # comment = ""
        page = []
        for i in range(len(list_comments)):
            comment = "" + list_comments[i]
            # print(comment)

            chinese_only = filter_pattern.sub('', comment)
            words_list = pseg.lcut(chinese_only)
            meaninful_words = {}
            for word, flag in words_list:
                if word not in stopwords:
                    meaninful_words[word] = 'True'
            page.append(meaninful_words)
        #print(page)
        print(len(page))

        pred = classifier.classify_many(page)

        data['emotion'] = pred
        # print(data)
        data.to_csv('analysis/' + f + '(a).csv', encoding='utf-8')


predict_file(['20191208-20200122',
             '20200123-20200207',
             '20200208-20200305',
             '20200306-20200618'])#用训练模型为阶段样本整体进行情绪分析预测，存入分析文件，用于最终统计
