'''
https://leetcode.com/problems/moving-average-from-data-stream/
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''
'''
Method below uses deque.
Time:O(1)
Space:O(n)
'''
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.size = size
        
    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.q.popleft()
        self.q.append(val)
        return sum(self.q)/len(self.q)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
