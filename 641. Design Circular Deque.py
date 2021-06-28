'''
https://leetcode.com/problems/design-circular-deque/
'''
'''
'''
class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.l = [0 for _ in range(k)]
        self.p1 = 0
        self.p2 = -1
        self.size = 0
        
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.p1 -= 1
            if self.p1<0:
                self.p1 += self.k
            self.l[self.p1] = value
            self.size += 1
            if self.size == 1:
                self.p2 = self.p1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.p2 = (self.p2+1)%self.k
            self.l[self.p2] = value
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.p1 = (self.p1+1)%self.k
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.p2 -= 1
            if self.p2<0:
                self.p2 += self.k
            self.size -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.l[self.p1]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.l[self.p2]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0 

    def isFull(self) -> bool:
        return self.size == self.k
