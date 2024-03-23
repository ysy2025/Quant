"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

"""

class Solution:
    def wordBreak(self, s, wordDict):
        wordDictL = len(wordDict)
        i = 0
        while i < wordDictL:
            # 如果等于,直接返回
            if wordDict[i] == s:
                return True
            else:
                # 和head相同
                if s.startswith(wordDict[i]):
                    wordL = len(wordDict[i])
                    if self.wordBreak(s[wordL:], wordDict):
                        return True
                    else:
                        i += 1
                else:
                    i += 1
        return False

if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet","code"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))