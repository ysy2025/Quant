"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        if len(s) == 2:
            return 1 if s[0] == s[1] else 2
        # 初始化最大长度为1
        maxLength = 1
        khars = list(s)
        maxList = khars[:1]

        for khar in khars[1:]:
            print("now maxList is {0}, khar is {1}".format(maxList, khar))
            # 没有重复
            if khar not in maxList:
                maxList.append(khar)
                maxLength = max(maxLength, len(maxList))
            # 有重复
            else:
                # 找到索引
                sameIndex = maxList.index(khar)
                maxList = maxList[sameIndex+1:] + [khar]
        return maxLength

if __name__ == '__main__':
    solution = Solution()

    stringA = "lebronjameshasfourwaterreward"
    stringB="abcdew"

    resB = solution.lengthOfLongestSubstring(stringB)
    print(resB)
