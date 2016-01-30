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


def dfs_adventure(x, y):
    next_step = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for k in range(4):
        tx = x + next_step[k][0]
        ty = y + next_step[k][1]

        if tx < 1 or tx > n or ty < 1 or ty > m:
            continue

        if island_map[tx][ty] > 0 and book[tx][ty] == 0:
            global sums
            sums += 1
            book[tx][ty] = 1
            dfs_adventure(tx, ty)

    return


startx, starty = 6, 8
sums = 1
book[startx][starty] = 1
dfs_adventure(startx, starty)
print 'area:', sums
