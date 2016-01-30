# -*- coding:utf-8 -*-


def kmpSearch(src_str, p_str, next):
    """
    :param src_str: 匹配串
    :param p_str: 模式串
    :param next: next数组
    :return: 成功 返回匹配串中的位置，失败 返回-1
    """

    i = 0
    j = 0
    slen = len(src_str)
    plen = len(p_str)
    nlen = len(next)
    if 0 == plen or 0 == plen or 0 == nlen:
        return -1

    while i < slen and j < plen:
        if -1 == j or src_str[i] == p_str[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == plen:
        return i - j
    else:
        return -1


def getNext(pattern):
    """
    给定一个模式串，返回其对应的next数组
    :param pattern: 模式串
    :return: next数组
    """

    # next = [-1,0,0,0,0,1,2]
    plen = len(pattern)
    next = [-1 for x in range(plen)]
    next[0] = -1
    k = -1
    j = 0
    while j < plen - 1:
        if -1 == k or pattern[j] == pattern[k]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]

    return next


def getNextVal(pattern):
    """
    优化后的next数组求解
    :param pattern: 模式串
    :return: next数组
    """

    plen = len(pattern)
    next = [-1 for x in range(plen)]
    next[0] = -1
    k = -1
    j = 0
    while j < plen - 1:
        if -1 == k or pattern[j] == pattern[k]:
            k += 1
            j += 1

            if pattern[j] != pattern[k]:
                next[j] = k
            else:
                next[j] = next[k]
        else:
            k = next[k]

    return next


if __name__ == '__main__':
    src = 'BBC ABCDAB ABCDABCDABDE'
    pattern = 'ABCDABD'
    # next = getNext(pattern)
    next = getNextVal(pattern)
    print next
    print kmpSearch(src, pattern, next)

    # test getNext
    print getNext('ABCDABD')
    print getNext('DABCDABDE')
    print getNextVal('ABCDABD')
    print getNextVal('abab')
