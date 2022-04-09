# 每年各个国家的文章数量
import pandas as pd

# 读取数据文件
dataset = pd.read_csv("./address_time.csv", header=0)

# 清除空白日期行
dataset = dataset.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# 读取各字段
for i in range(len(dataset.columns)):
    if dataset.columns[i] == "document_unique_id":
        paper_id_list = dataset.iloc[:, i].values
    elif dataset.columns[i] == "pub_year":
        year_list = dataset.iloc[:, i].values
    elif dataset.columns[i] == "address":
        address_list = dataset.iloc[:, i].values

# 提取作者国家
or_address = address_list
country_list = []
for i in or_address:
    re_address = ""
    for j in range(len(i)-1, -1, -1):
        if i[j] != " ":
            re_address = re_address+i[j]
        else:
            break
    re_address = re_address[::-1]
    country_list.append(re_address)

# 年份
year = []
for i in range(len(dataset)):
    if year_list[i] not in year:
        year.append(year_list[i])

# 国家
country = []
for i in range(len(dataset)):
    if country_list[i] not in country:
        country.append(country_list[i])

# 添加年份、国家组合
matrix = [[0 for j in range(len(year)+1)] for i in range(len(country)+1)]
matrix[0][1:] = year
matrix = list(map(list, zip(*matrix)))
matrix[0][1:] = country
matrix[0][0] = "country"

# 统计数量
for i in range(len(dataset)):
    for j in range(1, len(matrix[0])):
        if country_list[i] == matrix[0][j]:
            for z in range(1, len(matrix)):
                if year_list[i] == matrix[z][0]:
                    matrix[z][j] = matrix[z][j] + 1

year_country = []
for i in range(len(matrix[0])):
    re_year_country = []
    for j in range(len(matrix)):
        re_year_country.append(matrix[j][i])
    year_country.append(re_year_country)


year_country = pd.DataFrame(year_country)
# year_country.columns = ['country', '2021', '2020']
year_country.to_csv('./number_of_articles_by_country_per_year.csv', index=False, header=0)