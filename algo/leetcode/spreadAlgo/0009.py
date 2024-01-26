"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。

转string,这个就很简单了

那么纯数字能搞定吗?不能...
"""
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xString = str(x)
        flag = True
        if len(xString) == 1:
            return flag
        elif len(xString) == 2:
            flag = xString[0] == xString[1]
            return flag
        else:
            left = 0
            right = len(xString) - 1
            while left <= right:
                if xString[left] != xString[right]:
                    flag = False
                    break
                left += 1
                right -= 1
        return flag

    def numIsPalindrome(self, x):
        flag = True
        if x < 0:
            flag = False
            return flag
        elif x < 10:
            return flag
        else:
            left = 0
            right = math.floor(math.log10(x))
            while left <= right:
                print("now left is {0}, right is {1}".format(left, right))
                leftInt = int(x//math.pow(10, right))
                rightInt = int(x%math.pow(10, left+1))
                print("left int is {0}, right int is {1}".format(leftInt, rightInt))

                if leftInt != rightInt:
                    flag = False
                    return flag
                # 外围是回文,处理掉
                x = (x - rightInt)/10
            return flag


if __name__ == '__main__':
    solution = Solution()
    x = 1011
    # print(solution.isPalindrome(x))
    # print(solution.numIsPalindrome(x))