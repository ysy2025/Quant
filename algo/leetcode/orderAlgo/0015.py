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
        # print(length)
        res = []

        for i in range(0,length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    # print("i j k is {0}, {1}, {2}".format(i,j,k))
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        print(res)
        # 去重
        if len(res) < 2:
            return res
        else:
            # 重复的
            needRemove = []
            for i in range(len(res) - 1):
                for j in range(i+1, len(res)):
                    if set(res[i]) == set(res[j]):
                        needRemove.append(j)

            needRemove = sorted(list(set(needRemove)))
            print("needRemove is {0}".format(needRemove))
            # 删除
            for i in range(len(needRemove)-1, -1, -1):
                print("i is {0}".format(needRemove[i]))
                res.pop(needRemove[i])
                print(res)

        return res




if __name__ == '__main__':
    sol = Solution()
    #
    # nums = [0, 0, 1, -1, -10, 11, 0]
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0,0,0,0]
    print(sol.threeSum(nums))
    # res = sol.threeSum(nums)
    # print(res)

    # a = [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]
    # print(a[0] == a[2])
