# -*- coding:utf-8 -*-


class Node(object):
    """
    doc
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def get_num(i, j, maps):
    n = 0
    x, y = i, j
    while maps[x][y] != '#':
        if maps[x][y] == 'G':
            n += 1
        x -= 1

    x, y = i, j
    while maps[x][y] != '#':
        if maps[x][y] == 'G':
            n += 1
        x += 1

    x, y = i, j
    while maps[x][y] != '#':
        if maps[x][y] == 'G':
            n += 1
        y -= 1

    x, y = i, j
    while maps[x][y] != '#':
        if maps[x][y] == 'G':
            n += 1
        y += 1

    return n


que = [Node() for i in range(401)]
# print que[0].x, que[0].y
book = [[0 for x in range(20)] for y in range(20)]
max_num = 0
mx, my = 0, 0
next_step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 队列初始化
head, tail = 1, 1

# 初始化地图
str_map = '''#############
#GG.GGG#GGG.#
###.#G#G#G#G#
#.......#..G#
#G#.###.#G#G#
#GG.GGG.#.GG#
#G#.#G#.#.#.#
##G...G.....#
#G#.#G###.#G#
#...G#GGG.GG#
#G#.#G#G#.#G#
#GG.GGG#G.GG#
#############
'''

bomb_map = [['#' for x in range(13)] for y in range(13)]
lines = str_map.split('\n')
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        bomb_map[i][j] = ch



for i in range(len(bomb_map)):
    for j in range(len(bomb_map[i])):
        print bomb_map[i][j],
    print

startx, starty = 3, 3

que[tail].x = startx
que[tail].y = starty
tail += 1
book[startx][starty] = 1

max_num = get_num(startx, starty, bomb_map)

mx = startx
my = starty

n, m = 13, 13

while head < tail:
    for k in range(4):
        tx = que[head].x + next_step[k][0]
        ty = que[head].y + next_step[k][1]

        # 判断是否越界
        if tx < 0 or tx > n - 1 or ty < 0 or ty > m - 1:
            continue

        # 判断是否为平地或者已经走过
        # print bomb_map[tx][ty]
        if bomb_map[tx][ty] == '.' and book[tx][ty] == 0:
            book[tx][ty] = 1
            que[tail].x = tx
            que[tail].y = ty
            tail += 1

            # 统计当前新扩展的点可以消灭的敌人数
            sums = get_num(tx, ty, bomb_map)

            if sums > max_num:
                max_num = sums
                mx = tx
                my = ty

    head += 1

print "将炸弹放置在(%d,%d)处，可以消灭%d个敌人" % (mx, my, max_num)