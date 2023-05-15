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


if __name__ == '__main__':
    myStack = MyStack()

    for i in range(10):
        myStack.push(i)

    myStack.print_all()

    # while not myStack.is_empty():
    #     print(myStack.pop())
    #
    myStack2 = []
    while not myStack.is_empty():
        myStack2.append(myStack.pop())

    print(myStack2)
