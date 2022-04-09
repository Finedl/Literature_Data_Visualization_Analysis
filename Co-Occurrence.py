# 词频共现图
# 主要用于将现有的关键词与系统关键词进行对比分析=

import networkx as nx
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nxviz.plots import CircosPlot

# 打开文件数据
df_2 = pd.read_csv('./Co_score.csv', header=0)
interactions = df_2[['keyword_1', 'keyword_2', 'score']]

cipin = pd.read_csv('./co-data.csv', header=0)
cipin_data = cipin.iloc[:50, :].values

ci_dict = {}
for i in range(len(cipin_data)):
    ci_dict[cipin_data[i][0]] = cipin_data[i][1]

print(ci_dict)


# 高级边缘处理
G = nx.Graph(name='New Crown Keyword Relationship Network')
interactions = np.array(interactions)  # convert to array for clarity
for i in range(len(interactions)):
    interaction = interactions[i]
    a = interaction[0]  # protein a node
    b = interaction[1]  # protein b node
    w = interaction[2]

    # To only keep high scoring edges, use the following lines
    if w > 0:  # only keep high scoring edges
        G.add_weighted_edges_from([(a, b, w)])

# 高级图像绘制
def rescale(l,newmin,newmax,rnd=False):
    arr = list(l)
    return [round((x-min(arr))/(max(arr)-min(arr))*(newmax-newmin)+newmin, 2) for x in arr]

nodelist = [n for n in G.nodes]

# ws = rescale([float(G[u][v]['weight']) for u, v in G.edges], 1, 10)

ws = [float(G[u][v]['weight']) for u, v in G.edges]
edge_width = rescale(ws, 3, 10)

# alternative method below
# ws = rescale([float(G[u][v]['weight'])**70 for u, v in G.edges], 1, 10)
edgelist = [(str(u), str(v), {"weight": ws.pop(0)}) for u, v in G.edges]


edges = G.edges()

# create new graph using nodelist and edgelist
g = nx.Graph(name='Protein Interaction Graph')

g.add_nodes_from(nodelist)
g.add_edges_from(edgelist)


for v in G:
    g.nodes[v]["class"] = ci_dict[v]


# 图像展示
c = CircosPlot(graph=g, figsize=(10, 10), node_grouping='class', node_color='class',
               edge_width=edge_width, node_labels=True, node_label_layout='rotation', edge_color='weight')

c.draw()
plt.savefig("./co-occurrence.png", dpi=600)
plt.show()