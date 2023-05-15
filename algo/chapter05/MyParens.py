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


def check_parens(text):
    """
    :param text:给一段text,检查括号匹配情况
    :return:是否正确
    """
    parens = "()[]{}"
    left_parens = "([{"
    relation = {"(":")", "{":"}", "[":"]"}

    def paren_finder(text):
        for i in range(len(text)):
            if text[i] not in parens:
                pass
            else:
                yield text[i], i

    myStack = MyStack()

    for paren, i in paren_finder(text):
        print(paren, i)
        # 如果是 left paren, 压栈
        if paren in left_parens:
            myStack.push(paren)
        else: # 如果是右括号,查看最外的paren对应的right paren
            outside = myStack.pop()
            if paren != relation[outside]: # 不匹配,报错
                print("Unmatching paren!")
            else:
                print("matching paren")

if __name__ == '__main__':
    check_parens("[12*(123+123)]")