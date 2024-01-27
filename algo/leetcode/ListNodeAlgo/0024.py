"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

双指针法
"""
from leetcode.ListNodeKlass import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from leetcode.ListNodeKlass import ListNode

class Solution:
    def swapPairs(self, head):
        # 准备哨兵 和最后返回值
        sentinel = ListNode(None)
        sentinel.next = head
        temp = sentinel

        while temp.next and temp.next.next:
            a,b = temp.next, temp.next.next
            temp.next = b
            a.next = b.next
            b.next = a
            temp = temp.next.next
        return sentinel.next

if __name__ == '__main__':
    sol = Solution()

    La = ListNode(4)
    Lb = ListNode(2)
    Lc = ListNode(1)
    Ld = ListNode(0)

    Ld.next = Lc
    Lc.next = Lb
    Lb.next = La

    print("ld is ")
    Ld.toString()

    print("\n")

    res = sol.swapPairs(Ld)
    res.toString()
