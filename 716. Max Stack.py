'''
https://leetcode.com/problems/max-stack/
Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the MaxStack class:
MaxStack() Initializes the stack object.
void push(int x) Pushes element x onto the stack.
int pop() Removes the element on top of the stack and returns it.
int top() Gets the element on the top of the stack without removing it.
int peekMax() Retrieves the maximum element in the stack without removing it.
int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.

Example 1:
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]
'''
'''
Time:O(n)
Space:O(n)
'''
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        if not self.s:
            self.s.append([x, x])
        else:
            self.s.append([x, max(self.s[-1][1], x)])

    def pop(self) -> int:
        return self.s.pop()[0]

    def top(self) -> int:
        return self.s[-1][0]

    def peekMax(self) -> int:
        return self.s[-1][1]

    def popMax(self) -> int:
        m = self.s[-1][1]
        l = []
        while self.s[-1][0] != m:
            l.append(self.s.pop()[0])
        self.s.pop()
        for num in reversed(l):
            self.push(num)
        return m
