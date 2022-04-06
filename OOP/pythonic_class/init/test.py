class A(object):
    pass

class Rectangle:
    def area(self):
        # 延迟赋值,合法的,但是会带来隐藏的不确定性
        return self.length * self.width

class Book:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        
if __name__ == '__main__':
    # a = A()
    # print(a.__class__.__bases__)

    r = Rectangle()
    r.length = 10
    r.width = 10
    print(r.area())