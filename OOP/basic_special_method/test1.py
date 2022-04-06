class Card:
    insure = False
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()

    def _points(self):
        return int(self.rank), int(self.rank)

class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)

    def __str__(self):
        return "rank is {0} and suit is {1}".format(self.rank, self.suit)

    def __repr__(self):
        return "rank is {0} and suit is {1} and it is awesome!".format(self.rank, self.suit)
if __name__ == '__main__':
    x = NumberCard('2', '♠')
    print(str(x))
    print(repr(x))
    print(x)
    """
    <__main__.NumberCard object at 0x000002234FBAED48>
    <__main__.NumberCard object at 0x000002234FBAED48>
    <__main__.NumberCard object at 0x000002234FBAED48>
    
    可以看到,__repr__() & __str__() 的默认实现没啥用,信息有限
    
    非集合对象,不包括任何其他集合对象的简单对象,这类对象的格式化通常不会很复杂
    非集合对象,包括对象的对象,这类对象的格式化更加复杂
    
    改写str后
    def __str__(self):
        return "rank is {0} and suit is {1}".format(self.rank, self.suit)
        
    rank is 2 and suit is ♠
    <__main__.NumberCard object at 0x000001B27B09EDC8>
    rank is 2 and suit is ♠
    
    可以看到,print默认引用str
    
    
    
    """