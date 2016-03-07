# -*- coding:utf-8 -*-


def shift_down(r_heap, r_pos):
    """
    向下调整小顶堆
    :param r_heap: 小顶堆(数组)
    :param r_pos: 向下调整的结点编号,1 即从堆的顶点开始向下调整
    :return: 返回一个新的小顶堆
    """

    t, flag = 0, 0
    h_len = len(r_heap) - 1
    new_heap = r_heap

    i = r_pos
    while 2 * i <= h_len and flag == 0:
        # 判断当前顶点和其左孩子的关系,并用t记录较小的结点编号
        if r_heap[i] > r_heap[2 * i]:
            t = i * 2
        else:
            t = i

        # 如果当前结点有右儿子,再对右儿子进行讨论
        if i * 2 + 1 <= h_len:
            # 如果右儿子的值更小,更新较小的结点编号
            if r_heap[t] > r_heap[2 * i + 1]:
                t = i * 2 + 1
            else:
                pass

        if t != i:
            new_heap[t], new_heap[i] = new_heap[i], new_heap[t]
            i = t
        else:
            flag = 1

    return new_heap


def shift_up(r_heap, r_pos):
    """
    向上调整小顶堆
    :param r_heap:小顶堆(数组)
    :param r_pos:向上调整的结点编号
    :return: 新的小顶堆
    """

    new_heap = r_heap
    flag = 0
    if r_pos == 1:
        return new_heap

    i = r_pos
    while i != 1 and flag == 0:

        # 判断是否比父节点小
        if r_heap[i] < r_heap[i / 2]:
            new_heap[i], new_heap[i / 2] = new_heap[i / 2], new_heap[i]
        else:
            flag = 1

        i /= 2

    return new_heap


def create_heap(r_lst):
    """
    创建小顶堆
    :param r_lst: 元素列表
    :return: 创建好的小顶堆
    """
    new_heap = [0]
    for i in r_lst:
        new_heap.append(i)
        new_heap = shift_up(new_heap, len(new_heap) - 1)

    return new_heap


def create_heap1(r_lst):
    """
    利用完全二叉树创建小顶堆
    :param r_lst: 一个用数组表示的完全二叉树
    :return: 创建好的小顶堆
    """
    new_heap = r_lst
    new_heap.insert(0, 0)
    n = len(r_lst) - 1
    i = n / 2
    while i >= 1:
        # print i
        new_heap = shift_down(new_heap, i)
        i -= 1

    return new_heap


def delete_min(r_heap):
    if len(r_heap) <= 1:
        return None, r_heap

    t = r_heap[1]
    r_heap[1] = r_heap[len(r_heap) - 1]
    r_heap = r_heap[0:-1]
    new_heap = shift_down(r_heap, 1)

    return t, new_heap


def heap_sort(r_heap):
    """
    堆排序
    :param r_heap:
    :return:
    """
    sorted_lst = []
    t, new_heap = delete_min(r_heap)
    while t is not None:
        # print new_heap
        sorted_lst.append(t)
        t, new_heap = delete_min(new_heap)

    return sorted_lst


if __name__ == '__main__':
    # small_heap = [0, 1, 2, 5, 12, 7, 17, 25, 19, 36, 99, 22, 28, 46, 92]
    # small_heap[1] = 23
    # small_heap1 = shift_down(small_heap, 1)
    # print small_heap1
    # small_heap1.append(3)
    # small_heap2 = shift_up(small_heap1, len(small_heap1) - 1)
    # print small_heap2
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    lst.reverse()
    s_heap = create_heap(lst)
    print s_heap

    s1_heap = create_heap1(lst)
    print 's1_heap', s1_heap

    # h_min, s1_heap = delete_min(s1_heap)
    # print h_min
    # print s1_heap
    # h_min, s1_heap = delete_min(s1_heap)
    # print h_min
    # print s1_heap
    print heap_sort(s1_heap)

    lst2 = [99, 5, 36, 7, 22, 17, 46, 12, 2, 19, 25, 28, 1, 92]
    s2_heap = create_heap1(lst2)
    print 's2_heap', s2_heap
    print heap_sort(s2_heap)
