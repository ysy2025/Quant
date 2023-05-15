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

        elif (self.length(self.stack) == 0 and self.length(self.backup_stack) != 0):  # 元素都在备胎中
            print("0!!!!!!!! 元素都在备胎中")
            self.printAll()
            return self.backup_stack.pop()  # 备胎负责pop

        elif self.length(self.stack) == 1:  # 主胎只有1个,直接pop
            print("1!!!!!!!! 主胎只有1个,直接pop")
            self.printAll()
            return self.stack.pop()

        else:  # 主胎多个,首先转移到备胎,然后主胎pop
            print("2!!!!!!!! 主胎多个,首先转移到备胎,然后主胎pop")
            self.printAll()
            while self.length(self.stack) > 1:
                print("长度是", self.length(self.stack))
                self.backup_stack.append(self.stack.pop())

            print("长度是", self.length(self.stack))
            self.printAll()
            print("==============")
            print()
            return self.pop()

if __name__ == '__main__':
    solution = Solution()

    solution.push(1)
    solution.push(2)
    a = solution.pop()
    print(solution.stack)
    print(solution.backup_stack)

    solution.push(3)
    b = solution.pop()
    c = solution.pop()
    print(a, b, c)