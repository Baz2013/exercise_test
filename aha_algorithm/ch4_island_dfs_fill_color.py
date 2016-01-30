# -*- coding:utf-8 -*-

sums = 0
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

n, m = 10, 10


def dfs_adventure(x, y, color):
    next_step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    island_map[x][y] = color
    for k in range(4):
        tx = x + next_step[k][0]
        ty = y + next_step[k][1]

        if tx < 1 or tx > n or ty < 1 or ty > m:
            continue

        if island_map[tx][ty] > 0 and book[tx][ty] == 0:
            global sums
            sums += 1
            book[tx][ty] = 1
            dfs_adventure(tx, ty, color)

    return


# startx, starty = 6, 8
# sums = 1
# book[startx][starty] = 1
# dfs_adventure(startx, starty)
# print 'area:', sums
num = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if island_map[i][j] > 0:
            num -= 1
            book[i][j] = 1
            dfs_adventure(i, j, num)

print '-----after fill color ,island map----------'
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print '%3d' % (island_map[i][j],),
    print
