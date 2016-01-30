# -*- coding:utf-8 -*-

# 最少转机--图的广度优先搜索
# 广度优先搜索更加适用于所有边的权限相同的情况


class Node(object):
    """
    docs
    """

    def __init__(self, x=0, s=0):
        """
        :param x: 城市编号
        :param s: 转机次数
        :return:
        """

        self.x = x
        self.s = s


n = 5  # 图的顶点数
book = [0 for x in range(50)]
que = [Node() for x in range(401)]

# 初始化图的邻接矩阵
graphic = [[99999999 for x in range(n + 1)] for y in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graphic[i][i] = 0

# 读入顶点之间的边
points_edge_str = '''1,2
1,3
2,3
2,4
3,4
3,5
4,5'''

for line in points_edge_str.split('\n'):
    items = line.split(',')
    i, j = int(items[0]), int(items[1])
    graphic[i][j] = 1
    graphic[j][i] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print '%8d' % (graphic[i][j],),
    print

start, end = 1, 5

# 初始化队列
head, tail = 1, 1
que[tail].x = start
que[tail].s = 0
tail += 1
book[start] = 1

flag = 0

# 当队列不为空的时候循环
while head < tail:
    cur = que[head].x
    for j in range(1, n + 1):
        if graphic[cur][j] != 99999999 and book[j] == 0:
            que[tail].x = j
            que[tail].s = que[head].s + 1
            tail += 1
            book[j] = 1

        # 结束条件
        if que[tail - 1].x == end:
            flag = 1
            break

    if flag == 1:
        break

    head += 1

print '%d' % (que[tail - 1].s,)

for node in que:
    if node.x != 0:
        print '%d,%d' % (node.x, node.s)
