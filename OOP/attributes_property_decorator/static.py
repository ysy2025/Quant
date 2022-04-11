import os, sys

class BlackJackCard:
    """
    abstract superclass
    """

    __slots__ = ("rank","suit","hard","soft")

    def __init__(self, rank, suit, hard, soft):
        super().__setattr__("rank", rank)
        super().__setattr__("suit", suit)
        super().__setattr__("hard", hard)
        super().__setattr__("soft", soft)

    def __str__(self):
        return "{0.rank}{0.suit}".format(self)

    def __setattr__(self, key, value):
        raise AttributeError("'{0}' has no attribute '{1}'".format(self.__class__, key))

class Rate(dict):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._solve()

    def __getattr__(self, name):
        return self.get(name, None)

    def __setattr__(self, key, value):
        self[key] = value
        self._solve()

    def __dir__(self):
        return list(self.keys())

    def _solve(self):
        if self.rate is not None and self.time is not None:
            self['distance'] = self.rate * self.time
            """
            下面的写法会__setattr__ & _solve 无限递归调用
            """
            # self.distance = self.rate * self.time
        if self.rate is not None and self.distance is not None:
            self['time'] = self.distance / self.rate
        if self.distance is not None and self.time is not None:
            self['rate'] = self.distance / self.time



if __name__ == '__main__':
    # A = BlackJackCard(1,2,3,4)
    # print(A.soft)
    # print(A.suit)
    #
    # A.__setattr__("suit", 10)

    B = Rate(rate = 10, time = 10, distance = None)
    print(B.items())
    print(B.keys())
    print(B['distance'])