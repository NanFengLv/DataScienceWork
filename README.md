# DataScienceWork
## 2019级数据科学作业，组长：贺思嘉，组员：顾雯文，杨承玉


## （一）获取数据（关键代码：weibo.py, pipelines.py, settings.py）
利用scrapy project 建立爬虫项目，通过微博移动端爬取人民日报，央视新闻两大官媒于2019-12-08至2020-06-18
发布的与疫情相关的微博正文以及热评，在数据获取阶段通过直接抓取热评的方式筛选评论。通过直接对各类媒体号
的分析发现，央视新闻和人民日报与疫情相关的微博热度都显著较高，通过关键词筛选完成新闻筛选，不再另加过滤。
通过调整文件，共获取带日期的评论（rawcomments.csv）累计70000余条，相关微博近9000条（news.csv）。（爬虫
过程中由于网络等诸多因素可能部分数据略有重复）后期再次调整爬虫文件，抓取微博正文及相关信息（发布日期，
点赞数目，评论数目，转发数目，热评页面URL），微博热评内容及相关信息（发布时间，点赞数目，热评页面URL），
可实现微博和热评通过热评页面URL实现关联，减少request嵌套，提高效率。

### 问题以及解决：
  - 在三种微博访问端选取最简单的页面高效获取数据（移动端）
  - 链接格式'https://weibo.cn/2803301701/profile?advancedfilter=1&uid=2803301701&keyword=%E7%96%AB%E6%83%85&hasori=1&haspic=0&starttime=20191228&endtime=20200203&smblog=%E7%AD%9B%E9%80%89&rand=1579&p=r'
  - 解析页面时会发现爬取到一定页数再加载是空页，但是没有加载出对应时间段的全部微博，所以需要预先找出断点，调整时间段，避免数据缺失
  - 微博正文和评论页面不同的解析方式（通过callback和parser之间的组合实现对不同对象的爬取）
  - try方法的添加避免部分数据缺失导致的程序中断
  - 访问移动端实现关键词提取需要登陆状态，购买微博账号，登陆保存cookie，建立三个账号的cookiepool（settings.py）

    ```python   
        'cookie':random.choice([
            'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lxoYYU8q2xrxqTSKn_CpsdU9FRk9hkXgjFBd-ZFLtWgw.; SUB=_2A25NBfusDeRhGedL7FcQ9CnKzDiIHXVuCYXkrDV6PUJbktANLVGnkW1NVLlRXD1fNE5OHfzgjAj4Le2YREsDbNzK; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFc_RjAOE7eziX0B9Cxd0ZX5NHD95QpSKMfeKBNSoMXWs4Dqc_zi--fi-z7iKysi--fiKysi-8si--NiKnRi-zpi--Ri-8siK.fi--Ri-8siK.fi--fi-z7i-zpi--Ri-8siK.fi--Ri-8siK.f; SSOLoginState=1610714109'
            'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1ly4WN5Y7JF9S8Yt76TXvsM8hjszbiVDg2dNza4ztwPAc.; SUB=_2A25NBfpiDeRhGedG6FsZ8ijEzjiIHXVuCYYqrDV6PUJbktANLUflkW1NUUy5fomuAPwIr6k2MT8J7vvxz5wIpU_H; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Q.PBhxnseuIPdTqccfTLo5NHD95Qp1he41hzc1h-XWs4Dqcj.i--NiK.4i-i2i--4iK.ciKyFi--fiKnfiK.pi--ci-z7i-zX; SSOLoginState=1610713650'
            'ALF=1613290798; _T_WM=57793362254; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWzIL0bNFvHceYYZgGGQ8jF5NHD95Qp1hB4eKn4eh50Ws4Dqcj_i--fi-isiKn0i--NiKnpi-zfi--ci-zRiK.7i--fi-ihiKn7i--Ni-iWi-is; SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lIOJvS_dA7JJ7cE8eypaH8Zv7HiPlgzPFf6Nx25nfyLo.; SUB=_2A25NBfjJDeRhGedG71sQ-CfMyz-IHXVuCZiBrDV6PUJbktANLWrDkW1NUT_K-AioZvOx2Q1YSXElKPwm-pL6CV19; SSOLoginState=1610713241'
            #'SCF=AnzF7GAuIKbKOCjHneW1wudSb5QaieMnG5C1aGzWCr1lhajquDLFTFhx9kYhI3ieGWNb_H2g8ZoGI4cEzWjI7Gg.; SUB=_2A25NBSB-DeRhGeVG6FIT-CrKzTiIHXVuBkA2rDV6PUNbktANLXn2kW1NT6CtQ1TLm5kUNF4bU4YdWpMyxCCA_lsA; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFXSvMYvQD3wFF8om.-PVW45JpX5KMhUgL.FoeRe05E1hBcSoB2dJLoIEBLxKqL1-eL1hnLb812b70c51f3d17074fb0ffbe6892817'xKnL1h.LBozLxK-LBKBLBo2LxK.L1hML12Bt; SSOLoginState=1610698798; ALF=1613290798; _T_WM=
            ])
    ```
  - 访问头的设置（middlewares.py，RandomUserAgentMiddleware(object)）

## （二）数据处理（dataprocess0.py, dataprocess1.py, dataprocess2.py）
分析需求，根据重大公共事件将2019-12-08至2020-06-18分为四个阶段，并将数据按照提取的时间进行相同区间划分
内容存入阶段数据文件（dateformat.csv, dateformat(c).csv），在阶段划分时，筛去部分相关信息缺失的数据，
对数据文件分别进行总体层面上的分词词频分析以及时间段层面上的分词词频分析，建立词频记录文件fileformatwdc.txt
分析首轮不加定义词典的词频文件，结合微博内容，建立自定义词典对分词词典进行补充，实现分词动态调整，保证
部分词语的完整性。

### 问题以及解决：
  - 部分数据因为时间缺失无法划分，在此阶段筛去
  - 不同阶段的信息量存在明显差异，在最终数据可视化呈现中，通过情绪百分比对比表现情绪分布及对比
  - 数据筛选在阶段划分前实现，组织文件availcomments.csv，availnews.csv用于总体全面的数据分析
  - 获取不同层面的词频文件，根据总体意义上的高频词文件，结合阅读经验，建立自定义词典扩充分词词典，提高分词
  准确性
  - 通过停词库过滤停词，减少对词频的影响，综合中文停用词表 ，哈工大停用词表，百度停用词表，以及四川大学机器智能实验室停用词库四个停词库

## （三）机器学习（label.py, train.py, predict.py）
原定实现方法为基于心态词典的情感分析，后经过资料的查询以及建立心态词典的尝试，发现在建立多维情绪分析模
型时，心态词典根据词性，词义定义的加权计算规则较复杂，根据权值分析情感的效果不理想。最终确定为通过机器
学习进行心态预测。
### <1>样本标记
在总体有效数据中（评论），随机提取4000条内容，多人协作完成情感类型标记，label.py 实现终端人工阅读标记
对标记后的内容进行分词处理，存入对应标签的情绪样本文件emotion.txt
- 标记内容后分词处理以提高后续处理效率
### <2>样本预处理：
- 选取特征：通过【1】单字为特征，【2】双字为特征，【3】结合单、双字为特征，【4】根据结巴分词建立特征
  四种特征提取方式，结合卡方统计对数据进行降维，选取信息量前n位对应词作为特征，实验表明通过调整n至合
  适范围可以提高预测准确率，且四种模型中【4】的准确率显著高，结合不同学习模型不会对这一规律产生影响，
  n过大或过小都会降低准确率
  build_features()方法中设定n，选取特征方法会实现特征词的字典化格式处理
- 样本分割：根据“二八原则”，以20%的样本作为训练检测样本，80%的数据作为训练样本，根据实验结果知，过高
  过低的比重都会降低预测准确率

### <3>机器学习：
- 选取机器学习模型：【1】BernoulliNB，【2】MultinomiaNB，【3】LogisticRegression，【4】SVC，
 【5】LinearSVC 五种模型，分别结合上述四种提取方式，利用训练，预测测试选取最佳组合，提高预测准确率
  实验表明五种模型中【3】，【5】的准确率显著高于其他模型，两种模型准确率接近，最终选择LinearSVC作为
  训练模型
  ```python
  def score(classifier):    #传入选取的模型，最终返回训练过的模型用于预测
    classifier = SklearnClassifier(classifier)
    classifier.train(train)     #训练模型
    pred = classifier.classify_many(testdata) 
    #预测准确度检验
  ```
- 准确度检验：用训练过的模型预测训练检验样本，并将结果和人工标记进行对比，最终返回正确率

### <4>情感预测
- 格式预处理，将评论文件进行分词，字典化处理，转为机器学习方法需要的格式
```python
   for word, flag in words_list:
        if word not in stopwords:
             meaninful_words[word] = 'True'
   page.append(meaninful_words)
```

- 通过训练后的模型对各个阶段的评论进行情感类型预测，预测结果作为本次样本的分析结果
```python
    classifier = train.score(LinearSVC())[1]

    pred = classifier.classify_many(page)

    data['emotion'] = pred
```

## （四）数据可视化（views.py, views1.py, views2.py)
分别根据阶段评论情绪预测结果，阶段评论词云，通过pyechart制作情绪分布玫瑰图和词云图。
- 中性情感（“冷静”）：在人工标记时认为情感属于中性，即无明显情感取向的评论数量占有相当高的百分比。
  在图表中一定程度上影响了其他情感数据的展示，在views1.py中生成除去中性情感的图表，可提高较有特征性
  的情感分布展示效果
  ```python
    #in ./htmls/
    stage_rose_pie1.html  阶段情绪玫瑰图
    stage_rose_pie2.html     除去中性情绪的阶段情绪玫瑰图
    comment_stage_cloud.html     阶段评论词云
    news_stage_cloud.html     阶段新闻词云
    ```
