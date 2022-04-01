import timeit

"""
timeit + 自定义函数的正确用法
from timeit import Timer

def test1():
    n=0
    for i in range(101):
        n+=i
    return n

if __name__=='__main__':
    t1=Timer("test1()","from __main__ import test1")
    print(t1.timeit(10000))
"""


def printIt():
    for i in range(10):
        print(i)

if __name__ == '__main__':
    a = timeit.timeit("""a = range(10)""")
    print(a)

    b = timeit.Timer('printIt()', "from __main__ import printIt")
    # 这个timeit()中的1,表示计算1次
    print(b.timeit(1))



