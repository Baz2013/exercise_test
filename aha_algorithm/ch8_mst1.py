# -*- coding:utf-8 -*-

# minimal spanning tree -> MST
# Kruskal 算法

class Edge(object):
    """
       docs
    """

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def quick_sort(left, right):
    """
    快速排序
    :param left:
    :param right:
    :return:
    """
    if left > right:
        return
    i = left
    j = right

    while i != j:
        # 先从右边开始找(顺序很重要)
        while edges[j].w >= edges[left].w and i < j:
            j -= 1

        while edges[i].w <= edges[left].w and i < j:
            i += 1

        if i < j:
            edges[i], edges[j] = edges[j], edges[i]

    # 最终将基准数据归位, 将left和i互换
    edges[i], edges[left] = edges[left], edges[i]
    quick_sort(left, i - 1)
    quick_sort(i + 1, right)

    return


# 初始化边
n, m = 6, 9
edges = []

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
    one_edge = Edge(int(items[0]), int(items[1]), int(items[2]))
    edges.append(one_edge)

# print edges
sum, count = 0, 0
f = [x for x in range(n + 1)]

def get_father(v):
    """

    :param v:
    :return:
    """
    if f[v] == v:
        return v
    else:
        f[v] = get_father(f[v])
        return f[v]

def merge(v, u):
    """
    并查集合并两个子集的函数
    :param v:
    :param u:
    :return:
    """
    t1 = get_father(v)
    t2 = get_father(u)

    if t1 != t2:
        f[t2] = t1
        return True

    return False

if __name__ == '__main__':
    # 按照权值从小到大对边进行排序
    quick_sort(0, len(edges) - 1)

    # Kruskal 算法核心部分
    for edge in edges:
        # 判断一条边的两个顶点是否已经连通,即判断是否在同一个集合
        # print edge.u,edge.v,edge.w
        if merge(edge.u, edge.v):
            count += 1
            sum += edge.w
            print edge.u,edge.v,edge.w

        if count == n - 1:
            break


print sum,count