import matplotlib
from matplotlib import cm
from nltk import word_tokenize
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('./number_of_country_articles.csv', header=0)
data = data.iloc[:9, :16].values

country_date_count = [['中国'], ['美国'], ['英国'], ['澳大利亚'], ['法国'], ['日本'], ['其它国家']]
x = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
              '2017', '2018', '2019', '2020', '2021']

num = []
for i in range(len(data)-1):
     a = []
     for j in range(1, len(data[i])):
          a.append(data[i][j])
     num.append(a)

list_num = []
for i in range(1, len(data[-1])):
     list_num.append(data[-1][i])

y = []
for i in range(len(num)):
    y_t = []
    for j in range(len(num[i])):
        y_t.append(float(100*(num[i][j]/list_num[j])))
    y.append(y_t)

cmap = cm.get_cmap("viridis", 7)
colors = cmap(np.linspace(0, 1, len(country_date_count)))

# 百分比图
for i in range(len(country_date_count)):
    if i == 0:
        plt.bar(x, y[i], label=country_date_count[i][0], color=colors[i])
    else:
        bottom = np.array(y[0])
        for j in range(1, i):
            y[j] = np.array(y[j])
            bottom = bottom + y[j]
        plt.bar(x, y[i], bottom=bottom, label=country_date_count[i][0], color=colors[i])
matplotlib.rcParams['font.family']='SimHei'#修改了全局变量
plt.ylim(0, 100)
# 添加图例
plt.legend(bbox_to_anchor=(1, 1.01), loc='lower right', borderaxespad=0, ncol=7)
plt.xlim(-1, 15)
# plt.ylabel("发表论文的百分比 (%)", size=20, family='Arial')
plt.ylabel("发表论文的百分比 (%)", size=20, fontproperties='SimHei')
plt.xticks(rotation=60, size=15, family='Arial')
plt.yticks(size=15, family='Arial')

plt.show()
