import pandas as pd
from nltk.stem import WordNetLemmatizer
import numpy as np
from nltk import SnowballStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords

# 读取关键词
dataset = pd.read_csv("./wos_keyword.csv", header=0)
data = dataset.iloc[:, :].values
or_keyword = data[:, -1]

# 去掉词间的横杠
def del_bar(keyword):
    for i in range(len(keyword)):
        for j in range(len(keyword[i])):
            if keyword[i][j] == '-':
                keyword[i][j] = ' '
    return keyword

# 词干提取
def stem(or_keyword):
    ste_keyword = []
    stemmer = SnowballStemmer('english')
    for i in range(len(or_keyword)):
        inv_keyword = word_tokenize(or_keyword[i])
        re_keyword = ""
        for j in range(len(inv_keyword)):
            keyword = stemmer.stem(inv_keyword[j])
            # keyword = inv_keyword[j]
            for z in keyword:
                if (z != "'"):
                    re_keyword = re_keyword + z
            re_keyword = re_keyword + " "
        ste_keyword.append(re_keyword)
    return ste_keyword

# 词形还原
def lemmatization(ste_keyword):
    lemma_keyword = []
    wordnet_lematizer = WordNetLemmatizer()
    for i in range(len(ste_keyword)):
        inv_keyword = word_tokenize(or_keyword[i])
        re_keyword = ""
        for j in range(len(inv_keyword)):
            word_lematizer = wordnet_lematizer.lemmatize(inv_keyword[j])
            re_keyword = re_keyword+word_lematizer
            re_keyword = re_keyword+" "
        lemma_keyword.append(re_keyword)
    return lemma_keyword

# 去掉停用词
def delete_stopwords(ste_keyword):
    sto_keyword = []
    stop_words = set(stopwords.words("english"))
    for i in ste_keyword:
        word_tokens = word_tokenize(i)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        re_keyword = ""
        for j in filtered_sentence:
            re_keyword = re_keyword + j
            re_keyword = re_keyword + " "
        sto_keyword.append(re_keyword)
    return sto_keyword

# 判断是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# 特殊字符
characters = [' ', ',', '.', 'DBSCAN', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '-', '...',
              '^', '{', '}', '`', '< /bold > ']

# 去除数字与字符
def delete_characters(sto_keyword):
    non_num_char_keyword = []
    for i in sto_keyword:
        word_tokens = word_tokenize(i)
        words_list = [word for word in word_tokens if word not in characters and not is_number(word)]
        re_keyword = ""
        for j in words_list:
            re_keyword = re_keyword+j
            re_keyword = re_keyword+" "
        non_num_char_keyword.append(re_keyword)
    return non_num_char_keyword

# 删除特定前缀
def delete_prefix(non_num_char_keyword):
    for i in range(len(non_num_char_keyword)):
        keyword = non_num_char_keyword[i]
        if keyword[:4] == "beta":
            non_num_char_keyword[i] = keyword[4:]
        elif keyword[:5] == "alpha" or keyword[:5] == "gamma":
            non_num_char_keyword[i] == keyword[5:]
    non_prefix_keyword = non_num_char_keyword
    return non_prefix_keyword

# 删除特定首词
def delete_initial_words(non_prefix_keyword):
    initial_words = ['contaminated', 'environmental', 'polluted']
    non_ini_keyword = []
    for i in non_prefix_keyword:
        word_tokens = word_tokenize(i)
        re_keyword = ""
        if len(word_tokens) > 1:
            if word_tokens[0] in initial_words:
                word_tokens = word_tokens[1:]
        for j in word_tokens:
            re_keyword = re_keyword + j
            re_keyword = re_keyword + " "
        non_ini_keyword.append(re_keyword)
    return non_ini_keyword

# 删除特定尾词
def delete_ending_words(non_ini_keyword):
    ending_words = ['atom', 'concentration', 'concentrations', 'emission', 'emissions',
                    'formation', 'ion', 'ions', 'level', 'levels', 'production', 'reduction', 'removal']
    non_end_keyword = []
    for i in non_ini_keyword:
        word_tokens = word_tokenize(i)
        re_keyword = ""
        if len(word_tokens) > 1:
            if word_tokens[-1] in ending_words:
                word_tokens = word_tokens[:-1]
        for j in word_tokens:
            re_keyword = re_keyword + j
            re_keyword = re_keyword + " "
        non_end_keyword.append(re_keyword)
    return non_end_keyword

# 取出关键最后的空格
def delete_space(non_end_keyword):
    for i in range(len(non_end_keyword)):
        keyword = non_end_keyword[i]
        if keyword != "":
            if keyword[-1] == ' ':
                non_end_keyword[i] = keyword[:-1]
    return non_end_keyword

# 删除空白关键词相关的行
def delete_blank(data, non_end_keyword):
    all_data = data
    all_data[:, -1] = non_end_keyword
    i = 0
    while i < len(all_data):
        if all_data[i, -1] == "":
            all_data = np.delete(all_data, i, 0)
            i = i-1
        else:
            i = i+1
    return all_data

# 提取作者国家
def get_country(all_data):
    or_address = all_data[:, -1]
    country = []
    for i in or_address:
        re_address = ""
        for j in range(len(i)-1, -1, -1):
            if i[j] != " ":
                re_address = re_address+i[j]
            else:
                break
        re_address  = re_address[::-1]
        country.append(re_address)
    all_data[:, -1] = country
    return all_data

# 主函数
if __name__ == '__main__':
    ste_keyword = stem(or_keyword)
    # lemma_keyword = lemmatization(ste_keyword)
    sto_keyword = delete_stopwords(ste_keyword)
    non_num_char_keyword = delete_characters(sto_keyword)
    # non_prefix_keyword = delete_prefix(non_num_char_keyword)
    # non_ini_keyword = delete_initial_words(non_prefix_keyword)
    # non_end_keyword = delete_ending_words(non_ini_keyword)
    non_end_keyword = delete_space(non_num_char_keyword)
    end_data = delete_blank(data, non_end_keyword)
    # final_data = get_country(end_data)

# 保存数据文件
dataframe = pd.DataFrame(end_data)
dataframe.columns = ['keyword_id', 'document_unique_id', 'keyword']
dataframe.to_csv("./keyword_final.csv", index=False)






