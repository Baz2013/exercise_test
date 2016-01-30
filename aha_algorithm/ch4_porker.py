#-*- encoding:utf-8 -*-

a = [0 for x in range(0, 10)]
book = [0 for x in range(0, 10)]
n = 0


def dfs(step):

    if step == n + 1:
        for i in range(1, n + 1):
            print a[i],
        print ""

        return

    for i in range(1, n + 1):
        if book[i] == 0:
            a[step] = i
            book[i] = 1
            dfs(step + 1)
            book[i] = 0

    return

if __name__ == '__main__':
    n = 3
    dfs(1)
