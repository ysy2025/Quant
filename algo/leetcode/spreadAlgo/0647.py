"""
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。



示例 1：

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

"""

class Solution:
    def spread(self, s, left, right, count):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
            print("now left is {0} and right is {1} and count is {2} and substring is {3}".format(left, right, count, s[left:right+1]))
        return left + 1, right - 1, count

    def countSubstrings(self, s: str) -> int:
        count = 0

        # 奇数回文
        for i in range(len(s)):
            left, right, count = self.spread(s, i, i, count)

        # 偶数回文
        for i in range(len(s) - 1):
            left, right, count = self.spread(s, i, i+1, count)

        return count
if __name__ == '__main__':
    solution = Solution()
    s = "aaabbbaaa"
    print(solution.countSubstrings(s))