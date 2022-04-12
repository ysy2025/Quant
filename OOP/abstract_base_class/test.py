from abc import ABCMeta, abstractmethod

class ABS(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def bet(self, hand):
        return 1
    @abstractmethod
    def bet2(self):
        pass

class ABSS(ABS):
    pass
    # def bet(self, hand):
    #     return 2
    # def bet2(self):
    #     pass
if __name__ == '__main__':
    abss = ABSS()
    print(abss)