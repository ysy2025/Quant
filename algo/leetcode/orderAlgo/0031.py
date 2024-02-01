"""
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，
如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。
如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

"""

class Solution:
    # 判断是不是逆时针有序的
    def isOrder(self, listA):
        listB = sorted(listA)
        standard = listB.reverse()
        if listA == standard:
            return 1
        return 0
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pass

if __name__ == '__main__':
    nums = [3,2,1]
    sol = Solution()
    print(sol.isOrder(nums))