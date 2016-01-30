
def consumer():
    n = 0
    print 'consumer init'
    while True:
        n = yield n
        if not n:
            return
        n -= 1
        print 'consum 1 ,reserver %d'%n


def produce(c):
    n = 0
    next(c)
    while n < 6:
        n += 2
        print 'produce 2, sum %d'%n
        n = c.send(n)
        print 'aaaaa %d'%n

    c.close()

c = consumer()
produce(c)