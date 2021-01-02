'''
Implement a last in first out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
'''
'''
Time:O(1)
Space:O(n)
'''
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q        
