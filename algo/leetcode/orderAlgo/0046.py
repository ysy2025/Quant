"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""

class Solution:
    def permute(self, nums):

        if len(nums) == 1:
            return [nums]

        res = []

        for i in range(len(nums)):
            left = nums[:i] + nums[i+1:]
            right = nums[i]
            leftPermute = self.permute(left)
            # print("left permute is {0}".format(leftPermute))


            for each in leftPermute:
                # res.append(each.append(right))
                each.append(right)
                res.append(each)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [4,3,2, 1]
    # nums = [1, 2]
    res = sol.permute(nums)

    print(res)

    print(len(res))