def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

@a_new_decorator
def hello():
    print("zhangsan lisi wangermazi")

if __name__ == '__main__':
    # a_function_requiring_decoration()
    print("-"*64)

    """
    这里我们封装一个函数,并且用这样或者那样的方式来修改它的行为.
    """
    # a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    # a_function_requiring_decoration()

    hello()
    print(hello.__name__)

    """
    总结起来,装饰器,相当于,把定义的函数,作为参数,传递到装饰函数中,运行
    继续参考:https://www.runoob.com/w3cnote/python-func-decorators.html
    """