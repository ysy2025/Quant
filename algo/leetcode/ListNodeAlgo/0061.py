"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
"""
from leetcode.ListNodeKlass import ListNode

"""
1,拿到长度
2,拆分
3,然后合并
"""
class Solution:
    def rotateRight(self, head,k):
        # 拿到长度
        length = 0
        headCopy = head
        while headCopy:
            length += 1
            headCopy = headCopy.next
        if length == 0:
            return ListNode(0)
        if length == 1:
            return head
        k = k%length
        if k == 0:
            return head

        # prepare
        left = head
        right = head
        sentinel1 = ListNode(None)
        sentinel2 = ListNode(None)
        sentinel1.next = left

        # 一次,前后指针;right先跑
        while k:
            right = right.next
            k -= 1

        # 同时前进
        while right.next:
            right = right.next
            left = left.next

        # 拼接res,首先是获取后半部分
        res = left.next
        sentinel2.next = res

        # right到了最后一个,此时left还留了k个;left截断;sentinel链接right
        left.next = None

        # res指针移动到尾巴
        while res.next:
            res = res.next

        res.next = sentinel1.next

        return sentinel2.next




if __name__ == '__main__':
    sol = Solution()
    L0 = ListNode(5)
    La = ListNode(4)
    Lb = ListNode(2)
    Lc = ListNode(1)
    Ld = ListNode(0)

    Ld.next = Lc
    Lc.next = Lb
    Lb.next = La
    La.next = L0


    print("!"*32)

    res = sol.rotateRight(La, 0)
    res.toString()
