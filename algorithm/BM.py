# -*- coding:utf-8 -*-

"""
  BM 算法
  1、从右向左扫描；
  2、坏字符规则（Bad character shift rule,简称Bc）
  3、好后缀规则（Good suffix shift rule,简称Gs）
"""


def pre_bm_bc(pattern):
    """
    获取 坏字符规则
    :param pattern: 模式串
    :return: 坏字符规则表
    """

    bm_bc = [len(pattern) for x in range(256)]
    for i in range(len(pattern)):
        bm_bc[ord(pattern[i])] = len(pattern) - i - 1

    # print bm_bc
    return bm_bc

def pre_bm_gs(pattern):
    """
    获取 好后缀规则
    :param pattern: 模式串
    :return: 好后缀规则表
    """
    bm_gs = []

    for i in range(len(pattern)):
        bm_gs.append(len(pattern))

    return bm_gs


def bm_match(src, pattern):
    """
    BM算法匹配字符串
    :param src: 源字符串
    :param pattern: 模式串
    :return: 返回匹配到位置, -1 表示未匹配到
    """
    slen = len(src)
    plen = len(pattern)
    if slen == 0 or plen == 0 or plen > slen:
        return -1

    shift_list = pre_bm_bc(pattern)

    i = plen - 1
    j = plen - 1
    while i < slen and j >= 0 :
        if src[i] == pattern[j]:
            i -= 1
            j -= 1
        else:
            ascii_value = ord(src[i])
            i += shift_list[ascii_value]
            j = plen - 1

    if j == -1:
        return i + 1
    else:
        return -1



if __name__ == '__main__':

    p_str = 'bcababab'
    print pre_bm_gs(p_str)
    #p_str = 'EXAMPLE'
    #bc = pre_bm_bc(p_str)
    #src_str = 'HERE IS A SIMPLE EXAMPLE'
    #pos = bm_match(src_str,p_str)
    #print src_str[pos:pos + len(p_str)]

    #src_str1 = 'HERE IS A SIMPLE XAMPLE AAA TEST EXAMPLE'
    #pos1 = bm_match(src_str1,p_str)
    #print pos1
    #print src_str1[pos1:pos1 + len(p_str)]

    #src_str2 = 'HERE IS A SIMPLE XAMPLE AAA TEST MPLE'
    #pos2 = bm_match(src_str2,p_str)
    #print pos2

    #src_str3 = 'EXAMPLE:HERE IS A SIMPLE XAMPLE AAA TEST MPLE'
    #pos3 = bm_match(src_str3,p_str)
    #print pos3

