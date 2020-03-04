# #栈抽象的数据类型 采用list实现
# #确定列表的那一段是顶部 然后使用append和pop来实现操作

# #假设列表的尾部是栈的顶部


# class Stack:
#     def __init__(self):
#         self.item = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self,item):
#         return self.items.append(item)

#     def pop(self,item):
#         return self.items.pop(item)
    
#     def peek(self,item):
#         return self.items[len(self.items)-1]

#     def size(self):
#         return len(self.items)


# from pythonds.basic.stack import Stack

# s= Stack()

# print(s.isEmpty())
# s.push(4)
# s.push('lalla')


# print(s.peek())


# s.push(True)


# print(s.size())


# print(s.isEmpty())


# s.push(10.9)

# print(s.pop())
# print(s.pop())
# print(s.size())



# ()匹配

from pythonds.basic.stack import Stack

# SymbolString 假设 “( () )”
def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                s.pop()

        index = index + 1

    if flag and s.isEmpty():
        return True
    else:
        return False


print(parChecker('(())'))   # 栈：  
print(parChecker('((())')) # 栈：（





#  {[()]}   ( [ )]
# 每一个开始的符号被压入栈，等待匹配结果
# 当出现结束符号的时候，必须检查栈顶部的开始符号是什么类型，如果两个符号不匹配，则字符串不匹配
# 整个字符串处理完并且栈为空，则字符串匹配


from pythonds.basic.stack import Stack

def parchecker(SymbolString):
    s = Stack()
    index = 0


    while index < len(SymbolString) and flag:
        symbol = SymbolString(index)

        if symbol in "({[":
            s.push(symbol)
        else:
            if s.push(symbol):
                flag = False
            else:
                s.pop()
        index = index + 1

        
    if flag and s.isEmpty():
        return True
    else:
        return False

print(parChecker('{[()]}'))
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
