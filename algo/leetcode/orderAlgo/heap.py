"""
这个模块实现了堆队列算法，即优先队列算法。

堆是一棵完全二叉树，其中每个节点的值都小于等于其各个子节点的值。这个使用数组的实现，索引从 0 开始，且对所有的 k 都有 heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]。比较时不存在的元素被认为是无限大。堆最有趣的特性在于最小的元素总是在根结点：heap[0]。

https://docs.python.org/zh-cn/3/library/heapq.html
"""
def findKthLargest(nums, k):
    #堆栈 时间复杂度O(n)
    import heapq
    res = []
    for num in nums:
        print("num is {0}".format(num))
        heapq.heappush(res, -num)
        print("res is {0}".format(res))
    for i in range(k):
        temp = heapq.heappop(res)
        print("temp is {0}".format(temp))

    return -temp


if __name__ == '__main__':
    nums = [8,6,7,45,6,3,5,23]
    print(findKthLargest(nums, 2))