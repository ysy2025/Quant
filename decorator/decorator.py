"""
this file is used to explain the decorators
"""

"""
everything is object

"""
def hi(name = "yahoo"):
    return "hi " + name


"""
我们可以在函数中定义函数
"""


def hi2(name="yahoo"):
    print("now you are inside the hi2() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi2() function")



"""
所谓装饰器,就是将函数,作为参数,传给另一个函数

此外装饰器让你在一个函数的前后去执行代码
"""
def hi3():
    return "zhangsan niubi!"

def deco(func):
    print("I am doing some boring work before executing hi3()")
    print(func())

if __name__ == '__main__':

    """
    可以将函数赋值给变量,这里不需要用小括号,
    """
    greet = hi
    print(greet())

    """
    可以使用小括号,得到返回值
    """
    gg = hi()
    print(gg)

    """
    如果我们删掉旧的hi函数,看看会发生什么?
    """
    del hi
    try:
        print(hi())
    except Exception as e:
        print(e)
    print(gg)
    print(greet())


    hi2()

    deco(hi3)