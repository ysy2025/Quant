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