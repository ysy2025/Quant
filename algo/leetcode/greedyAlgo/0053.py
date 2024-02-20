"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
"""
import math


class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        print("length is {0} and nums is {1}".format(length, nums))
        # 特殊情况直接返回
        if length == 1:
            return nums[0]
        # 其他特殊情况
        # 全员非正
        if max(nums) <= 0:
            return max(nums)
        # 全员非负
        if min(nums) >= 0:
            return sum(nums)

        # 普通情况
        summ = sum(nums)
        # 针对不同summ有不同路线
        maxSum = -math.inf
        # minSum = math.inf
        minSum = 0
        # 上半区
        if summ>=0:
            print("上半区")
            for i in range(length):
                print("===> i is {0}, length is {1}, nums is {2}".format(i, length, nums))
                sumNums = sum(nums[:i+1])
                maxSum = max(maxSum, sumNums)
                minSum = min(minSum, sumNums)
                print("sum is {0}, max sum {1}, min sum {2}".format(sumNums, maxSum, minSum))

            # 结束循环
            # return maxSum if minSum >= 0 else maxSum - minSum
            return maxSum - minSum
        # 下半区
        else:
            maxDelta = 0
            for i in range(length):
                sumNums = sum(nums[:i+1])
                print("===> i is {0}, length is {1}, nums is {2}, nums[i] is {3}, sumNums is {4}".format(i, length, nums, nums[i], sumNums))
                if nums[i] <= 0:
                    # 非正数,更新min
                    minSum = min(minSum, sumNums)
                    print("负数的情况 ==> sum is {0}, max sum {1}, min sum {2}\n".format(sumNums, maxSum, minSum))
                else:
                    # 正数,更新maxsum和delta
                    maxSum = max(maxSum, sumNums)
                    minSum = 0 if i == 0 else minSum
                    maxDelta = max(maxDelta, maxSum - minSum)
                    print("++++的情况 ==> sum is {0}, max sum {1}, min sum {2}, maxDelta is {3}\n".format(sumNums, maxSum, minSum, maxDelta))


            # 结束循环
            return max(maxDelta, summ-minSum)

if __name__ == '__main__':
    # nums = [-15,-4,1,7,-1,2, -8]
    # nums = [1, -1, -2]
    nums = [1, -2 , 3]
    # nums = [1, 1, 1,-2,-3,-3,1,3,0]
    sol = Solution()
    print(sol.maxSubArray(nums))