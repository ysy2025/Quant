"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

递归
"""

class Solution:
    def lst2Dict(self, lst):
        res = {}
        for each in lst:
            res[each] = 1

        return res

    def distinct(self, lst):
        temp = []
        res = []
        for each in lst:
            eachDict = self.lst2Dict(each)
            if eachDict not in temp:
                temp.append(eachDict)
                res.append(each)
            else:
                pass

        return res


    def combinationSum(self, candidates, target):
        sortedNums = sorted(candidates)

        res = []

        if target < sortedNums[0]:
            return []
        elif target in sortedNums:
            res.append([target])

        for num in sortedNums:
            print("\nsortCan is {0} and each is {1}".format(sortedNums, num))
            remain = target - num
            remainCombine = self.combinationSum(candidates, remain)

            print("now remain is {0} and remainCombine is {1}".format(remain, remainCombine))

            for combine in remainCombine:
                if combine:
                    print("==> combine is {0}, num is {1}".format(combine, num))
                    combine.append(num)
                    print("===========> temp is {0}".format(combine))
                    res.append(combine)
                    print("now res is {0}".format(res))
                else:
                    pass

        return self.distinct(res)



if __name__ == '__main__':
    candidates = [2,3,7]
    target = 18
    sol = Solution()

    res = sol.combinationSum(candidates, target)
    print("!!!!!!!!!!{0}".format(res))