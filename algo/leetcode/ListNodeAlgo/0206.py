from leetcode.ListNodeKlass import ListNode

"""
第一步 拿到长度
第二步 长度遍历,每两个交换 n*(n-1)/2 次
"""
class Solution:
    def reverseList(self, head):
        lenHead = head

        # get length
        length = 0
        while lenHead.next:
            length += 1
            lenHead = lenHead.next
        length += 1

        print("it is length {0}".format(length))

        sentinel = ListNode(None)
        sentinel.next = head

        res = ListNode(None)
        res.next = sentinel

        while length-1:
            # 初始化
            tail = head.next
            print("ow head is {0}, tail is {1}".format(head.val,tail.val))
            # tailNext = tail.next

            # 交换
            head.next = tail.next
            sentinel.next = tail
            tail.next = head
            sentinel.next.toString()

            print("交换完毕")
            # 交换完毕
            length -= 1
            # head = head.next
            sentinel = sentinel.next
            print("exchange hou head is {0}, tail is {1}, sentinel is {2}".format(head.val, tail.val, sentinel.val))
            # sentinel.toString()
        # res.next.toString()
        return res.next.next



class Solution2:
    def node2List(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res

    def list2Node(self, lst):
        sentinel = ListNode(None)

        res = ListNode(None)
        res.next = sentinel

        for i in range(len(lst)):
            head = ListNode(lst[i])
            sentinel.next = head
            sentinel = sentinel.next
        return res.next.next


    def reverseList(self, head):
        headList = self.node2List(head)

        headList.reverse()

        return self.list2Node(headList)

class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next
            cur.next = pre # 修改 next 引用指向
            pre = cur      # pre 暂存 cur
            cur = tmp      # cur 访问下一节点
        return pre

if __name__ == '__main__':
    sol = Solution2()

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

    print("ld is ")
    Ld.toString()

    print("\n")

    # res = sol.node2List(Ld)
    # print(res)
    #
    # res.reverse()
    # print("reversed res is {0}".format(res))
    # res2=sol.list2Node(res)
    # res2.toString()

    res = sol.reverseList(Ld)
    res.toString()

    sol3 = Solution3()
    res2 = sol.reverseList(Ld)
    res2.toString()