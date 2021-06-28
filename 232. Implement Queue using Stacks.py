'''
https://leetcode.com/problems/implement-queue-using-stacks/
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
'''
'''
Time:O(1)
Space:O(n)
'''
class MyQueue:
    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, x: int) -> None:
        self.l1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.l2.pop()
        
    def peek(self) -> int:
        if not self.l2:
            while self.l1:
                self.l2.append(self.l1.pop())
        return self.l2[-1]

    def empty(self) -> bool:
        return False if self.l1 or self.l2 else True

'''
2 stacks
Time:O(n) for push, O(1) for else.
Space:O(n)
'''
class MyQueue(object):

    def __init__(self):
        self.d1 = []
        self.d2 = []

    def push(self, x):
        while self.d1:
            self.d2.append(self.d1.pop())
        self.d1.append(x)
        while self.d2:
            self.d1.append(self.d2.pop())

    def pop(self):
       return self.d1.pop()

    def peek(self):
        return self.d1[-1]

    def empty(self):
        return not self.d1
        
'''
deque
Time:O(1)
Space:O(n)
'''
class MyQueue(object):

    def __init__(self):
        self.d = deque()

    def push(self, x):
        self.d.append(x)

    def pop(self):
        return self.d.popleft()

    def peek(self):
        return self.d[0]

    def empty(self):
        return not self.d
