class Solution:
    def combinationSum2(self, candidates, target):
        def backtrack(state, target, choices, start, res):
            """ 回溯算法"""
            # 退出临界点
            if target == 0:
                print("now target is {0}".format(target))
                res.append(list(state))
                return

            # 非退出情况
            # 剪枝,加上不允许重复;从start开始遍历,避免生成重复子集
            for i in range(start, len(choices)):
                # 结束循环条件:子集和超过target
                if target - choices[0] < 0:
                    break
                # else 可以继续计算;更新target start
                state.append(choices[0])
                # 递归选择
                backtrack(state, target-choices[0], choices[i+1:], start, res)

                # 如果一直退出到这里,说明,没办法正常 return 节点没办法得到target=0;撤销选择,状态回退
                state.pop()

        state = []  # 状态（子集）
        candidates.sort()  # 对 candidates 进行排序
        start = 0  # 遍历起始点
        res = []  # 结果列表（子集列表）
        backtrack(state, target, candidates, start, res)
        return res



if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 2

    sol = Solution()
    res = sol.combinationSum2(candidates, target)
    print(res)