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
                print("此时q---- is")
                q.toString()
                print("此时pppp is")
                p.toString()
                print("\n")
                p = q
                q = q.next
                temp = temp - 1
            p.next = q.next
        print("-----------end head is")
        head.toString()
        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    head = ListNode(4)

    head.next = l3
    l3.next = l2
    l2.next = l1

    # head.toString()
    n = 1

    # res = removeNthFromEnd(head, n)
    # while res:
    #     print("end ===========> {0}".format(res.val))
    #     res = res.next

    res = head
    res.toString()
    print("\n")
    while res:
        print(res.val)
        res = res.next

    print("\n")

    print(res == None)

    res = head
    res.toString()


    # print(head.toString())
    #
    # res2 = removeNthFromEnd(head, 2)
    # while res2:
    #     print(res2.val)
    #     res2 = res2.next
    # print(res2.toString())
    #
    # len, p = 0, head
    # while p:
    #     len = len + 1
    #     p = p.next
    # if n > len:
    #     print("sorry but no enough node")
    # else:
    #     q = head
    #     p = head
    #     temp = len - n
    #     if temp == 0:
    #         print("只能噶开头了{0}".format(head.val))
    #     else:
    #         while temp > 0:
    #             p = q
    #             q = q.next
    #             temp = temp - 1
    #         p.next = q.next
    #     print(head.toString())
    #
    # print(head.toString())


    # res = removeNthFromEnd(head, 2)
    # while res:
    #     print(res.val)
    #     res = res.next
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