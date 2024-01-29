"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
"""

class Solution:
    def threeSum(self, nums):
        length = len(nums)
        if (not nums or length < 3):
            return []

        # 排序
        nums.sort()
        print("nums 排序 is{0}".format(nums))
        # res
        res = []

        # 遍历
        for i in range(length):
            print("nums[i] is {0}".format(nums[i]))
            # 排序后,当前>0,后续也大于0,不可能sum=0了
            if nums[i] > 0:
                return res
            # 重复元素,跳过
            if ( i > 0 and nums[i-1] == nums[i]):
                continue

            # 从左到右,分别指针移动
            left = i + 1
            right = length - 1
            while(left < right):
                print("left is {0} and right is {1}".format(left, right))
                # 符合条件
                if (nums[i] + nums[left] + nums[right] == 0):
                    res.append([nums[i], nums[left], nums[right]])
                    # 判断有没有重复解
                    while(left < right and nums[left] == nums[left+1]):
                        left = left + 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right = right - 1
                    left = left + 1
                    right = right - 1
                # 偏大
                elif (nums[i] + nums[left] + nums[right] > 0):
                    right = right - 1
                # 偏小
                else:
                    left = left + 1

        return res



if __name__ == '__main__':
    sol = Solution()
    #
    # nums = [0, 0, 1, -1, -10, 11, 0]
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0,0,0,0]
    print(sol.threeSum(nums))
    # res = sol.threeSum(nums)