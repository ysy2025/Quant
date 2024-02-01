"""
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。

整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。

返回被除数 dividend 除以除数 divisor 得到的 商 。

递归
比如 divide(20, 3)：

先将3不断翻倍，知道超过20，翻1次为2倍得6，翻2次为4倍得12，翻3次为8倍的24
这时4倍12是我们需要的值
递归 4 + divide(20-12, 3)
递归出口为：被除数 < 除数时返回0， 被除数 == 除数时返回1

"""

class Solution:
    def recursion(self, dividend, divisor):
        # print("==>>>recurstion start diviend is {0} divisor is {1} ".format(dividend, divisor))
        if dividend < divisor:
            return 0
        if dividend == divisor:
            return 1

        end = dividend
        sor = divisor

        sam = 0
        index = 0

        while end - sor:
            if end > sor:
                end = end-sor
                # 位移
                sam = sam + (1 << index)
                # sor 翻倍
                sor = sor + sor
                index += 1

            else:
                return sam + self.recursion(end, divisor)
        # 对残余值处理
        return sam + self.recursion(end, divisor)
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1

        if divisor == 0:
            raise Exception("!")
        else:
            # 判断flag
            if (dividend<0 and divisor>0) or (dividend > 0 and divisor < 0):
                flag = 0
            if (dividend > 0 and divisor > 0) and (dividend < 0 and divisor < 0):
                flag = 1
        print(flag)
        # 倍数减法
        ans = self.recursion(abs(dividend), abs(divisor))
        if flag:
            if ans > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return ans
        else:
            return -ans

if __name__ == '__main__':
    a = 10
    b = 3
    sol = Solution()
    sol.divide(a, b)
    # print(sol.divide(a, b))
    print(sol.recursion(a, b))