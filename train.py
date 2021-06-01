def text():
    f1 = open('emotions/angry.txt','r',encoding='utf-8')
    f2 = open('emotions/cold.txt','r',encoding='utf-8')
    f3 = open('emotions/excited.txt','r',encoding='utf-8')
    f4 = open('emotions/hopeful.txt','r',encoding='utf-8')
    f5 = open('emotions/excited.txt','r',encoding='utf-8')
    f6 = open('emotions/moved.txt','r',encoding='utf-8')
    f7 = open('emotions/neutral.txt','r',encoding='utf-8')
    f8 = open('emotions/sad.txt','r',encoding='utf-8')
    f9 = open('emotions/satisfied.txt','r',encoding='utf-8')
    f10 = open('emotions/unsatisfied.txt','r',encoding='utf-8')
    f11 = open('emotions/shock.txt','r',encoding='utf-8')
    f12 = open('emotions/worry.txt','r',encoding='utf-8')
    f=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12]
    str=''
    for fx in f:
        line = fx.readline()
        while line:
            str += line
            line = fx.readline()
        fx.close()

    return str

def bag_of_words(words):
    return dict([(word,True)for word in words])     #返回格式化单字特征标记结果
#print((bag_of_words(text())))


import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
#双词特征标记
def bigram(words,score_fn=BigramAssocMeasures.chi_sq,n=1000):   #结合卡方统计降维，选取信息量最大的前n条作为特征
    bigram_finder=BigramCollocationFinder.from_words(words)
    bigrams=bigram_finder.nbest(score_fn,n)
    newBigrams = [u+v for (u,v) in bigrams]
    return  bag_of_words(newBigrams)
#print(bigram(text(),score_fn=BigramAssocMeasures.chi_sq,n=1000))

#单双词结合特征标记
def bigram_words(words,score_fn=BigramAssocMeasures.chi_sq,n=1000):     #结合卡方
    bigram_finder=BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn,n)
    newBigrams=[u+v for(u,v)in bigrams]
    a = bag_of_words(words)
    b = bag_of_words(newBigrams)
    a.update(b)
    return a
#print(bigram_words(text(),score_fn=BigramAssocMeasures.chi_sq,n=1000))

import jieba
def read_file(filename):
    #stop = [line.strip() for line in open('F:/train/stop.txt','r',encoding='utf-8').readlines()]
    f=open(filename,'r',encoding='utf-8')
    line = f.readline()
    str=[]
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

    while line:
        fenci = jieba.lcut(line,cut_all=False)
        str.append(list(set(fenci)))
        line = f.readline()
    return str

from  nltk.probability import FreqDist,ConditionalFreqDist
from nltk.metrics import  BigramAssocMeasures

#jieba分词特征标记
def jieba_features(number):
    angryWords = []     #angry类型的words
    coldWords = []
    excitedWords = []
    hopefulWords =[]
    movedWords = []
    neutralWords = []
    sadWords = []
    satisfiedWords = []
    shockWords = []
    suspiciousWords=[]
    unsatisfiedWords=[]
    worryWords=[]
    Words=[angryWords,coldWords,excitedWords,hopefulWords,
           movedWords,neutralWords,sadWords,satisfiedWords,
           shockWords,suspiciousWords,unsatisfiedWords,worryWords]
    filename=['angry','cold','excited','hopeful',
              'moved','neutral','sad','satisfied',
              'shock','suspicious','unsatisfied','worry']
    for i in range(12):
        for items in read_file('emotions/'+filename[i]+'.txt'):
            for item in items:
                Words[i].append(item)   #添加对应样本


    word_fd=FreqDist()      #所有words的频率统计
    cond_word_fd = ConditionalFreqDist()    #条件words频率统计

    for word in angryWords:
        word_fd[word] += 1
        cond_word_fd['angry'][word]+=1
    for word in coldWords:
        word_fd[word]+=1
        cond_word_fd['cold'][word]+=1
    for word in excitedWords:
        word_fd[word]+=1
        cond_word_fd['excited'][word]+=1
    for word in hopefulWords:
        word_fd[word]+=1
        cond_word_fd['hopeful'][word]+=1
    for word in movedWords:
        word_fd[word]+=1
        cond_word_fd['moved'][word]+=1
    for word in neutralWords:
        word_fd[word]+=1
        cond_word_fd['neutral'][word]+=1
    for word in sadWords:
        word_fd[word]+=1
        cond_word_fd['sad'][word]+=1
    for word in satisfiedWords:
        word_fd[word]+=1
        cond_word_fd['satisfied'][word]+=1
    for word in shockWords:
        word_fd[word]+=1
        cond_word_fd['shock'][word]+=1
    for word in suspiciousWords:
        word_fd[word]+=1
        cond_word_fd['suspicious'][word]+=1
    for word in unsatisfiedWords:
        word_fd[word]+=1
        cond_word_fd['unsatisfied'][word]+=1
    for word in worryWords:
        word_fd[word]+=1
        cond_word_fd['worry'][word]+=1

    angry_word_count = cond_word_fd['angry'].N()    #angry words数量
    cold_word_count = cond_word_fd['cold'].N()
    excited_word_count = cond_word_fd['excited'].N()
    hopeful_word_count = cond_word_fd['hopeful'].N()

    moved_word_count = cond_word_fd['moved'].N()
    neutral_word_count = cond_word_fd['neutral'].N()
    sad_word_count=cond_word_fd['sad'].N()
    satisfied_word_count=cond_word_fd['satisfied'].N()

    shock_word_count=cond_word_fd['shock'].N()
    suspicious_word_count=cond_word_fd['suspicious'].N()
    unsatisfied_word_count=cond_word_fd['unsatisfied'].N()
    worry_word_count=cond_word_fd['worry'].N()

    #总词数
    total_word_count = (angry_word_count + cold_word_count + excited_word_count + hopeful_word_count
                        + moved_word_count + neutral_word_count + sad_word_count + satisfied_word_count
                        + shock_word_count + suspicious_word_count + unsatisfied_word_count + worry_word_count)

    word_scores ={}

    for word,fred in word_fd.items():
        angry_score = BigramAssocMeasures.chi_sq(cond_word_fd['angry'][word],(fred,angry_word_count),
                                                 total_word_count)      #angrywords的卡方统计量
        cold_score = BigramAssocMeasures.chi_sq(cond_word_fd['cold'][word],(fred,cold_word_count),
                                                total_word_count)
        excited_score=BigramAssocMeasures.chi_sq(cond_word_fd['excited'][word],(fred,excited_word_count),
                                                 total_word_count)
        hopeful_score = BigramAssocMeasures.chi_sq(cond_word_fd['hopeful'][word], (fred, hopeful_word_count),
                                                   total_word_count)
        moved_score = BigramAssocMeasures.chi_sq(cond_word_fd['moved'][word], (fred, moved_word_count),
                                                   total_word_count)
        neutral_score = BigramAssocMeasures.chi_sq(cond_word_fd['neutral'][word], (fred, neutral_word_count),
                                                   total_word_count)
        sad_score = BigramAssocMeasures.chi_sq(cond_word_fd['sad'][word], (fred, sad_word_count),
                                                    total_word_count)
        satisfied_score = BigramAssocMeasures.chi_sq(cond_word_fd['satisfied'][word], (fred, satisfied_word_count),
                                                   total_word_count)
        shock_score = BigramAssocMeasures.chi_sq(cond_word_fd['shock'][word], (fred, shock_word_count),
                                                   total_word_count)
        suspicious_score = BigramAssocMeasures.chi_sq(cond_word_fd['suspicious'][word], (fred, suspicious_word_count),
                                                   total_word_count)
        unsatisfied_score = BigramAssocMeasures.chi_sq(cond_word_fd['unsatisfied'][word], (fred, unsatisfied_word_count),
                                                   total_word_count)
        worry_score = BigramAssocMeasures.chi_sq(cond_word_fd['worry'][word], (fred, worry_word_count),
                                                   total_word_count)
        word_scores[word]=(angry_score+cold_score+excited_score+hopeful_score+
                            moved_score+neutral_score+sad_score+satisfied_score+
                           shock_score+suspicious_score+unsatisfied_score+worry_score)
        #一个词的信息量等于所有类型词的卡方统计量之和

    best_vals = sorted(word_scores.items(),key=lambda item:item[1],reverse=True)[:number]
    #信息量倒序排序
    best_words=set([w for w,s in best_vals])
    return dict([(word,True) for word in best_words])   #格式化返回
#print(jieba_features(100))

def build_features():
    #feature = bag_of_words(text())
    #feature = bigram(text(),score_fn=BigramAssocMeasures.chi_sq,n=300)
    #feature=bigram_words(text(),score_fn=BigramAssocMeasures.chi_sq,n=500)
    feature=jieba_features(1000)    #选择jieba特征

    angryFeatures = []
    coldFeatures=[]
    excitedFeatures=[]
    hopefulFeatures=[]
    movedFeatures=[]
    neutralFeatures=[]
    sadFeatures=[]
    satisfiedFeatures=[]
    shockFeatures=[]
    suspiciousFeatures=[]
    unsatisfiedFeatures=[]
    worryFeatures=[]

    Features=[angryFeatures,coldFeatures,excitedFeatures,hopefulFeatures,
              movedFeatures,neutralFeatures,sadFeatures,satisfiedFeatures,
              shockFeatures,suspiciousFeatures,unsatisfiedFeatures,worryFeatures]
    filename = ['angry', 'cold', 'excited', 'hopeful',
                'moved', 'neutral', 'sad', 'satisfied',
                'shock', 'suspicious', 'unsatisfied', 'worry']
    for i in range(12):
        for items in read_file('emotions/' + filename[i] + '.txt'):
            a={}
            for item in items:
                if item in feature.keys():
                    a[item]='True'
            fWords=[a,filename[i]]
            Features[i].append(fWords)      #给各种情感词语标记标签

    '''negFeatures = []
    for items in read_file('F:/train/bad.txt'):
        a={}
        for item in items:
            if item in feature.keys():
                a[item]='True'
        negWords = [a,'neg']
        negFeatures.append(negWords)'''
    return Features

Features=build_features()

train=[]
test=[]
from random import shuffle
import math
for i in range(12):
    shuffle(Features[i])    #shuffle避免顺序影响机器学习
    point=math.ceil(len(Features[i])*0.2)   #二八定律分割样本
    train=train+Features[i][point:]
    test=test+Features[i][:point]



'''train = posFeatures[200:]+negFeatures[200:]
test = posFeatures[:200]+negFeatures[:200]'''

testdata,tag = zip(*test)   #test解析矩阵
print(testdata)

from nltk.classify.scikitlearn import SklearnClassifier
import sklearn
def score(classifier):
    classifier = SklearnClassifier(classifier)
    classifier.train(train)

    pred = classifier.classify_many(testdata)   #对测试集进行标记
    n=0
    s=len(pred)
    for i in range(0,s):
        if pred[i] == tag[i]:   #对比解析的人工标注tag
            n=n+1       #相同加一
    #return n/s
    return n/s,classifier   #返回精确值和训练后的模型

from  sklearn.svm import  SVC,LinearSVC,NuSVC
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import  LogisticRegression
from sklearn.metrics import  accuracy_score

print('BernoulliNB \'s accuracy is %f' % score(BernoulliNB())[0])

print('MultinomiaNB\'s accuracy is %f' % score(MultinomialNB())[0])

print('LogisticRegression\'s accuracy is  %f' % score(LogisticRegression())[0])

print('SVC\'s accuracy is %f' % score(SVC())[0])

print('LinearSVC\'s accuracy is %f' % score(LinearSVC())[0])



