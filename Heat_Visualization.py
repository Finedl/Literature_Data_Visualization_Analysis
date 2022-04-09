# 分析热图
# 对关键词在不同月份的频率进行统计分析

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 读取excel文件
df_2 = pd.read_csv('./heatmaps.csv', index_col='keyword')
fig = plt.figure(figsize=(15, 15))

ax  = fig.add_subplot(111)



plt.rc('font', family='Arial', size=8) #调整格子里面数字的大小

p1 = sns.heatmap(df_2, annot=True, vmin=0, vmax=6, fmt="d", linewidths=0, linecolor='#FFFFFF', cmap='jet', center=3,
                 square=True, cbar_kws={'shrink':0.3, 'aspect':10, 'pad':0.03}, annot_kws={'color':'black'}
                 )# )#WistiaRdBu_r

#不能分开画，还得放到一起。
camp = plt.get_cmap('Set3'),


# x和y轴的坐标设置
ax.set_xlabel('')
ax.set_ylabel('')

# 图片的保存
s1 = p1.get_figure()
# plt.show()
s1.savefig('./123.png', dpi=600, bbox_inches='tight')