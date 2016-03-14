# -*- coding:utf-8 -*-

# 并查集


# n表示强盗的人数, m表示警方搜索到的m条线索
n, m = 10, 9
data_lst = []
data_str = '''1,2
3,4
5,2
4,6
2,6
8,7
9,7
1,6
2,4'''

for line in data_str.split('\n'):
    items = line.split(',')
    tup1 = (int(items[0]), int(items[1]))
    data_lst.append(tup1)


def merge(r_tuple):
    """
    :param r_tuple: 两元组
    :return:
    """
    t1 = get_father(r_tuple[0])
    t2 = get_father(r_tuple[1])

    if t1 != t2:
        f[t2] = t1

    return


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


print data_lst

# 初始化
f = [x for x in range(n + 1)]
print f

# 合并犯罪团伙
for t in data_lst:
    merge(t)

print f
