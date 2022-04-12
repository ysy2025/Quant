属性访问的5种方法
    内部集成属性处理方式->最简单的
    @property,修饰符,特性扩展了属性的概念,包含了方法的处理
    底层的特殊方法来控制属性的访问:__getattr__(),__setattr__(),__delattr__()
    使用__getattribute__()方法在更细粒度层面上操作属性
    介绍一些修饰符,用于属性访问
    默认方法

3.1 属性基本操作
    4种操作,创建,赋值,获取值,删除属性
    添加,修改,删除属性;如果视图获取一个未赋值的属性,或者删除一个不存在的属性时,报错

    另一中更好的方法是从,types.SimpleNamespace类创建实例,此时不需要额外定义一个新类,就能实现同样功能

    特性和init方法
        理想情况下,在init方法中提供所有属性的默认值
        init方法中,没必要为所有属性赋值;一个特性的存在与否构成了对象状态的一部分
    可选择性,更好完善了类定义.
    可选择性,隐藏了一种非正式的子类关系

3.2 创建特性
    特性是一个函数,语法上看起来就是一个简单的属性,可以获取,设置,删除,看起来和属性没有区别
    但是,特性是一个函数,而且可以被调用,而不仅仅是存储对象的引用

    除了复杂程度,特性和属性的区别->我们不能轻易为已有的对象添加新特性,但是添加新属性不难
    两种方式创建特性:@property;property函数

    特性的两种基本设计模式:
        主动计算:更新特性值,其他相关特性就立即重算
        延迟计算:仅当访问特性时,才触发计算过程

    主动计算特性

    赋值更加显然的体现了代码意图

    setter和getter
    @property就是getter
    @xx.setter是setter
    @xx.deleter是删除器

3.3 使用特殊方法完成属性访问
    getattr,setattr,delattr,dir查看属性名称;getattribute

    关于属性,几种默认操作
    setattr,创建属性和赋值
    getattr,已有值,则获取值,没有值,则赋值
    dir,用于返回属性名称列表

    注意扩展,封装,创建
    扩展类,通过重写 __getattr__(),__setattr__(),__delattr__(),使得它几乎是不可变的;也可以使用 __slot__() 替换内部的 __dict__
    封装类,提供对象或者对象集合属性访问的代理实现->可能需要完全重写和属性相关的函数
    创建类并提供和特性功能一样的函数->用来对特性逻辑集中处理

    创建延迟计算->getattr
    创建主动计算->setattr

    使用__slot__创建不可变对象

    使用tuple子类创建不可变对象
        通过让card特性成为tuple子类的对象,重写 getattr函数来实现一个不可变对象, getattr->self[index]

3.4 __getattribute__()方法
    提供了对于属性更加底层的一些操作.默认的实现方式是从内部__dict__中查找已经有的属性,如果属性没有找到则调用getattr函数
    如果值是一个修饰符,对修饰符进行处理,否则返回当前值即可.

    重写此方法,可以有效组织属性访问
    可以仿照getattr的函数的工作方式来创建新属性.可以绕过getattribute的实现逻辑
    可以使得属性执行单独或者不同的任务->降低程序的可读性和可维护性
    可以改变修饰符的行为

    getattribute方法时,将阻止任何内部属性访问函数体

    为了获得getattribute方法中的属性值,必须显式调用object基类中的方法

3.5 创建修饰符
    修饰符,可以当成属性的访问中介
    修饰符类,可以用来获取,赋值,删除属性值,修饰符对象通常在类定义的时候被创建
    修饰符模式有两个部分:owner和attribute descriptor
        owner,使用一个或者多个修饰符作为属性;
        修饰符中,可以定义获取赋值和删除的函数;一个修饰符类的实例,将作为拥有者类的属性
    特性是,基于拥有这类的函数,修饰符不同于特性,与拥有者类直接没有耦合

    修饰符是在类级别定义的,它的引用,并非在init的初始化函数中被创建
    修饰符可以再初始化过程中被赋值
    修饰符通常作为类定义的一部分,处于任何函数之外
    定义owner的时候,每个修饰符对象都是修饰符类的实例,绑定在类级别的属性上

    为了标识为修饰符,必须实现以下3个方法中的一个或者多个
        Descriptor.__get__(self, instance, owner)->object
            此方法中,instance参数来自被访问对象的self变量,owner变量是拥有者类的对象
            if被调用,instance参数默认值为None,此方法负责返回修饰符的值
        Descriptor.__set__(self, instance, value)
            此方法中,instance参数,是被访问对象的self变量,而value参数为即将赋的新值
        Descriptor.__delete__(self, instance)
            此方法中,instance参数来自被访问对象的self变量,此方法实现删除功能

    非数据修饰符
        set和delete或者两者皆有
        不能定义get
        常常用于构建复杂表达式
        可能是可以调用的对象;
        不可变的非数据修饰符必须实现set函数;
        逻辑只是单纯刨除attributeerror异常

    数据修饰符
        至少要定义get方法
        通常可以通过定义get和set方法,创建可变对象
        不能定义自己内部的属性或者方法->通常是不可见的.
        对修饰符属性的访问,也转换为 get set delete 方法的调用

    修饰符使用案例
        类内部方法被实现为修饰符;它们是非数据修饰符,应用在对象和不同的参数值上
        property函数是通过为命名的属性,创建数据修饰符来实现的
        类方法或者静态方法被实现为修饰符,修饰符作用于类,而不是实例

    设计修饰符:
        修饰符对象包含或者获取数据
            __get__ & __set__ 方法创建数据修饰符,不用__get__方法的情况下创建非数据修饰符
        拥有者实例包含数据
            @property装饰器的作用.把计算逻辑从拥有者类搬到了修饰符类中
        拥有者类包含数据
            @staticmethod和@classmethod装饰器的实现

    3.5.1 使用非数据修饰符
