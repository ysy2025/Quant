from functools import wraps
import time
from random import random
from time import sleep

"""
有一个通过网络获取数据的函数（可能会因为网络原因出现异常），写一个装饰器让这个函数在出现指定异常时可以重试指定的次数，并在每次重试之前
随机延迟一段时间，最长延迟时间可以通过参数进行控制
"""
def get_data(f):
    def wrapper(*args, **kwargs):
        print(*args)
        # print(**kwargs.keys(), **kwargs.values())
        return "{0}, {1}, {2}".format(time.ctime(), *args, **kwargs)

        for key, value in kwargs.items():
            print(key, value)

    return wrapper

class Network:
    @get_data
    def get_network_data(self, url, pdate=20230101):
        pass


def kkk(*args, **kwargs):
    print(*args)
    # print(**kwargs.keys(), **kwargs.values())
    # return "{0}, {1}, {2}".format(time.ctime(), *args, **kwargs)

    for key, value in kwargs.items():
        print(key, value)



if __name__ == '__main__':
    network = Network()
    a = network.get_network_data("www.baidu.com", pdate=20230101)
    print(a)


    kkk(100, pdate=20230101)