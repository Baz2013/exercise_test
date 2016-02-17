# -*- coding:utf-8 -*-

# Dijkstra 算法 - 单源最短路径

# book[i] == 1 表示 已知最短路径的几点集合P
# book[i] == 0 表示 未知最短路径的几点集合Q
book = [0 for x in range(20)]

# n 个顶点 m 个边 (有向边)
n = 6
m = 9

# 初始化图的邻接矩阵
dir_graph = [[99999999 for x in range(n + 1)] for y in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dir_graph[i][i] = 0

# a,b,c 表示a到b城市的里程为c
data_str = '''1,2,1
1,3,12
2,3,9
2,4,3
3,5,5
4,3,4
4,5,13
4,6,15
5,6,4'''

for line in data_str.split('\n'):
    items = line.split(',')
    i, j = int(items[0]), int(items[1])
    dir_graph[i][j] = int(items[2])
    # dir_graph[j][i] = int(items[2]) # 无向图

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print '%8d' % (dir_graph[i][j],),
    print

# 初始化dis数组,这里是1号顶点到其余各个顶点的初始路程
dis = []
for i in range(n + 1):
    dis.append(dir_graph[1][i])

# print len(dis)

# dijkstra 算法核心语句
for i in range(1, n):

    # 找到离1号顶点最近的顶点
    min_distance = 99999999
    for j in range(1, n + 1):
        if book[j] == 0 and dis[j] < min_distance:
            min_distance = dis[j]
            u = j
        else:
            pass

    book[u] = 1
    for v in range(1, n + 1):
        if dir_graph[u][v] < 99999999:
            if dis[v] > dis[u] + dir_graph[u][v]:
                dis[v] = dis[u] + dir_graph[u][v]
            else:
                pass
        else:
            pass


# 输出最终的结果
print '-'*120
for i in range(1, len(dis)):
    print dis[i],
