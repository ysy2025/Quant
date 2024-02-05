"""
双指针算法
"""
class Solution:
    def isSubsequence(self, s, t):
        lenS = len(s)
        lenT = len(t)

        # 特殊情况
        if lenS > lenT:
            return False
        left, right = 0, 0

        # 双指针移动
        while left < lenS and right < lenT:
            # 对比每个字符
            # 相同,同时移动指针
            if s[left] == t[right]:
                left += 1
                right += 1

            # 不同,移动right,因为默认right要更长点;主要是把false的情况解释清楚
            else:
                # 剩余长度比较
                if len(s[left:]) >= len(t[right:]):
                    return False
                right += 1

        # 排除一切,可以返回true
        return True

if __name__ == '__main__':
    s = "axc"
    t = "abdc"

    sol = Solution()
    res = sol.isSubsequence(s, t)
    print(res)