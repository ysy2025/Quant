"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

"""
class Solution:
    def search(self, nums, target):
        # 异常情况,直接返回
        if target < nums[0] or target > nums[-1]:
            return -1

        # 正常情况
        length = len(nums)
        if length == 1:
            return 0 if nums[0] == target else -1

        left = 0
        right = length-1
        mid = (left+right)//2

        # 避免最后剩两个数
        while left < right-1:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
                mid = (left+right)//2
            else:
                left = mid
                mid = (left+right)//2

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        else:
            return -1

if __name__ == '__main__':
    # nums = [-1, 0, 3, 5, 9, 12]
    nums = [-1, 10]
    target = 1
    sol = Solution()
    res = sol.search(nums, target)
    print(res)
