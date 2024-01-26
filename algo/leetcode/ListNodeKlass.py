class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

class List2ListNode:
    def getListNode(self, l):
        if len(l) == 0:
            raise Exception("length error")
        if len(l) == 1:
            return ListNode(l[0], None)
        else:
            return ListNode(l[0], ListNode(l[1:]))