#生成阶段性评论热词词云
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import pandas as pd

#attr = Faker.choose()
tl = Timeline()
tl.add_schema(label_opts=opts.LabelOpts(font_size=10))

stage=['20191208-20200122',
       '20200123-20200207',
       '20200208-20200305',
       '20200306-20200618']

for i in stage:
    file = pd.read_csv('wdc/' + i + '(c)wdc.txt', encoding='utf-8', sep=" ")
    # print(file)
    file.columns = ['word', 'tag', 'times']
    word = list(file['word'])
    words_s=[]
    times = list(file['times'])
    words = list(zip(word, times))[:50]
    for w in words: #去除单字
        if len(w[0])>1:
            words_s.append(w)
    c = (
        WordCloud()
            .add("", words_s, word_size_range=[20, 100], shape=SymbolType.DIAMOND)

    ).set_global_opts(title_opts=opts.TitleOpts(title="WordCloud for {}".format(i)))



    tl.add(c,i)
tl.render("comment_stage_cloud.html")
