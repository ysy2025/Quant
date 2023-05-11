class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        if pHead1 is None and pHead2 is None:
            return ListNode(None)
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        # 都不是空
        res = ListNode(0)
        new = res
        # 遍历
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                temp = pHead1
                res.next = temp
                pHead1 = pHead1.next
            else:
                temp = pHead2
                res.next = temp
                pHead2 = pHead2.next

        # 剩下的也连接上
        if pHead1 is None:
            res.next = pHead2
        if pHead2 is None:
            res.next = pHead1

        return new.next

if __name__ == '__main__':
    p = ListNode(1)
    for i in range(2, 11, 2):
        p.next = ListNode(i)
        p = p.next

    q = ListNode(2)
    for i in range(3, 12, 2):
        q.next = ListNode(i)
        q = q.next

    while p is not None:
        print("p val is ", p.val)
        p = p.next