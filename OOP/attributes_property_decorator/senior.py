class BlackJackCard:
    """
    abstract superclass
    """
    def __init__(self, rank, suit, hard, soft):
        super().__setattr__("rank", rank)
        super().__setattr__("suit", suit)
        super().__setattr__("hard", hard)
        super().__setattr__("soft", soft)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError("cannot see {name}".format(name=key))
        raise AttributeError("'{__class__.__name__}' has no attribute '{name}'".format(___class__=self.__class__, name=key))

    def __getattribute__(self, item):
        print(item)
        if item.startswith('_'):
            raise AttributeError
        return object.__getattribute__(self, item)
if __name__ == '__main__':
    c = BlackJackCard("A", "!", 1, 11)
    print(c.rank)

    """
    以上代码重写了 __getattribute__()方法,访问私有名称或者python内部名称时,代码会raise异常->对象被封装更加彻底,无法改变
    """
    # c.rank = "B"
    # print(c.rank)
    print(c.__setattr__("suit", "zhangsan"))
    # print(c.__setattr__("suit", "zhangsan"))
    # print(c.suit)