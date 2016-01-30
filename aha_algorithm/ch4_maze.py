#-*- coding:utf-8 -*-

"""
基于深度优先搜索的迷宫求解算法
"""

n = 0
m = 0
p = 0
q = 0
min_step = 0

a = [[0 for col in range(6)] for row in range(7)]
book = [[0 for col in range(6)] for row in range(7)]


def dfs(x, y, step):
    next_step = [(0,1), (1,0), (0,-1), (-1,0)]

    global min_step
    if x == p and y == q:
        if step < min_step:
            min_step = step
        return

    for k in range(0, 4):
        tx = x + next_step[k][0]
        ty = y + next_step[k][1]

        if tx < 1 or tx > n or ty < 1 or ty > m:
            continue

        print '----->', book
        if a[tx][ty] == 0 and book[tx][ty] == 0:
            book[tx][ty] = 1
            dfs(tx, ty, step + 1)
            book[tx][ty] = 0

    return

if __name__ == '__main__':
    n, m = 5, 4
    min_step = 9999999
    #设置障碍物
    a[1][3], a[3][3], a[4][2], a[5][4] = 1, 1, 1, 1
    print a
    #设置终点
    p, q = 4, 3
    book[1][1] = 1
    dfs(1, 1, 0)

    print min_step





