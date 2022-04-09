import pandas as pd
import numpy as np

# 读取关键词
dataset = pd.read_csv("./keyword_final.csv", header=0)
data = dataset.iloc[:, :].values
paper_id = data[:, 1]
or_keyword = data[:, 2]

# 词频统计
dict_keyword = {}
for i in range(len(or_keyword)):
    if or_keyword[i] in dict_keyword:
        dict_keyword[or_keyword[i]] = dict_keyword[or_keyword[i]]+1
    else:
        dict_keyword[or_keyword[i]] = 1

# 字典排序
sort_dict = sorted(dict_keyword.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
sort_dict = np.array(sort_dict)
hight_fre_keyword = []                              # 前50个高频词
for i in range(0, 50):
    hight_fre_keyword.append(sort_dict[i, 0])

# 创建每篇文章的关键词组合
paper_keyword = []                                  # 所有文章的ID与keyword组合
keyword_data = [paper_id[0]]                        # 每篇文章的ID与keyword
every_paper_id = paper_id[0]

for i in range(len(data)):
    if paper_id[i] == every_paper_id:
        keyword_data.append(or_keyword[i])
    else:
        paper_keyword.append(keyword_data)
        every_paper_id = paper_id[i]
        keyword_data = [paper_id[i]]
        keyword_data.append(or_keyword[i])

# dataset = pd.read_csv("C:/Users/Tom/Desktop/co-data.csv", header=None)
# hight_fre_keyword = dataset.iloc[:, 0].values

# 创建二维矩阵
edge = len(hight_fre_keyword)+1
matrix = [['' for j in range(edge)] for i in range(edge)]
matrix[0][1:] = hight_fre_keyword
matrix = list(map(list, zip(*matrix)))
matrix[0][1:] = hight_fre_keyword
for i in range(1, edge):
    for j in range(1, edge):
        matrix[i][j] = int(0)

# 计算共现次数
for i in range(1, len(matrix)):                            # 循环matrix的行名
    for j in range(1, len(matrix)):                        # 循环matrix的列名
        keyword_1 = matrix[i][0]                           # keyword_1为行名
        keyword_2 = matrix[0][j]                           # keyword_2为列名

        for k in range(len(paper_keyword)):                # 遍历每篇文章的关键词
            keyword_list = paper_keyword[k][1:]
            if keyword_1 in keyword_list and keyword_2 in keyword_list:
                matrix[i][j] = matrix[i][j]+1

for i in range(1, len(matrix)):
    for j in range(1, len(matrix)):
        if i == j:
            matrix[i][j] = 0

matrix = np.array(matrix)

# 转化为二维数组
Co_occ_score = []
for i in range(1, len(matrix)):
    for j in range(i, len(matrix)):
        keyword_combin = []
        keyword_combin.append(matrix[i, 0])
        keyword_combin.append(matrix[0, j])
        keyword_combin.append(int(matrix[i, j]))
        Co_occ_score.append(keyword_combin)

# 按照共现次数排序
Co_occ_score = sorted(Co_occ_score, key=lambda x:x[2])

Co_score = []
for i in range(len(hight_fre_keyword)):
    keyword = hight_fre_keyword[i]
    for j in range(len(Co_occ_score)):
        for z in range(len(Co_occ_score[j])-1):
            if Co_occ_score[j][z] == keyword and Co_occ_score[j] not in Co_score:
                Co_score.append(Co_occ_score[j])
                break

# 保存数据文件
dataframe = pd.DataFrame(Co_score)
dataframe.columns = ['keyword_1', 'keyword_2', 'score']
dataframe.to_csv("./Co_score.csv", index=False)