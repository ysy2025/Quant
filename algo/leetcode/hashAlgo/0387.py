"""
给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。



示例 1：

输入: s = "leetcode"
输出: 0
示例 2:

输入: s = "loveleetcode"
输出: 2
示例 3:

输入: s = "aabb"
输出: -1

首先输出dict
然后根据dict,找到最小的值
"""
import math
from collections import Counter

class Solution:
    def str2Dict(self, str):
        res = {}
        for s in str:
            res[s] = res.get(s, 0) + 1
        return res

    def str2Index(self, str):
        res = {}
        for i in range(len(str)):
            if not res.get(str[i]):
                res[str[i]] = [i]
            else:
                temp = (res.get(str[i])).append(i)
        return res

    def firstUniqChar(self, s):
        sDict = self.str2Dict(s)
        print(sDict)

        sIndex = self.str2Index(s)
        print(sIndex)
        #
        # minIndex = math.inf
        #
        # for k,v in sDict:
        #     if v == 1:
        #         minIndex = min(minIndex, )



if __name__ == '__main__':
    s = "leetcode"

    sol = Solution()
    sol.firstUniqChar(s)

