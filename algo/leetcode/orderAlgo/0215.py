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
        index = left + 1

        for i in range(left+1, right):
            if nums[i] < mid:
                print("i is {0} indx is {1}".format(i, index))
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
                print("==>now nums is {0}, index-1 is {1}".format(nums, index - 1))

        nums[left], nums[index-1] = nums[index-1], nums[left]
        print("now nums is {0}, index-1 is {1}".format(nums, index-1))
        return index-1

    def quickSort(self, nums, left, right):
        # 这种带索引的,能够解决TopK的问题;相比python的快速写法,覆盖面更广一点
        # left = 0
        # right = len(nums) - 1
        if left < right:
            # 有部分排序的功能,也有返回分区界限的功能
            index = self.partition(nums, left, right)
            self.quickSort(nums, left, index-1)
            self.quickSort(nums, index+1, right)
        return nums

    def findKthLargest(self, nums, k):

        pass

if __name__ == '__main__':
    # a = [3, 4, 3, 1, 2, 4, 5, 5, 6]
    a = [4,2,1,3]
    k = 4
    sol = Solution()
    # sol.findKthLargest(a, k)
    print(sol.quickSort(a, 0, 4))
    # print(sol.partition(a, 0, len(a)-1))