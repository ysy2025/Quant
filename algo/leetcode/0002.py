"""
https://leetcode.cn/problems/add-two-numbers/

"""
from ListNode import ListNode
import math

class Solution:
    def getTrueNumber(self, l3):
        trueNumber = 0
        index = 1
        while l3.next != None:
            trueNumber += l3.val * index
            index *= 10
            """
            这里没有用math.pow,因为指数超标后,会导致溢出;故此采用常规的手段
            """
            l3 = l3.next
        # print("now index is {0} and value is {1} and trueNumber is {2}".format(index, l3.val, trueNumber))
        # print("add is {0}".format(l3.val * index))
        trueNumber += l3.val * index
        # print("final situation is : index is {0} and value is {1} and trueNumber is {2}".format(index, l3.val, trueNumber))
        return trueNumber

    def num2ListNode(self, number):
        strings = list(str(number))
        if len(strings) == 0:
            raise Exception("sorry but input wrong!")
        elif len(strings) == 1:
            return ListNode(int(strings[0]))
        else:
            last = ListNode(int(strings[0]))
            strs_remain = strings[1:]

            for string in strs_remain:
                first = ListNode(int(string), last)
                last = first

        return last

    def addTwoNumbers(self, l1, l2):

        l1Value = self.getTrueNumber(l1)
        l2Value = self.getTrueNumber(l2)

        res = l1Value + l2Value

        return self.num2ListNode(res)

if __name__ == '__main__':
    solution = Solution()
    #
    # l1 = ListNode(3, None)
    # l2 = ListNode(4,l1)
    # l3 = ListNode(5,l2)
    #
    #
    # l4 = ListNode(7, None)
    # l5 = ListNode(8,l4)
    # l6 = ListNode(9,l5)
    #
    # la = solution.getTrueNumber(l3)
    # lb = solution.getTrueNumber(l6)
    # res = la + lb
    # print(la, lb)
    # print(res)
    #
    temp = 1134

    last = solution.num2ListNode(temp)

    print(last.val)








