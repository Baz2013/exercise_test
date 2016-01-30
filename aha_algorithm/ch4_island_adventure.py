# -*- coding:utf-8 -*-


class Node(object):
    """
    docs
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


que = [Node() for x in range(2501)]
book = [[0 for x in range(51)] for y in range(51)]
island_map = [[0 for x in range(51)] for y in range(51)]

str_map = '''1210000023
3020121012
4010123201
3200012400
0000001530
0121015430
0123136210
0034897500
0003786012
0000000010
'''
lines = str_map.split('\n')
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        island_map[i + 1][j + 1] = int(ch)

print '-----island map----------'
for i in range(1, 11):
    for j in range(1, 11):
        print island_map[i][j],
    print

# 队列初始化
head, tail = 1, 1
# 降落的起始坐标
startx, starty = 6, 8
que[tail].x = startx
que[tail].y = starty
tail += 1
book[startx][starty] = 1

next_step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n, m = 10, 10
sums = 1


while head < tail:

    for k in range(4):
        tx = que[head].x + next_step[k][0]
        ty = que[head].y + next_step[k][1]

        if tx < 1 or tx > n or ty < 1 or ty > m:
            continue

        if island_map[tx][ty] > 0 and book[tx][ty] == 0:
            print sums
            sums += 1
            book[tx][ty] = 1
            que[tail].x = tx
            que[tail].y = ty
            tail += 1

    head += 1

print 'island area is :%d' % (sums, )