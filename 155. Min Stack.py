'''
https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
'''
Time:O(1) for all operations
Space:O(n)
'''
class MinStack:
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append([val, val])
            return
        self.s.append([val, min(self.s[-1][1], val)])

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]


class MinStack:
    def __init__(self):
        self.s = []
        self.mins = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.mins or self.mins[-1]>=val:
            self.mins.append(val)
        
    def pop(self) -> None:
        num = self.s.pop()
        if self.mins[-1]==num:
            self.mins.pop()
        return num

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mins[-1]
