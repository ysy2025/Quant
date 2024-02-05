class Solution:
    def str2Index(self, str):
        res = {}
        for i in range(len(str)):
            if not res.get(str[i]):
                res[str[i]] = [i]
            else:
                temp = (res.get(str[i])).append(i)
        return res

    def isIsomorphic(self, s, t):
        sIndex = self.str2Index(s)
        tIndex = self.str2Index(t)

        sList = [v for k, v in sIndex.items()]
        tList = [v for k, v in tIndex.items()]

        return True if sList == tList else False

if __name__ == '__main__':
    s = "foo"
    t = "bar"

    sol = Solution()
    print(sol.isIsomorphic(s, t))

    word = zip(*set(zip(s, t)))
    for w in word:
        print(w)