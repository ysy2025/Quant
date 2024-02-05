"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
"""

class Solution:
    def str2Dict(self, str):
        res = {}
        for s in str:
            res[s] = res.get(s, 0) + 1
        return res

    def isAnagram(self, s, t):
        # 特殊情况直接反馈
        if len(s) != len(t):
            return False

        sDict = self.str2Dict(s)
        tDict = self.str2Dict(t)

        print(sDict)
        print(tDict)

        return sDict == tDict

if __name__ == '__main__':
    # s = "axc"
    s = "anagrama"
    # t = "abdc"
    t = "nagaram"

    sol = Solution()
    res = sol.isAnagram(s, t)
    print(res)