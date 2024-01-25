"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。



示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

 同样的窗口函数，套公式试试

"""
import sys

class Solution:
    def minSubArrayLen(self, target, nums):
        if target > sum(nums) or target < min(nums):
            return 0
        # Step 1: 定义需要维护的变量, 本题求最小长度，所以需要定义min_len, 该题隐含了去重，需要一个哈希表
        minLength = sys.maxsize - 1
        sumHash = {}

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(1, len(nums)+1):
            # Step 3
            # 更新需要维护的变量 (minLength, sumHash)
            # i.e. 把窗口区间内部元素求和，加入哈希表，使其频率加1，并且更新最大长度
            print("===>  now (nums[start:end]) is {0}, start is {1}, end is {2}\n".format(nums[start:end], start, end))
            addResult = sum(nums[start:end])

            # 和小于target，继续累加
            if addResult < target:
                # if len(hashmap) == end - start + 1:
                sumHash[addResult] = sumHash.get(addResult, 0) + 1
                # minLength = min(minLength, end-start)

            # Step 4:
            # 达标和超标了
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
            while addResult >= target:
                sumHash[addResult] = sumHash.get(addResult, 0) + 1
                minLength = min(minLength, end - start)
                # if addResult == target:
                #     # if len(hashmap) == end - start + 1:
                #     sumHash[addResult] = sumHash.get(addResult, 0) + 1
                #     minLength = min(minLength, end - start)
                #     print("|||")
                #     print("now start is {1}, end is {2}".format(nums[start:end], start, end))
                #     print("now sumhash is {0}， minLength is {1}".format(sumHash, minLength))
                print(">>>"*6)
                print("now start is {1}, end is {2} and addResult is {0}".format(addResult, start, end))
                print("now sumhash is {0}， minLength is {1}".format(sumHash, minLength))
                print("\n")
                start += 1
                addResult = sum(nums[start:end])

        return minLength if minLength != sys.maxsize-1 else 0

if __name__ == '__main__':
    solution = Solution()

    target = 11
    nums = [1,2,3,4,5]

    res = solution.minSubArrayLen(target, nums)
    print(res)
