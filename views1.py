from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
import pandas as pd
#去除中性情绪的玫瑰图
#attr = Faker.choose()
tl = Timeline()
tl.add_schema(label_opts=opts.LabelOpts(font_size=10))

stage=['20191208-20200122',
       '20200123-20200207',
       '20200208-20200305',
       '20200306-20200618']
attr=['angry','cold','excited','hopeful',
      'moved','sad','satisfied',
      'shock','suspicious','unsatisfied','worry']

attr1=['愤怒','冷漠','喜悦','振奋',
      '感动','悲伤','满足',
      '不满','震惊','怀疑','担忧']
time={stage[0]:{attr[0]:None,attr[1]:None,attr[2]:None,attr[3]:None,
                attr[4]:None,attr[5]:None,attr[6]:None,attr[7]:None,
                attr[8]:None,attr[9]:None,attr[10]:None,},
      stage[1]:{attr[0]:None,attr[1]:None,attr[2]:None,attr[3]:None,
                attr[4]:None,attr[5]:None,attr[6]:None,attr[7]:None,
                attr[8]:None,attr[9]:None,attr[10]:None,},
      stage[2]:{attr[0]:None,attr[1]:None,attr[2]:None,attr[3]:None,
                attr[4]:None,attr[5]:None,attr[6]:None,attr[7]:None,
                attr[8]:None,attr[9]:None,attr[10]:None,},
      stage[3]:{attr[0]:None,attr[1]:None,attr[2]:None,attr[3]:None,
                attr[4]:None,attr[5]:None,attr[6]:None,attr[7]:None,
                attr[8]:None,attr[9]:None,attr[10]:None,},}

for i in stage:
    file=pd.read_csv('analysis/'+i+'(a).csv',encoding='utf-8')
    file.columns= ['No','date', 'URL', 'content', 'numF','emotions']
    emo=list(file['emotions'])
    #print(emo)
    for e in attr:
        time[i][e]=emo.count(e)
print(time)
print(time[stage[0]])
print(zip(attr1,time[stage[0]].values()))

for i in stage:
    pie = Pie()

    pie.add(
            "情绪",

            [list(z) for z in zip(attr1, time[i].values())],
            rosetype="radius",
            radius=["35%", "65%"],
            center=["50%","50%"],
            label_opts=opts.LabelOpts(
                formatter= '{b}:{d}%:({c})'
            )


        ).set_global_opts(title_opts=opts.TitleOpts(title='{} 公众情绪分布情况'.format(i),
                                                    pos_top='top',
                                                    pos_left='center',

                                                    ),

                          legend_opts=opts.LegendOpts(pos_left='left',
                                                      pos_top='20%',
                                                      type_='scroll',
                                                      orient='vertical'),
                          )



    tl.add(pie,i)
tl.render("stage_rose_pie2.html")