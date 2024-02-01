"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

输入: nums = [2,3,1,1,4]
==> 贪心,得到每个数能跳到最远的索引 [2, 4, 3, 4, 8]

从第一个开始

输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
"""

class Solution:
    def jump(self, nums):
        if len(nums) <= 1:
            return 0

        # 贪心,得到每个数能跳到最远的索引 [2, 4, 3, 4, 8]
        greedy = [None] * len(nums)
        for i in range(len(nums)):
            greedy[i] = i + nums[i]
        print("after greedy is {0}".format(greedy))

        # 长度, 索引, 步数
        length = len(nums)-1
        index = 0
        # print("beginning ==> length is {0} index is {1} steps is {2} greedy[index] is {3}".format(length, index, steps, greedy[index]))

        # 遍历,如果知道最后都不大于len,则达不到
        while index < length:
            print("now index is {0} and length is {1} greedy[index] is {2}".format(index, length, greedy[index]))
            if greedy[index] >= length:
                print("可以跳到尾巴了, 截取为 {0}".format(nums[:index+1]))
                return 1 + self.jump(nums[:index+1])
            index += 1
        # 到了最后一个才满足条件
        raise Exception("不可能到达")



if __name__ == '__main__':
    nums = [1,2,3]

    sol = Solution()
    print(sol.jump(nums))