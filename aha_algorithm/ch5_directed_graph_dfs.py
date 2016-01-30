# -*- coding:utf-8 -*-

# 深度优先遍历有向图

n = 5
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
1,5,10
2,3,3
2,5,7
3,1,4
3,4,4
4,5,5
5,3,3'''

for line in data_str.split('\n'):
    items = line.split(',')
    i, j = int(items[0]), int(items[1])
    dir_graph[i][j] = int(items[2])
    # dir_graph[j][i] = int(items[2]) # 无向图


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print '%8d' % (dir_graph[i][j],),
    print

def dfs(cur, dis):
    global min_distance
    if dis > min_distance:
        return

    if cur == n:

        if dis < min_distance:
            min_distance = dis

        return

    for j in range(1, n + 1):
        if dir_graph[cur][j] != 99999999 and book[j] == 0:
            book[j] = 1
            dfs(j, dis + dir_graph[cur][j])
            book[j] = 0

    return


book[1] = 1
dfs(1, 0)

print min_distance
