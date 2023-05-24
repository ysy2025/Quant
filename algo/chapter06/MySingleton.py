class Singleton(object):
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def get_instance(cls, *args, **kwargs):
        # hasattr() 函数用于判断对象是否包含对应的属性 , 这里是看看这个类有没有 _instance 属性  
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = Singleton(*args, **kwargs)

        return Singleton._instance

if __name__ == '__main__':

    s1 = Singleton()  # 使用这种方式创建实例的时候 , 并不能保证单例
    print(hasattr(Singleton, '_instance'))
    s2 = Singleton.get_instance()  # 只有使用这种方式创建的时候才可以实现单例
    print(hasattr(Singleton, '_instance'))
    s3 = Singleton()
    s4 = Singleton.get_instance()

    print(id(s1), id(s2), id(s3), id(s4))
