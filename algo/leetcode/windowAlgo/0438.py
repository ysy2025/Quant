"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。



示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        # Step 1: 定义需要维护的变量们 (对于滑动窗口类题目，这些变量通常是最小长度，最大长度，或者哈希表)
        resList = []
        hashMap = {}
        hashMap_p = {}

        # Step 1.1： 同时把p的哈希表也建立了 (这个哈希表不需要维护，为定值)
        hashMap_p = {}
        for char in p:
            hashMap_p[char] = hashMap_p.get(char, 0) + 1

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            print("\n===> 现在 start 是{0} end 是{1} hashMap is {2} resList 是{3}, s[end] is {4}".
                  format(start, end, hashMap, resList, s[end]))
            # Step 3: 更新需要维护的变量 (hashmap)， 如果hashmap == hashmap_p，代表找到了一个解，加入到res
            # 遍历,写进去
            hashMap[s[end]] = hashMap.get(s[end], 0) + 1

            if hashMap == hashMap_p:
                resList.append(start)
            print("===> 修改hash 判断结束 现在 start 是{0} end 是{1} hashMap is {2} resList 是{3}, s[end] is {4}".
                  format(start, end, hashMap, resList, s[end]))
            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (hashmap)
            if end >= len(p) - 1:
                hashMap[s[start]] -= 1
                if hashMap[s[start]] == 0:
                    del hashMap[s[start]]
                start += 1
            print("最后 start 是{0} end 是{1} hashMap is {2} resList 是{3}, s[end] is {4}".
                  format(start, end, hashMap, resList, s[end]))
        return resList


if __name__ == '__main__':
    s = "aaaabcaabc"
    p = "abc"
    solution = Solution()

    print(solution.findAnagrams(s, p))