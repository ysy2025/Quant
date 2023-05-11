class LNode:
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass

class DLNode(LNode):
    def __init__(self, elem, prev = None, next_ = None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self.is_empty():
            raise LinkedListUnderflow("LList is empty.")

        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return

        p = self._head
        while p.next is not None:
            p = p.next

        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")

        p = self._head
        if p.next is None:# 表中只有1个元素
            e = p.elem
            self._head = None
            return e

        else:# 多个元素
            while p.next.next is not None: # 直到 p.next是最后节点
                p = p.next
            e = p.next.elem
            p.next = None
            return e

    def find(self, pred):
        p = self._head # 首先定位head
        while p is not None: # 遍历
            if pred == p.elem:
                print("终于找到啦!")
                return p.elem
            p = p.next

    def printAll(self):
        p = self._head
        while p is not None:
            print(p.elem, end = '')
            if p.next is not None:
                print(', ', end = '')
            p = p.next
        print("")

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            p = p.next

    def reverse(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next #摘下head
            q._next = p # 继续摘下head

            p = q # head赋给p
        self._head = p

    def insert(self, n, elem):
        p = self._head
        print(p.elem)

        # 如果p是空的
        if p is None:
            # head插入
            if n > 0:
                raise Exception("长度不够")
            else:
                self._head = LNode(elem, self._head)

        # 如果p非空
        else:
            if n == 0:
                # 开头插入
                self._head = LNode(elem, p)

            else:
                # 中间插入;首先遍历
                while p is not None and n-1 != 0:
                    # 首先遍历
                    n -= 1
                    print("elem is {0}".format(p.elem))
                    p = p.next
                    print("n is ", n)

                # 遍历完事后,如果n!=0,则长度不够
                if n > 1:
                    raise Exception("长度不够")
                # 长度够,中间插入
                else:
                    newElem = LNode(elem, p.next)
                    p.next = newElem


class DLList(LList):
    def __init__(self):
        LList.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)

        # 空表
        if self._head is None:
            self._rear = p

        # 非空表
        else:
            p.next.prev = p
        self._head = p

if __name__ == '__main__':
    # llist1 = LNode(1)
    #
    # p = llist1
    #
    # for i in range(2, 11):
    #     p.next = LNode(i)
    #     p = p.next
    #
    # p = llist1
    # while p is not None:
    #     print(p.elem)
    #     p = p.next

    mlist1 = LList()
    for i in range(10):
        mlist1.prepend(i)

    for i in range(21, 30):
        mlist1.append(i)

    mlist1.find(26)
    mlist1.printAll()

    mlist1.insert(0, 11)
    mlist1.printAll()