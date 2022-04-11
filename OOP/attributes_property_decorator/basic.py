import os, sys
import types

class A:
    pass

class Hand:
    def __init__(self, card):
        self.card = card

    def __str__(self):
        return ",".join(map(str, self.card))

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(
            __class__=self.__class__,
            _cards_str = ",".join(map(str, self.card)),
            **self.__dict__)

class HandLazy(Hand):
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self._cards = list(cards)

    @property
    def total(self):
        delta_soft = max(c.soft - c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)

        if hard_total + delta_soft <= 21:
            return hard_total + delta_soft

        return hard_total

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, aCard):
        self._cards.append(aCard)

    @card.deleter
    def card(self):
        self._cards.pop(-1)


class HandEager(Hand):
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.total = 0
        self._delta_soft = 0
        self._hard_total = 0
        self._cards = list()

        for c in cards:
            self.card = c

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, aCard):
        self._cards.append(aCard)

    @card.deleter
    def card(self):
        removed = self._cards.pop(-1)
        self._hard_total -= removed.hard
        self._delta_soft = max(c.soft - c.hard for c in self._cards)
        self._set_total()

    def _set_total(self):
        if self._hard_total+self._delta_soft <= 21:
            self.total = self._hard_total+self._delta_soft
        self.total = self._hard_total



if __name__ == '__main__':
    a = A()
    a.attribute = "zhangsan"
    print(a.attribute)

    b = A()

    c = types.SimpleNamespace()
    c.attribute = "zhangsan"
    print(c.attribute)