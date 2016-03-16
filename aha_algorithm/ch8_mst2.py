# -*- coding:utf-8 -*-

# minimal spanning tree -> MST
# Prim 算法

# 初始化

# n表示顶点数,m表示边的条数
n, m = 6, 9
book = [0 for x in range(n + 1)]
# 记录生成树中顶点的个数
count = 0
j = 0
# 存储路径之和
sum = 0

# 表示正无穷值
inf = 99999999
graphic = [[inf for x in range(n + 1)] for y in range(n + 1)]

str_data = '''2,4,11
3,5,13
4,6,3
5,6,4
2,3,6
4,5,7
1,2,1
3,4,9
1,3,2'''

for line in str_data.split('\n'):
    items = line.split(',')
    graphic[int(items[0])][int(items[1])] = int(items[2])
    graphic[int(items[1])][int(items[0])] = int(items[2])

dis = [graphic[1][x] for x in range(n + 1)]

print dis


# Prim 核心部分
# 将1号顶点加入到生成树
book[1] = 1
count += 1

while count < n:
    min = inf
    for i in range(1, n + 1):
        if book[i] == 0 and dis[i] < min:
            min = dis[i]
            j = i

    book[j] = 1
    count += 1
    sum += dis[j]

    # 扫描当前顶点j所有的边 再以j为中间点 更新生成树到每一个非树顶点的距离
    for k in range(1, n + 1):
        if book[k] == 0 and dis[k] > graphic[j][k]:
            dis[k] = graphic[j][k]

    print j,dis

print count,sum