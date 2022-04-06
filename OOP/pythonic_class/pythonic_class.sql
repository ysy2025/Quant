重写特殊方法来实现对内部机制的调用
可以重写一些类的默认方法

对于len(x)这样的通用公共接口,任何类都可以重写,实现多态

如何让创建的类,更加pythonic?任何一个类,都应当与python语言其余的任何原生部分更好的结合,这样一来,不仅可以重用很多其他语言先用的功能和标准库
编写的包和模块也更加容易维护和扩展

创建的类都要可以作为python扩展的形式来实现,更加接近python的原生类

可扩展性:
    特性访问:attribute access,对象的特性访问,object.attribute,类似java的field,域,属性,有getter和setter
    可调用对象:callables,使用对象作为参数,例如len()函数
    集合:collections,这类方法提供了很多集合操作,例如 sequence[index], mapping[key]
    数字:numbers 提供了大量的数学和比较运算
    上下文:context with语句实现上下文管理
    迭代器:iterator,generator

