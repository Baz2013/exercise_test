# -*- coding:utf-8 -*-

# Dijkstra 算法 - 单源最短路径
# 用邻接表存储图 (数组实现)

# n 个顶点 m 个边 (有向边)
n = 6
m = 5

# a,b,c 表示a到b城市的里程为c
data_str = '''1,4,9
4,3,8
1,2,5
2,4,6
1,3,7'''

v = [0 for x in range(6)]
u = [0 for x in range(6)]
w = [0 for x in range(6)]

first = [-1 for x in range(6)]
# next_edge[i] 编号为i的边的下一条边的编号
next_edge = [-1 for x in range(6)]

i = 1
for line in data_str.split('\n'):
    items = line.split(',')
    u[i], v[i], w[i] = int(items[0]), int(items[1]), int(items[2])
    next_edge[i] = first[u[i]]
    first[u[i]] = i
    i += 1

print u, v, w, first, next_edge
