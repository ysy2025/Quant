# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.backup_stack = []

    def printAll(self):
        print("stack is {0}".format(self.stack))
        print("backup_stack is {0}".format(self.backup_stack))

    def length(self, input_stack):
        return len(input_stack)

    def push(self, node):
        # write code here
        self.stack.append(node)

    def pop(self):
        # return xx
        if (self.length(self.stack) == 0 and self.length(self.backup_stack) == 0):  # 空
            pass

        else:
            if (self.length(self.backup_stack) != 0):  # 备胎非空,首先pop备胎
                print("0!!!!!!!! 备胎非空,首先pop备胎")
                return self.backup_stack.pop()  # 备胎负责pop

            else:# 主胎n个备胎空,首先转移到备胎,然后主胎pop
                    print("2!!!!!!!! 主胎n个备胎空,首先转移到备胎,然后主胎pop")
                    while self.length(self.stack):
                        self.backup_stack.append(self.stack.pop())

                    print("==============")
                    print()
                    return self.pop()

if __name__ == '__main__':
    solution = Solution()

    solution.push(2)
    solution.push(3)
    a = solution.pop()
    print(solution.stack)
    print(solution.backup_stack)

    solution.push(1)
    b = solution.pop()
    solution.push(4)
    c = solution.pop()
    d = solution.pop()
    print(a, b, c, d)