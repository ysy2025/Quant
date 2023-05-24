from collections import namedtuple
Card = namedtuple('Card', ('suite', 'face'))
card1 = Card('红桃', 13)
card2 = Card('草花', 5)
print(f'{card1.suite}{card1.face}')
print(f'{card2.suite}{card2.face}')

class MyCard(Card):
    def show(self):
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{self.suite}{faces[self.face]}'


if __name__ == '__main__':
    print(Card)  # <class '__main__.Card'>
    card3 = MyCard('方块', 12)
    print(card3.show())  # 方块Q
    print(dict(card1._asdict()))  # {'suite': '红桃', 'face': 13}
    print(card2._replace(suite='方块'))  # Card(suite='方块', face=5)