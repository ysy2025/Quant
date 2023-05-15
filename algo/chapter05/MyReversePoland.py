class MyStack:
    def __init__(self): # 通过list实现栈
        self._elems = []

    def is_empty(self):
        return len(self._elems) == 0

    def top(self):
        if self.is_empty():
            raise StackUnderFlow("null stack")
        else:
            return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow("null stack")
        else:
            return self._elems.pop(-1)

    def print_all(self):
        print(self._elems)


class StackUnderFlow(ValueError):
    pass


def calc(left, right, input_string):
    if input_string == "+":
        return left + right
    if input_string == "-":
        return left - right
    if input_string == "*":
        return left * right
    if input_string == "/":
        return left / right

def calculate_string(input_list):
    # 指定计算符号
    parens = "+-*/"

    # 初始化栈
    myStack = MyStack()

    # 初始化 length
    length = 0

    # 初始化 is_number
    is_number = []

    for i in range(len(input_list)):
        print("this is i of input list:{0}".format(input_list[i]))
        print("this is list of whether is number: {0}".format(is_number))
        print("let us check stack: {0}".format(myStack.print_all()))

        if input_list[i] not in parens: # 普通数字, 压栈即可
            myStack.push(int(input_list[i]))
            is_number.append(1)
            length += 1
        else: # 计算符号
            if i < 2:
                raise Exception("异常参数")
            else:
                if not (is_number[length-1] == 1 and is_number[length-2] == 1):
                    raise Exception("数值不够")
                else:
                    # 首先出栈
                    right = myStack.pop()
                    is_number.pop()
                    length -= 1

                    left = myStack.pop()
                    is_number.pop()
                    length -= 1

                    res = calc(left, right, input_list[i])

                    # 将计算结果压栈
                    myStack.push(res)
                    is_number.append(1)
                    length += 1

    return myStack.pop()

if __name__ == '__main__':
    input_string = ""
    res = calculate_string(["3", "5", "-", "6", "17", "4", "*", "+", "*", "3", "/"])
    print(res)