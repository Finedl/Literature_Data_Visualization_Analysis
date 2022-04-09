# 为每个年份创建词频字典
import pandas as pd
from nltk import word_tokenize

# 读取数据文件
dataset = pd.read_csv("./time.csv", header=0)
heatmap = pd.read_csv("./heatmap.csv", header=None)

# 清除空白日期行
dataset = dataset.dropna(axis=0, subset=['pub_year'])

dataset = dataset.iloc[:, :].values
heatmap = heatmap.iloc[:, :].values

for i in range(1, len(heatmap)):
    for j in range(1, len(heatmap[i])):
        heatmap[i][j] = 0

for i in range(len(dataset)):
    print(i)
    temp = 0
    for j in range(1, len(heatmap)):
        if dataset[i, 1] == heatmap[j][0]:
            for t in range(1, len(heatmap[j])):
                if int(dataset[i, 2]) == int(heatmap[0][t]):
                    heatmap[j][t] = heatmap[j][t] + 1
                    temp = 1
                    break
        if temp == 1:
            break


# 保存数据文件
dataframe = pd.DataFrame(heatmap)
dataframe.to_csv("./heatmaps.csv", index=False)



