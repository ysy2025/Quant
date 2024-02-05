"""
给你单链表的头结点 head ，请你找出并返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

标准的双指针

"""
from leetcode.ListNodeKlass import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast.next:
            print("1, fast value is {0}".format(fast.val))
            if fast.next.next:
                fast = fast.next
                print("2, fast next value is {0}".format(fast.val))
                fast = fast.next
                slow = slow.next
                print("after one cycle value is {0}".format(fast.val))
            else:
                break

        print("finally fast value is {0}".format(fast.val))
        return slow.next if fast.next else slow

if __name__ == '__main__':
    Ld = ListNode(1)
    Lc = ListNode(4)
    Lb = ListNode(3)
    La = ListNode(2)
    Laa = ListNode(5)
    Laaa = ListNode(2)

    Ld.next = Lc
    Lc.next = Lb
    Lb.next = La
    La.next = Laa
    Laa.next = Laaa

    sol = Solution()
    res = sol.middleNode(Ld)
    res.toString()