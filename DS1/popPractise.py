# from timeit import Timer
#
# x = range(2000000)
# pop_zero = Timer("x.pop(0)","from __main__ import x")
# print("pop_zero ",pop_zero.timeit(number=1000), "seconds")
# # x = range(2000000)
# # pop_end = Timer("x.pop()","from __main__ import x")
# # print("pop_end ",pop_end.timeit(number=1000), "seconds")
#
# ('pop_zero ', 1.9101738929748535, 'seconds')
# ('pop_end ', 0.00023603439331054688, 'seconds')

import timeit

def test5():
    list_1 = list(range(100))
    for i in range(100):
        list_1.pop()  #最后一个元素

def test6():
    list_2 = list(range(100))
    for i in range(100):
        list_2.pop(0)  #第一个元素

time6 = timeit.Timer("test5()", "from __main__ import test5")
time7 = timeit.Timer("test6()", "from __main__ import test6")
print("pop():%s"%time6.timeit(),'毫秒')#pop():8.954501
print("pop(0):%s"%time7.timeit(),'毫秒')#pop(0):14.834948

