'''
https://leetcode.com/problems/design-circular-queue/
'''
'''
'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.l = []
        self.p1 = 0
        self.p2 = 0
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.l.append(value)
            self.size += 1
            self.p2 = len(self.l)-1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.size -= 1
            self.p1 += 1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.l[self.p1]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.l[self.p2]
        else:
            return -1
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
