"""
1423. 可获得的最大点数
中等
相关标签
相关企业
提示
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。



示例 1：

输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
示例 2：

输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
示例 3：

输入：cardPoints = [9,7,7,9,7,7,9], k = 7
输出：55
解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
示例 4：

输入：cardPoints = [1,1000,1], k = 1
输出：1
解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。
示例 5：

输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
输出：202

"""
import math
class Solution:
    def maxScore(self, cardPoints, k):
        # 这题相比前面的题目加了一丢丢小的变通: 题目要求首尾串最大点数，其实就是求非首尾串的连续序列的最小点数,牛逼
        length = len(cardPoints)
        #特解
        if k == length:
            return sum(cardPoints)

        # Step 1: 定义需要维护的变量们 (对于滑动窗口类题目，这些变量通常是最小长度，最大长度，或者哈希表)
        # 反过来的cards数量
        m = length - k

        minScore = math.inf

        sumScore = 0

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0

        for end in range(length):
            # Step 3: 更新需要维护的变量, 有的变量需要一个if语句来维护 (比如最大最小长度)
            sumScore += cardPoints[end]
            # 窗口长度固定,判断限定超标了
            if end >= m - 1:
                minScore = min(sumScore, minScore)
                sumScore -= cardPoints[start]
                start += 1

        return sum(cardPoints) - minScore


if __name__ == '__main__':
    solution = Solution()
    cardPoints = [1,20,1,20,8,9,8,9]
    k = 4
    print(solution.maxScore(cardPoints, k))