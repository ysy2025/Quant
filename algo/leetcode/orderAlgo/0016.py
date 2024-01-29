"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

排序
双指针

"""
import math


class Solution:
    def threeSumClosest(self, nums, target):
        # 排序数组,初始化长度,初始化minDelta
        nums = sorted(nums)
        length = len(nums)

        plusDelta = math.inf
        plusFlag = 1

        minusDelta = math.inf
        minusFlag = -1

        print("nums is {0}, length is {1}".format(nums, length))

        # 特殊情况 直接返回
        if length < 3:
            sumClosest = 0
            return sumClosest

        # 正常情况,长度>2,数据普通
        for i in range(length-2):

            # 从左到右,分别指针移动
            left = i + 1
            right = length - 1
            print("i is {0} left is {1} right is {2}".format(i, left, right))

            while(left < right):
                temp = nums[i] + nums[left] + nums[right]
                # 正正好
                if temp == target:
                    sumClosest = target
                    return sumClosest
                # 偏大
                if temp >= target:
                    plusDelta = min(plusDelta, abs(temp - target))
                    print("plus delta is {0}, temp is {1}".format(plusDelta, temp))
                    right = right - 1
                # 偏小
                else:
                    minusDelta = min(minusDelta, abs(temp - target))
                    print("minusDelta delta is {0}, temp is {1}".format(minusDelta, temp))
                    left = left + 1

        print("minus delta is {0} and plus delta is {1}".format(minusDelta, plusDelta))
        if plusDelta < minusDelta:
            sumClosest = target + plusDelta
        else:
            sumClosest = target - minusDelta
        return sumClosest


if __name__ == '__main__':
    sol = Solution()
    #
    # nums = [0, 0, 1, -1, -10, 11, 0]
    nums = [2,3,8,9,10]
    target = 16
    print(sol.threeSumClosest(nums, target))