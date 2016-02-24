import Queue
import threading
import time
import random


def do_work(r_item):
    time.sleep(random.randint(1, 4))
    print '[%d]' % (r_item,)


def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()


q = Queue.Queue()
for i in range(4):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

for item in range(100):
    q.put(item)

q.join()  # block until all tasks are done
