# 总的词频统计
import pandas as pd

# 读取数据文件
dataset = pd.read_csv("./keyword_final.csv", header=0)

# 读取各字段
for i in range(len(dataset.columns)):
    if dataset.columns[i] == "keyword":
        keyword_list = dataset.iloc[:, i].values

# 统计词频
counts = {}
for keyword in keyword_list:
    counts[keyword] = counts.get(keyword, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(len(items)):
    items[i] = list(items[i])

data = pd.DataFrame(items)
data.columns = ['keyword', 'frequency']
data.to_csv("./total_word_frequency.csv", index=False)
