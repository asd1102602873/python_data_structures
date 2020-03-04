def test5():
    li = []    
    for i in range(10000):        
        li.extend([i]) 
def test6():    
    li = []    
    for i in range(10000):        
        li.insert(0,i) 
        # 采用timeit测算一小段代码的运行速度 
        # # 追加操作

from timeit import Timer

#合并
timer5 = Timer('test5()','from __main__ import test5','毫秒')    
print('extend: ',timer5.timeit(1000)) 
#插入
timer6 = Timer('test6()','from __main__ import test6','毫秒')
print('insert :',timer6.timeit(1000))
# extend:  1.0101343999999999
# insert : 18.3201127