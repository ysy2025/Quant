"""
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

输入：head = [1,1,1,2,3]
输出：[2,3]

1,复制一个head 找到重复数字
2,建立哨兵一个,用作返回
3,复制一个head,直接遍历,删除

a = ListNode(None)
a == None
Out[6]: False
"""
from leetcode.ListNodeKlass import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        # 找重复数据的head,顺便拿到length
        numHead = head
        length = 0

        # 删除节点的head
        delHead = ListNode(None)
        delHead.next = head

        # 哨兵
        sentinel = delHead

        # 找重复
        nums = {}
        dupNums = []

        while numHead:
            length += 1
            # print("numHead is {0}".format(numHead.val))
            if numHead.val in nums.keys():
                dupNums.append(numHead.val)
            else:
                nums[numHead.val] = nums.get(numHead.val, 0) + 1
            numHead = numHead.next

        print("now dupNums is {0} and nums is {1}, length is {2} \n".format(dupNums, nums, length))

        # 针对长度判断
        if length <= 1:
            return head
        else:
            print("开始删除之前,delHead is")
            delHead.toString()
            # 针对每个节点判断 ListNode(None) 是ok的
            # 从哨兵的next开始,每个next进行判断
            while delHead.next:
                # 准备next节点
                temp = delHead.next
                tempNext = temp.next

                # next 是重复的,删除 next;delhead 不要移动
                if temp.val in dupNums:
                    print("链表当前节点的是 {1}, 下一个节点是重复的, 下一个节点 值是 {0}".format(temp.val, delHead.val))
                    delHead.next = tempNext
                    print("删除1个, sentinel val is {0}".format(delHead.val))
                    delHead.toString()
                else:
                    print("链表当前节点不是重复的, 下一个节点值是 {0}".format(temp.val))
                    delHead = delHead.next
                    print("删除0个, sentinel val is {0}".format(delHead.val))
                    delHead.toString()

            print("=" * 64)
            # 结束循环,还在最后一个
            if delHead.val in dupNums:
                del delHead
            else:
                pass

        # sentinel.next.toString()
        return sentinel.next




if __name__ == '__main__':
    sol = Solution()
    L0 = ListNode(0)
    La = ListNode(0)
    Lb = ListNode(0)
    Lc = ListNode(1)
    Ld = ListNode(0)

    Ld.next = Lc
    Lc.next = Lb
    Lb.next = La
    La.next = L0

    Ld.toString()
    print("!"*32)

    res = sol.deleteDuplicates(Ld)
    res.toString()
