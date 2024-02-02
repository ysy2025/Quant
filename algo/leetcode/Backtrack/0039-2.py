"""
我的思路其实已经很靠近了,但是没有想到剪枝,还有回溯这块差点意思
"""
class Solution:
    def combinationSum(self, candidates, target):

        def backtrack(state, target, choices, start, res):
            """回溯算法：子集和 I"""
            # 子集和等于 target 时，记录解
            if target == 0:
                res.append(list(state))
                return
            # 遍历所有选择
            # 剪枝二：从 start 开始遍历，避免生成重复子集
            for i in range(start, len(choices)):
                # 剪枝一：若子集和超过 target ，则直接结束循环
                # 这是因为数组已排序，后边元素更大，子集和一定超过 target
                if target - choices[i] < 0:
                    break
                # 尝试：做出选择，更新 target, start
                state.append(choices[i])
                # 进行下一轮选择
                backtrack(state, target - choices[i], choices, i, res)
                # 回退：撤销选择，恢复到之前的状态
                state.pop()

        state = []  # 状态（子集）
        candidates.sort()  # 对 candidates 进行排序
        start = 0  # 遍历起始点
        res = []  # 结果列表（子集列表）
        backtrack(state, target, candidates, start, res)
        return res

if __name__ == '__main__':
    candidates = [2, 3, 5]
    target = 6

    sol = Solution()
    res = sol.combinationSum(candidates, target)
    print(res)