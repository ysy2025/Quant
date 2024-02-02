class Solution:
    def lst2Dict(self, lst):
        res = {}
        for each in lst:
            res[each] = res.get(each, 0) + 1

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


    def combinationSum2(self, candidates, target):
        def backtrack(state, target, choices, start, res):
            """ 回溯算法"""
            # 退出临界点
            if target == 0:
                print("===>now target is {0}".format(target))
                res.append(list(state))
                print("=====>now res is {0}\n".format(res))
                return

            # 非退出情况
            # 剪枝,加上不允许重复;从start开始遍历,避免生成重复子集
            for i in range(start, len(choices)):
                # 结束循环条件:子集和超过target
                print("target is {0} choices is {1} and i is {2}".format(target, choices[i], i))
                if target - choices[i] < 0:
                    break
                # else 可以继续计算;更新target start
                state.append(choices[i])
                # 递归选择
                print("{0}, {1}, {2}, {3}, {4}\n".format(state, target-choices[i], choices[i+1:], start, res))
                backtrack(state, target-choices[i], choices[i+1:], start, res)

                # 如果一直退出到这里,说明,没办法正常 return 节点没办法得到target=0;撤销选择,状态回退
                state.pop()

        state = []  # 状态（子集）
        candidates.sort()  # 对 candidates 进行排序
        print("sorted candidates is {0}".format(candidates))
        start = 0  # 遍历起始点
        res = []  # 结果列表（子集列表）
        backtrack(state, target, candidates, start, res)
        return self.distinct(res)



if __name__ == '__main__':
    # candidates = [2, 3, 5]
    # candidates = [10, 1, 2, 7, 6, 1, 5]
    candidates = [2,5,1,1,2,3,3,3,1,2,2]
    target = 5

    sol = Solution()
    res = sol.combinationSum2(candidates, target)
    print(res)