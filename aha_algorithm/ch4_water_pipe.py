# -*- coding:utf-8 -*-


class Node(object):
    """
    docs
    """
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y

s = []
top = 0


book = [[0 for x in range(51)] for y in range(51)]
pipe_map = [[0 for x in range(51)] for y in range(51)]
n, m = 5, 4
flag = 0

str_map = '''5353
1530
2351
6115
1554
'''
lines = str_map.split('\n')
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        pipe_map[i + 1][j + 1] = int(ch)

# for i in range(n):
#     for j in range(m):
#         print pipe_map[i+1][j+1],
#     print


def dfs(x, y, front):
    """
    :param x:
    :param y:
    :param front:
    :return:
    """

    if x == n and y == m + 1:
        global flag
        flag = 1
        for i in s:
            print '(%d,%d)' % (i.x, i.y),
        print
        return

    if x < 1 or x > n or y < 1 or y > m:
        return

    # 判断这个水管是否已经使用过
    if book[x][y] == 1:
        return

    book[x][y] = 1

    # 将当前坐标入栈
    s.append(Node(x, y))

    # print 'pipe_map[x][y] = %d' %(pipe_map[x][y],)
    # 当前水管是直管的情况
    if pipe_map[x][y] >= 5 and pipe_map[x][y] <= 6:

        # 进水口在左边的情况
        if front == 1:
            dfs(x, y + 1, 1)
        # 进水口在上边的情况
        if front == 2:
            dfs(x + 1, y, 2)
        # 进水口在右边的情况
        if front == 3:
            dfs(x, y - 1, 3)
        # 进水口在下边的情况
        if front == 4:
            dfs(x - 1, y, 4)

    # 当前水管是弯管的情况
    if pipe_map[x][y] >= 1 and pipe_map[x][y] <= 4:
        if front == 1:
            dfs(x + 1, y, 2)
            dfs(x - 1, y, 4)
        if front == 2:
            dfs(x, y + 1, 1)
            dfs(x, y - 1, 3)
        if front == 3:
            dfs(x - 1, y, 4)
            dfs(x + 1, y, 2)
        if front == 4:
            dfs(x, y + 1, 3)
            dfs(x, y - 1, 1)

    book[x][y] = 0

    # 将当前尝试的坐标出栈
    s.pop()
    return


dfs(1, 1, 1)
if flag == 1:
    print '找到铺设方案'
else:
    print '未找到铺设方案'
