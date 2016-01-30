#-*- coding:utf-8 -*-

"""
 基于广度优先搜索的迷宫求解算法
"""


class node(object):

    def __init__(self, x=0, y=0, f=0, s=0):
        self.x = x
        self.y = y
        self.f = f
        self.s = s

que = [node() for x in range(50)]
a = [[0 for x in range(6)] for y in range(7)]
book = [[0 for x in range(6)] for y in range(7)]

next_step = [(0,1), (1,0), (0,-1), (-1,0)]

head, tail = 1, 1

##设置障碍物
a[1][3], a[3][3], a[4][2], a[5][4] = 1, 1, 1, 1

n, m = 5,4

##设置终点
p, q = 4, 3

que[tail].x = 1
que[tail].y = 1
que[tail].f = 0
que[tail].s = 0

tail += 1
book[1][1] = 1

flag = 0

#########start
while head < tail:
    for k in range(4):
        tx = que[head].x + next_step[k][0]
        ty = que[head].y + next_step[k][1]
        # 判断是否越界
        if tx < 1 or tx > n or ty < 1 or ty > m:
            continue

        # 判断是否是障碍物或者已经在路径中
        if a[tx][ty] == 0 and book[tx][ty] == 0:
            book[tx][ty] = 1
            que[tail].x = tx
            que[tail].y = ty
            que[tail].f = head
            que[tail].s = que[head].s + 1
            tail += 1

        if tx == p and ty == q:
            flag = 1
            break
    if 1 == flag:
        break

    head += 1

print que[tail - 1].s

