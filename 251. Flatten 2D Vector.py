'''
https://leetcode.com/problems/flatten-2d-vector/
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

Example:
Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
'''
'''
Time:O(1)
Space:O(1)
'''
class Vector2D(object):
    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.v = v
        self.p1 = 0
        self.p2 = 0
        
    def tonext(self):
        while self.p1<len(self.v) and self.p2 == len(self.v[self.p1]):
            self.p1 += 1
            self.p2 = 0
            
    def next(self):
        """
        :rtype: int
        """
        self.tonext()
        num = self.v[self.p1][self.p2]
        self.p2 += 1
        return num
            
    def hasNext(self):
        """
        :rtype: bool
        """
        self.tonext()
        return self.p1<len(self.v)
