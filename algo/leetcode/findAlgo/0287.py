"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

"""

from collections import Counter

class Solution:
    def findDuplicate(self, nums):
        counter = Counter(nums)

        for k in counter.elements():
            if counter[k] > 1:
                return k


class Solution2:
    def findDuplicate(self, nums):
        exists = []
        for num in nums:
            if num in exists:
                return num
            exists.append(num)

if __name__ == '__main__':
    # nums = [1,3,4,2,2]
    nums = [3,1,3,4,2]
    sol = Solution()
    print(sol.findDuplicate(nums))