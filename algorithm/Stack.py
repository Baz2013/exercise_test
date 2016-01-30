# -*- coding:utf-8 -*-

import string


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):

        return len(self.items) == 0 and True or False

    def pop(self):

        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def push(self, item):

        self.items.append(item)

    def peek(self):

        if not self.is_empty():
            return self.items[len(self.items) - 1]
        else:
            return None

if __name__ == '__main__':
    s = Stack()

    str1 = 'abc'
    mid = len(str1)/2
    for i in range(mid):
        s.push(str1[i])

    j = (len(str1) % 2 == 0 and mid) or mid + 1

    for i in range(j, len(str1)):
        #print '%s,%s'%(str1[i], s.peek())
        if str1[i] != s.peek():
            break
        else:
           s.pop()

    if s.is_empty():
        print "YES"
    else:
        print "NO"

