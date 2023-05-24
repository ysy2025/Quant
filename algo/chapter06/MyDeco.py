"""
装饰器,本质上就是一个函数;接收其他函数作为参数,将其以一个新的修改后的函数进行替换
最简单的装饰器就是本体函数,仅仅返回原函数
"""

_functions = {}
def register(f):
    _functions[f.__name__] = f
    return f

@register
def foo():
    print("zhangsan lisi wangermazi")


from functools import wraps
# def check_admin(f):
#     def wrapper(*args, **kwargs):
#         print(args)
#         print(kwargs)
#         if kwargs.get("username") != "admin":
#             raise Exception("!!")
#         return f(*args, **kwargs)
#     return wrapper()
#
#
# class Store:
#     def __init__(self):
#         self.storage = {}
#
#     @check_admin
#     def get_food(self, username="admin", food="apple"):
#         return self.storage.get(food)
#
#     @check_admin
#     def put_food(self, username="admin", food="haha"):
#         self.storage[username] = food

import time

def print_log(f):
    def wrapper(*args, **kwargs):
        return "{0}, {1}, {2}".format(time.ctime(), *args, **kwargs)
    return wrapper

class MathWork:
    @print_log
    def add(self, a, b):
        result = a + b
        return result


if __name__ == '__main__':
    mathwork = MathWork()
    a = mathwork.add(1, 2)
    print(a)