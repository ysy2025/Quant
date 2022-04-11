Python有一些特殊方法,允许我们的类和Python更好集成.
object 的默认方法
Out[10]:
'__class__',
'__delattr__',
'__dict__',
'__dir__',
'__doc__',
'__eq__',
'__format__',
'__ge__',
'__getattribute__',
'__gt__',
'__hash__',
'__init__',
'__init_subclass__',
'__le__',
'__lt__',
'__module__',
'__ne__',
'__new__',
'__reduce__',
'__reduce_ex__',
'__repr__',
'__setattr__',
'__sizeof__',
'__str__',
'__subclasshook__',
'__weakref__'

标准库参考中,称为基本特殊方法,是与Python的其他特性无缝集成的基础
__repr__() 方法和 __str__() 方法,提供了对象的字符串的描述
__hash__(),__bool__(),__bytes__()方法,提供了对象的数字,布尔,哈希转换
其他方法

__lt__()

__repr__() & __str__() 方法
    和内置函数 repr,str,print,format的功能一直
    str方法表示的对象对用户更加友好.通过__str__()方法实现
    repr()方法的表示通常更加技术化,对于打电话类型,这个方法会尝试给出和eval一样的结果
    print函数会调用str()来生成输出对象
    format函数也可以使用这些方法. {!r} 或者 {!s} 格式时,实际上分别调用了 __repr__() & __str__()

    非集合对象的 __repr__() & __str__()
        见test2.py

    集合对象的 __repr__() & __str__()
        见test3.py
        涉及集合的时候,需要格式化集合中的单个对象,以及这些对象的整体容器

__format__()
    string.format() 和内置的format() 都是调用 __format__() 方法,都是为了获取给定对象的一个符合要求的字符串表示.
    两种传参的方式
        someobject.__format__("") "{0}".format(someobject),默认以这种方式调用 __format__()
        someobject.__format__(specification) 当应用程序中出现 format(someobject, specification) 或者 "{0:specification}".format(specification) 时,默认以这种方式调用 __format__()

    注意:
        "{0!r}" & "{0!r}" .format() 不是调用 __format__(),而是调用 __repr__() __str__()
        当specification 是 "" 一种合理返回值 return str(self),为各种对象的字符串表示形式提供了明确一致性

    内嵌格式规范
    string.format() 处理{}中内嵌实例,替换关键字,生成新规范

__hash__()
    哈希,将复杂值->小整数;理论上,一个hash值可以表示出源头值的所有位

    python中两个hash方法,hashlib,zlib
    hash 函数主要用来创建 set frozenset dict 这些集合类的键.这些集合利用不可变对象的hash值,来高效率查找集合中的对象
    不可变性很重要.不可变性对象不会改变状态.
    不同平台的hash值计算方法不同
    hash和内部id有很强依赖关系.hash方法默认行为是要保证每一个对象都是可以hash的,而且hash值是唯一的,及时这些对象包含同样值

    决定hash的对象->不是每一个对象都需要一个哈希值,尤其是创建一个包含有状态的,可以改变对象的类时,不应该返回hash值
    eq方法和hash有紧密关系

    等价性有三个层次:
        hash值相等->两个对象可能相等,对象相等,hash值必然相等
        比较结果相等,==运算符判断.相等->可能是同一个
        IDD相等->两个对象时同一个->hash值相同,==结果相同,是is运算符

    基本hash法, fundamental law of hash 比较相等的对象的hash值一定相同
    使用set 和 dict 时,计算hash值相等是预期的开销
    集合中有一些内置算法,当hash冲突时,使用备用位置

    不可变对象:可以继承eq和hash进行相等性测试和hash值
              可以自定义eq和hash
    可变对象:自定义eq和hash

    有关不可变对象和继承的默认行为
        默认行为如何工作?

        is 测试时基于id的值
        hash值是根据id计算出来的

    重载不可变对象
        如何防止属性值被改变?第三章介绍

    eq方法,比较了两个初始值
    hash函数,通过对两个基本数字的所有位,取异或,计算出一种新的位模式.^运算符是另外一种快速的方式,但是不太好
    对于复杂对象,可以考虑ziplib

    重载可变对象
        加上__hash__=None,即可,确保生成的对象不可以被hash,无法通过hash函数提供hash值
        对于set,dict这种,需要不可变对象的,不能用可变对象作为成员,因为需要hashable的数据类型.


2.4 __bool__()方法
    真假定义
    用下面的语句测试一个对象是否非空
    if some_object:
        process(some_object)

    默认的 bool 函数的逻辑->返回True
    对于大多数对象,都不应该和False等价;对于集合,空集合=False,非空集合=True

    将布尔值的计算委托给了其他对象.

2.5 __bytes__()方法
    只有极少数情况,需要将对象转换为字节
    通常,字符串会通过IO类内置的编码方法讲字符串转换为字节.一般都够用了.除非自定义一种新的字符串的时候需要定义编码方法
    byte(integer),返回一个不可变的字节对象