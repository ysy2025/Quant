"""
猴子补丁
https://blog.csdn.net/lycwhu/article/details/125573781
https://blog.csdn.net/u013391094/article/details/127530177

"""
class Test:
    def func(self):
        print("hi")


def monkey(self):
    print("hi monkey")


Test.func = monkey

a = Test()
a.func()
