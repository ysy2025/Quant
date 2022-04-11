class Card:
    insure = False

    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(
            ___class__=self.__class__, **self.__dict__)

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)

class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__("A", suit, 1, 11)

class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({11:"J",12:"Q",13:"K"}[rank], suit, 10, 10)

if __name__ == '__main__':
    c = AceCard(1, "♥")
    d = AceCard(1, "♥")
    print(id(c))
    print(id(d))

    print(c == d)
    print(c is d)
