"""
bt算法,回溯之

"""

class Solution:

    def exist(self, board, word):
        res = []  # 存放所欲符合条件结果的集合
        path = ''  # 存放当前符合条件的结果

        def bt(board, i, j, path, passed):
            # 边界条件
            if (i >= length) or (j >= height):
                return
            if path == word: # 说明找到了一组符合条件的结果
                res+(path) # 将当前符合条件的结果放入集合中
                return

            print("now i is {0}, j is {1}, board[i][j] is {2}, path is {3}, 是否踩过? {4}".format(i, j, board[i][j], path,
                                                                                              passed[i][j]))
            # 枚举可选元素列表范围
            while i < length and j < height:
                # 只能踩一次
                if passed[i][j] == 0:
                    path += board[i][j] # 选择元素,递归搜索
                    passed[i][j] = 1 # 改变踩过的状态
                    for yidong in [[1,0], [-1, 0], [0, 1], [0, -1]]:  # 选择元素
                        bt(board, i + yidong[0], j + yidong[1], path, passed)
                    path = path[:-1] # 回溯,撤销选择

            # while i < length and j < height and len(path) < len(word) and passed[i][j] != 0: # 限定在board范围内部,而且只能用1次
            #     passed[i][j] = 1 # 表示已经踩过了
            #     bt(board, i+1, j, path+(board[i][j]), passed) # 选择元素, 递归搜索, # 撤销选择
            #     bt(board, i-1, j, path+(board[i][j]), passed)
            #     bt(board, i, j+1, path+(board[i][j]), passed)
            #     bt(board, i, j-1, path+(board[i][j]), passed)

        # 遍历每个字符,使用bt算法
        length = len(board)
        height = len(board[0])

        passed = [[0 for i in range(height)] for i in range(length)]

        for i in range(length):
            for j in range(height):
                bt(board, i, j, path, passed)

        pass

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    sol = Solution()
    sol.exist(board, word)