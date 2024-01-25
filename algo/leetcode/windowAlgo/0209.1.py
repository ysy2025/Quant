import sys
class Solution:
    def minSubArrayLen(self, target, nums):
        if target > sum(nums):
            return 0
        # Step 1: 定义需要维护的变量, 本题求最小长度，所以需要定义min_len, 该题隐含了去重，需要一个哈希表
        minLength = sys.maxsize - 1
        sumHash = 0

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(nums)):
            print("end is {0} and num[end] is {1}".format(end, nums[end]))
            # Step 3
            # 更新需要维护的变量 (minLength, sumHash)
            sumHash += nums[end]

            # Step 4:
            # 达标和超标了
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
            while sumHash >= target:
                minLength = min(minLength, end - start + 1)
                sumHash -= nums[start]
                start += 1

        return minLength if minLength != sys.maxsize-1 else 0

if __name__ == '__main__':
    solution = Solution()
    nums = [9]
    target = 7

    print(solution.minSubArrayLen(target, nums))