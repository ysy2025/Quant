"""
输入一个数字,返回括号的组合
比如3,输出 ()()() ()(()) (())() ((()))

"""


class Solution:
    def backTrace(self, res, left, right, path):  # 左右剩下的数量,string是当前构建的字符串
        print("1  now res is {0}, left is {1}, right is {2} path is {3}".format(res, left, right, path))
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.backTrace(res, left-1, right, path + '(')
            print("2  now res is {0}, left is {1}, right is {2} path is {3}".format(res, left, right, path))
        if left < right:
            self.backTrace(res, left, right-1, path + ')')
            print("3  now res is {0}, left is {1}, right is {2} path is {3}".format(res, left, right, path))

    def threeParenteses(self, param):
        res = []
        self.backTrace(res, param, param, '')
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.threeParenteses(3)
    print(res)
