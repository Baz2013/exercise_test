#-*- coding:utf-8 -*-
import time

TIMES = 100000

dict_test = {'pp': 20, 'rr': 10, 'infoload': 30, 'indb': 20, 'filter': 20, 'rate': 10, 'split': 30, 'sdfstrans': 30, 'smsremind': 10, 'custsplit': 30}
list_test = [('pp', 20),( 'rr', 10),( 'infoload', 30),( 'indb', 20),( 'filter', 20),( 'rate', 10),( 'split', 30),( 'sdfstrans', 30),( 'smsremind', 10),('custsplit', 30)]
start =  time.time()
print 'start time:',start
for i in range(TIMES):
    pp = dict_test.get('pp')
    rr = dict_test.get('rr')
    infoload = dict_test.get('infoload')
    indb = dict_test.get('indb')
    filter = dict_test.get('filter')
    rate = dict_test.get('rate')

end = time.time()
print 'end time:', end
print end - start
print '------------------------test list'
def get_value(lst,key):
    for item in lst:
        if item[0] == key:
            return item[1]
        else:
            pass
    else:
        return 180
start =  time.time()
print 'start time:',start
for i in range(TIMES):
    pp = get_value(list_test,'pp')
    rr = get_value(list_test,'rr')
    infoload = get_value(list_test,'infoload')
    indb = get_value(list_test,'indb')
    filter = get_value(list_test,'filter')
    rate = get_value(list_test,'rate')

end = time.time()
print 'end time:', end
print end - start
