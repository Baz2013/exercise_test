# -*- coding:utf-8 -*-

n = 5  # 图的顶点数
book = [0 for x in range(20)]
sums = 0


# 初始化图的邻接矩阵
graphic = [[99999999 for x in range(n + 1)] for y in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graphic[i][i] = 0

# 读入顶点之间的边
points_edge_str = '''1,2
1,3
1,5
2,4
3,5'''

for line in points_edge_str.split('\n'):
    items = line.split(',')
    i, j = int(items[0]), int(items[1])
    graphic[i][j] = 1
    graphic[j][i] = 1

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print '%8d' % (graphic[i][j],),
#     print


def dfs(cur):
    print 'current point: %d' % (cur,)
    global sums
    sums += 1

    if sums == n:
        return

    for i in range(1, n + 1):
        if graphic[cur][i] == 1 and book[i] == 0:
            book[i] = 1
            dfs(i)

book[1] = 1
dfs(1)
