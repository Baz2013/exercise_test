# -*- coding:utf-8 -*-


def violent_match(src_str,pattern_str):
    """
    :param src_str: 匹配串
    :param pattern_str: 模式串
    :return: 返回匹配到的位置，-1表示失败
    """
    slen = len(src_str)
    plen = len(pattern_str)

    if 0 == slen or 0 == plen:
        return -1

    i = 0
    j = 0
    while i < slen and j < plen:
        if src_str[i] == pattern_str[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j == plen:
        return i - j
    else:
        return -1

if __name__ == '__main__':
    s_str = 'BBC ABCDAB ABCDABCDABDE'
    p_str = 'ABCDABD'
    print violent_match(s_str, p_str)


