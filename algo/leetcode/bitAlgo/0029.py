"""
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。

整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。

返回被除数 dividend 除以除数 divisor 得到的 商 。
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if divisor == 0:
            raise Exception("!")
        elif dividend == 0:
            return 0
        if dividend<0 and divisor>0:
            index = 0
            while dividend + divisor <= 0:
                dividend += divisor
                index += 1

            return 0 - index

        if dividend > 0 and divisor < 0:
            index = 0
            while dividend + divisor >= 0:
                dividend += divisor
                index += 1

            return 0 - index

        if dividend > 0 and divisor > 0:
            index = 0
            while dividend - divisor >= 0:
                dividend -= divisor
                index += 1

            return index
        if dividend < 0 and divisor < 0:
            index = 0
            while dividend - divisor <= 0:
                dividend -= divisor
                index += 1

            return index
if __name__ == '__main__':
    a = 7
    b = -3
    sol = Solution()

    print(sol.divide(a, b))