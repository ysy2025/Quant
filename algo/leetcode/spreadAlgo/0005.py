"""
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


能想到的只有暴力办法了

"""

class Solution():
    def isPalindrome(self, string):
        if len(string) == 1:
            return 1
        if len(string) == 2:
            return string[0] == string[1]
        left = 0
        right = len(string) - 1
        flag = 1
        while (right - left >= 1):
            print("left is {0}, right is {1}".format(left, right))
            if string[left] != string[right]:
                flag = 0
                break
            left += 1
            right -= 1

        return flag

    def longestPalindrome(self, s: str):
        maxLength = 1
        maxString = s[0]
        for start in range(len(s)):
            print("\n")
            for end in range(start+1,len(s)+1):
                print("现在start is {0}, end is {1}, string is {2}".format(start, end, s[start:end]))
                if self.isPalindrome(s[start:end]):
                    print("string is {0}, 是回文".format(s[start:end]))
                    if maxLength < end - start:
                        maxLength = end - start
                        maxString = s[start:end]
        return maxString



"""
中心扩展法

枚举每个位置，把每个位置当作回文子串的中心，这个过程中记录你想要得到的答案。
牛逼
"""

class NewSolution():
    def longestPalindrome(self, s: str) -> str:
        def spread(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start, end = 0, 0
        # 奇数回文
        for i in range(len(s)):
            l, r = spread(i, i)
            if r - l > end - start:
                start, end = l, r
        # 偶数回文
        for i in range(len(s) - 1):
            l, r = spread(i, i + 1)
            if r - l > end - start:
                start, end = l, r
        return s[start:end + 1]


if __name__ == '__main__':
    solution = Solution()

    s = "aba"
    print("maxLength 回文 is {0}".format(solution.longestPalindrome(s)))

    # solution.isPalindrome(s)