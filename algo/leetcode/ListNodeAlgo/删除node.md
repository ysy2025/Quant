先验知识：如何删除链表的一个节点
删除链表的一个节点，我们需要获取要删除节点的前一个节点，改变其next指针的指向，跳过要删除的节点，指向要删除节点的下一个节点。

如果要删除节点是头节点，由于头节点没有前一个节点。为了方法的统一，可以在头节点之前加入一个伪头节点（又称“哨兵节点”）。如果最终要返回链表，返回伪头节点的下一个节点即为链表的头节点。

哈希表
由于链表结构不像数组可以知道每个节点的索引，因此我们先遍历一遍链表，用哈希表记录每个节点的索引；然后通过要删除节点的索引，获取要删除链表的前一个节点，将其的next指针指向要删除链表的后一个节点。

```python
class Solution:
    def removeNthFromEnd(self, head, n: int):
        pre = ListNode(0, head)   # 伪头节点
        node = pre    # 当前节点，初始化为伪头节点
        idx = 0    # 节点编号，初始为0
        node_map = {}   # 哈希表存储节点编号和节点
        while node:    # 遍历链表，idx最终为节点总个数
            node_map[idx] = node
            node = node.next
            idx += 1
        node_map[idx - n - 1].next = node_map[idx - n].next  # 根据节点编号获取删除节点的前一个节点和要删除的节点
        return pre.next    # 返回头节点 

```
作者：画图小匠
链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/2411535/javapython3ckuai-man-zhi-zhen-jian-ge-we-gjmb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


双指针
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/2188511/bian-li-liang-bian-shi-jian-fu-za-du-wei-so2j/