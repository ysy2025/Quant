class Ration10:

    @staticmethod
    def _gcd(big, small):
        if big == 0: # 可以除尽
            big, small = small, big
        else:
            while small != 0:
                big, small = small, big%small
        return big

    def __init__(self, num, den=1):
        """

        :param num:分子
        :param den: 分母
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError

        if den == 0:
            raise ZeroDivisionError

        sign = 1
        if num < 0: # 负数
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign

        g = Ration10._gcd(num, den) # 求最大公约数,然后分子分母一起除
        self._num = sign * (num//g)
        self._den = den

    # def plus(self, another):
    #     den = self.den * another.den
    #     num = (self.num *another.den + self.den * another.num)
    #
    #     return Ration10(num, den)
    #
    def print(self):
        print(str(self._num) + "/" + str(self._den))

def gcd(big, small):
    """

    :param big:
    :param small:
    :return:
    required:small != 0
    """
    if small == 0:
        return 0
    else:
        if big%small == 0:
            return small
        else:
            big, small = small, big%small
            print("big is {0}, small is {1}".format(big, small))
            return gcd(big, small)

if __name__ == '__main__':
    a = Ration10(-3, 5)
    a.print()
    # b = Ration10(4, 5)
    # c = a.plus(b)
    # c.print()

    # big = 77
    # small = 60
    # bs_gcd = gcd(big, small)
    # print(bs_gcd)