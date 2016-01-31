# -*- coding:utf-8 -*-

# floyd-warshall 多源最短路径

n = 4
min_distance = 99999999
book = [0 for x in range(20)]

# 初始化图的邻接矩阵
dir_graph = [[99999999 for x in range(n + 1)] for y in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            dir_graph[i][i] = 0

# a,b,c 表示a到b城市的里程为c
data_str = '''1,2,2
1,3,6
1,4,4
2,3,3
3,1,7
3,4,1
4,1,5
4,3,12'''

for line in data_str.split('\n'):
    items = line.split(',')
    i, j = int(items[0]), int(items[1])
    dir_graph[i][j] = int(items[2])
    # dir_graph[j][i] = int(items[2]) # 无向图

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print '%8d' % (dir_graph[i][j],),
    print

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dir_graph[i][j] > dir_graph[i][k] + dir_graph[k][j]:
                dir_graph[i][j] = dir_graph[i][k] + dir_graph[k][j]

    print '-' * 50
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print '%8d' % (dir_graph[i][j],),
        print
