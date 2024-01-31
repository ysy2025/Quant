class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s) + [' '], sorted(t)
        for c1, c2 in zip(s, t):
            if c1 != c2: return c2


class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        temp = s+t
        from collections import Counter
        c = Counter(temp)
        for key, value in c.items():
            if value % 2 == 1:
                return key