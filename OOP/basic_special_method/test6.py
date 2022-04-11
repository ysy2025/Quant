import collections

class Ordered_Attributes(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwds):
        return collections.OrderedDict()
    def __new__(cls, name, bases, namespace, **kwds):
        result = super().__new__(cls, name, bases, namespace)
        result._order = tuple(n for n in namespace if not n.startswith('__'))
        return result

class Order_Preserved(metaclass=Ordered_Attributes):
    pass

class Something(Order_Preserved):
    this = 'text'
    def z(self):
        return False

    b = 'order is preserved'
    a = 'more text'

if __name__ == '__main__':
    print(Something._order)
    print(dir(Something))
    """
    这里的namespace,实际上是dir,Something自带的属性和方法的处理
    """