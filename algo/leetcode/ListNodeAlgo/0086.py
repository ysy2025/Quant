from leetcode.ListNodeKlass import ListNode

class Solution:
    def partition(self, head, x):
        sentinel = ListNode(None)
        sentinel.next = head

        left = head
        right = head
        leftNext = left.next
        print("left{0} right{1} leftNext{2}".format(left.val, right.val, leftNext.val))


        # 首先定位到k
        while right:
            print("now right is {0}".format(right.val))
            if right.val != x:
                right = right.next
            else:
                break

        # 定位后,双指针运行
        while right.next:
            rightNext = right.next
            print("right val is {0}, rightnext is {1}".format(right.val, rightNext.val))
            # 所有小于x的节点 移动
            if rightNext.val < x:
                # right 要跳过next节点
                # 要注意,区分有没有next.next
                if rightNext.next:
                    print("足够长啊========================================>")
                    right.next = rightNext.next
                    right = right.next
                    # left 要顺移
                    rightNext.next = None
                    left.next = rightNext
                    left = left.next
                    print("移动之后 ==> right val is {0}".format(right.val))
                    print("now is {0}".format(leftNext.val))
                else:
                    print("不够长!")
                    # right 清空
                    right.next = None

                    # left 要顺移
                    rightNext.next = None
                    left.next = rightNext
                    left = left.next
                    print("移动之后 ==> right val is {0}".format(right.val))
                    print("now is {0}".format(leftNext.val))
                    break
            # 不小于x,不d动
            else:
                right = right.next
                print("移动之后 ==> right val is {0}".format(right.val))

        # 到最后,粘贴left和leftNext
        left.next = leftNext
        print("最后的后 ==> right val is {0}".format(right.val))

        while leftNext.next:
            print("now is {0}".format(leftNext.val))
            leftNext = leftNext.next

        # while sentinel.next:
        #     print("now is {0}".format(sentinel.next.val))
        #     sentinel = sentinel.next
        return sentinel.next

class Solution2:
    def partition(self, head, x):
        small_dummy = ListNode(None)
        big_dummy = ListNode(None)
        small = small_dummy
        big = big_dummy

        while head:
            if head.val < x:
                small.next = head
                # print("snall is ")
                # small.toString()
                small = small.next
            else:
                big.next = head
                print("big is ")
                big.toString()
                big = big.next
            head = head.next
        print("==> bigdummy is ")
        big_dummy.next.toString()
        print("==> small dummy is ")
        small_dummy.next.toString()
        small.next = big_dummy.next
        big.next = None
        return small.next

class Solution3:
    def partition(self, head,x):
        sml_dummy, big_dummy = ListNode(None), ListNode(None)
        sml, big = sml_dummy, big_dummy
        while head:
            if head.val < x:
                sml.next = head
                sml = sml.next
            else:
                big.next = head
                big = big.next
                big_dummy.toString()
            head = head.next
        sml.next = big_dummy.next
        big.next = None
        return sml_dummy.next

if __name__ == '__main__':

    # Ld = ListNode(1)
    # Lc = ListNode(4)
    # Lb = ListNode(3)
    # La = ListNode(2)
    # Laa = ListNode(5)
    # Laaa = ListNode(2)
    #
    # Ld.next = Lc
    # Lc.next = Lb
    # Lb.next = La
    # La.next = Laa
    # Laa.next = Laaa


    Ld = ListNode(2)
    Lc = ListNode(1)
    Ld.next = Lc

    # sol = Solution2()
    # res = sol.partition(Ld, 2)
    # res.toString()

    sol = Solution3()
    res = sol.partition(Ld, 2)
    res.toString()