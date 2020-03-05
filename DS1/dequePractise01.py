

#i
from pythonds.basic.deque import Deque

def palChecker(aString):
    chardeque = Deque()
    for i in aString:
        chardeque.addRear(i)
    flag = True

    while chardeque.size() > 1 and flag:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
    
        if first != last:
            flag = False

    return flag


print(palChecker("山西运煤车煤运西山"))