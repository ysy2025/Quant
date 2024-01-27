"""
我悟了
合并,其实一次性就可以搞定.
一次过,然后针对大小处理,设置前置的哨兵,即可.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from leetcode.ListNodeKlass import ListNode


class Solution:
    def listToLN(self, list1):
        # print("list is {0} and length is {1}".format(list1, len(list1)))
        if len(list1) == 0:
            return None

        if len(list1) == 1:
            return ListNode(list1[0])
        else:
            head = ListNode(list1[0])
            length = len(list1)
            nodeList = [head]
            for i in range(1, length):
                node = ListNode(list1[i])
                nodeList.append(node)
            # print("node 数量几个?{0}".format(len(nodeList)))
            head2 = head
            head.next = nodeList[0]
            head = head.next
            for node in nodeList[1:]:
                head.next = node
                head = head.next
        return head2

    def LNtoList(self, ln1):
        list1 = []
        while ln1:
            list1.append(ln1.val)
            ln1 = ln1.next

        return list1

    def mergeTwoLists(self, list1, list2):
        left = list1
        right = list2

        sentinel = ListNode(None)
        res = sentinel
        
        while left and right:
            print("now left is {0} and right is {1}".format(left.val, right.val))
            # 左边小
            if left.val < right.val:
                sentinel.next = left
                left = left.next
                sentinel = sentinel.next
            else:
                sentinel.next = right
                right = right.next
                sentinel = sentinel.next

        sentinel.next = left if left else right

        return res.next

if __name__ == '__main__':
    sol = Solution()

    L1 = ListNode(4)
    L2 = ListNode(2)
    L3 = ListNode(1)

    L3.next = L2
    L2.next = L1

    LL1 = ListNode(4)
    LL2 = ListNode(3)
    LL3 = ListNode(1)

    LL3.next = LL2
    LL2.next = LL1

    # L3.toString()
    # LL3.toString()

    # list1 = [1,2,3,4]
    # LN1 = sol.listToLN(list1)
    # LN1.toString()

    # list2 = sol.LNtoList(L3)
    # list3 = sol.LNtoList(LL3)
    # print(list2, list3)

    res = sol.mergeTwoLists(L3, LL3)
    res.toString()


