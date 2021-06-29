/*
https://leetcode.com/problems/maximum-frequency-stack/
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:
FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
*/
/*
Time:O(1)
Space:O(1)
*/
class FreqStack:

    def __init__(self):
        self.fre = defaultdict(list)
        self.ele = defaultdict(int)
        self.maxfre = 0

    def push(self, val: int) -> None:
        self.ele[val] += 1
        fre = self.ele[val]
        if fre>self.maxfre:
            self.maxfre = fre
        self.fre[fre].append(val)

    def pop(self) -> int:
        ele = self.fre[self.maxfre].pop()
        self.ele[ele] -= 1
        if len(self.fre[self.maxfre]) == 0:
            self.maxfre -= 1
        return ele
