"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""


class Solution:
    def lstToDict(self, lst):
        res = {}
        for i in range(len(lst)):
            res[i] = lst[i]
        return res

    def distinct(self, lst):
        print(lst)
        lstDict = {}
        for i in range (len(lst)):
            eachDict = self.lstToDict(lst[i])
            print("\ni is {1} each dict is {0}".format(eachDict, i))

            if eachDict not in lstDict.values():
                lstDict[i] = eachDict
        print("循环结束{0}".format(lstDict))

        res = []
        for value in lstDict.values():
            temp = [None] * len(value)
            for k, v in value.items():
                temp[k] = v

            print("now temp is {0}".format(temp))

            res.append(temp)

        return res

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
        # return list(set(res))
        return res

    def afterPermute(self, nums):
        res1 = self.permute(nums)
        print("permute over, res is {0}\n".format(res1))

        res2 = self.distinct(res1)
        print("res2 is {0}".format(res2))

if __name__ == '__main__':
    sol = Solution()
    # nums = [1,1,2]
    # nums = [1, 2]
    nums = ["zhangsan"]
    res = sol.afterPermute(nums)

    # print(res)

    # print(len(res))
    #
    # print()