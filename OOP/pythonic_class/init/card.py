import random
from functools import partial


class Card:
    """
    在Python中,通过单下划线"“来实现模块级别的私有化,变量除外.
    一般约定以单下划线""开头的函数为模块私有的,也就是说"from moduleName import * "将不会引入以单下划线"_"开头的函数.
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()

class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1, 11
    
class FAceCard(Card):
    def _points(self):
        return 10, 10

class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class A(list):
    def __init__(self, n):
        super().__init__(i for i in range(n))
        random.shuffle(self)


if __name__ == '__main__':
    # Club, Diamond, Heart, Spade = Suit('Club', '♣'), Suit('Diamaond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')
    # card1 = AceCard('a', Spade)
    # print(card1.soft)
    # print(card1.suit)

    a = A(10)
    print(a)