from leetcode.ListNodeKlass import ListNode


def removeNthFromEnd(head, n: int):
    len, p = 0, head
    while p:
        len = len + 1
        p = p.next
    if n > len:
        return 0
    else:
        q = head
        p = head
        temp = len - n
        if temp == 0:
            return head.next
        else:
            while temp > 0:
                p = q
                q = q.next
                temp = temp - 1
            p.next = q.next
        # return
        return p

def printL(res):
    while res:
        print(res.val)
        res = res.next

if __name__ == '__main__':
    l1 = ListNode(1, None)
    l2 = ListNode(2, l1)
    l3 = ListNode(3, l2)
    head = ListNode(4, l3)

    res = removeNthFromEnd(head, 2)
    while res:
        print(res.val)
        res = res.next
    # n = 2
    # res = removeNthFromEnd(head, 2)
    # while res:
    #     print(res.val)
    #     res = res.next
    #
    # while head:
    #     # print(head.val)
    #     head = head.next
    #
    # p, q = head, head
    # printL(p)
    # printL(q)
    # len, p = 0, head
    # while p:
    #     print(p.val)
    #     p = p.next
    #
    # while head:
    #     print(head.val)
    #     head = head.next
    #
    # len, p2 = 0, head
    # while p2:
    #     print(p2.val)
    #     p2 = p2.next

    # len, p = 0, head
    # while p:
    #     len = len + 1
    #     p = p.next
    # if n > len:
    #     print("!!!")
    # else:
    #     q = head
    #     p = head
    #     temp = len - n
    #     if temp == 0:
    #         res = head.next
    #         while res.next:
    #             print("开头!")
    #             print(res.val)
    #             print("\n")
    #             res = res.next
    #     else:
    #         while temp > 0:
    #             p = q
    #             q = q.next
    #             temp = temp - 1
    #         p.next = q.next
    #     res = head
    #     while res.next:
    #         print("不是开头!")
    #         print(res.val)
    #         print("\n")
    #         res = res.next