"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4


"""

class Solution:
    def partition(self, nums, left, right):
        mid = nums[left]

        # 从右往左,从左往右分别遍历
        while left < right:
            # 从右往左
            while left < right and nums[right] > mid:
                right -= 1
            # 短暂循环结束,right是小于mid的
            nums[left] = nums[right]
            # 从左往右
            while left < right and nums[left] <= mid:
                left += 1
            # 短暂循环结束,left是大于mid的
            nums[right] = nums[left]

        # 所有循环结束,交叉了
        nums[left] = mid
        return left

    def quickSort(self, nums, left, right):
        if len(nums) <= 1:
            return nums
        if left >= right:
            return

        index = self.partition(nums, left, right)
        print("index is {0}".format(index))
        self.quickSort(nums, left, index-1)
        self.quickSort(nums, index+1, right)
        return nums

    def findKthLargest(self, nums, k):
        left = 0
        right = len(nums) -1

        index = self.partition(nums, left, right)
        print("now nums is {0} and index is {1}".format(nums, index))

        # topK,看看index位置
        lenSmaller = index + 1
        lenLarger = len(nums) - lenSmaller
        print(lenSmaller, lenLarger, len(nums))

        print("now lef is {0} and right is {1} and index is {2} and k is {3}".format(nums[:lenSmaller], nums[lenSmaller:], index, k))

        # 刚好比larger长度多一个,就是他了
        if lenLarger == k:
            return nums[index]
        # 大的多了,也递归
        if lenLarger > k:
            return self.findKthLargest(nums[lenSmaller:], k)
            # 大的多了,也递归
        if lenLarger < k:
            # 大的不够,那么就递归调用
            return self.findKthLargest(nums[:lenSmaller], k - lenLarger)


if __name__ == '__main__':
    # a = [3, 4, 3, 1, 2, 4, 5, 5, 6]
    # a = [3,2,1,5,6,4,3,3]
    a = [4,6,5]
    k = 2
    sol = Solution()

    print(sol.partition(a, 0, 2))
    print(a)
    print(sol.quickSort(a, 0, len(a)-1))
    # print(sol.findKthLargest(a, k))
    # print(sol.partition(a, 0, len(a)-1))