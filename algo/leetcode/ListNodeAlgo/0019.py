"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


进阶：你能尝试使用一趟扫描实现吗？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from leetcode.ListNodeKlass import ListNode


class Solution:
    def getListNode(self, l):
        if len(l) == 0:
            raise Exception("length error")
        if len(l) == 1:
            return ListNode(l[0], None)
        else:
            return ListNode(l[0], self.getListNode(l[1:]))

    def removeNthFromEnd(self, head, n: int):
        # 2次法
        length = 0
        head2 = head

        # 遍历,得到值
        while head:
            length += 1
            head = head.next

        # 超标:
        if n > length:
            return 0

        # 二次遍历
        head3 = head
        head4 = head
        temp = length - n

        # 第一个节点,直接返回
        if temp == 0:
            return head.next
        else:
            while temp > 0:
                head4 = head3
                head3 = head3.next
                temp -= 1
            head3.next = head4

        return head

if __name__ == '__main__':
    sol = Solution()
    l1 = ListNode(1,None)
    l2 = ListNode(2,l1)
    l3 = ListNode(3,l2)
    l4 = ListNode(4,l3)

    res = sol.removeNthFromEnd(l4, 3)
    #
    # while res.next:
    #     print(res)
    #     res = res.next

