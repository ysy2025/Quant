"""
bt算法,回溯之

"""

class Solution:

    def combine(self, n, k):
        nums = [i for i in range(1, n+1)]

        res = []  # 存放所欲符合条件结果的集合
        path = []  # 存放当前符合条件的结果

        def backtracking(nums):  # nums 为选择元素列表
            if len(path) == k:  # 说明找到了一组符合条件的结果
                res.append(path[:])  # 将当前符合条件的结果放入集合中
                return

            for i in range(len(nums)):  # 枚举可选元素列表
                # 避免重复
                if nums[i] not in path:
                    path.append(nums[i])  # 选择元素
                    backtracking(nums)  # 递归搜索
                    path.pop()  # 撤销选择
                else:
                    return

        backtracking(nums)
        return res

if __name__ == '__main__':
    n = 5
    k = 3
    sol = Solution()
    res = sol.combine(n, k)
    print(res)