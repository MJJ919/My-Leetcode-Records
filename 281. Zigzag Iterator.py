'''
https://leetcode.com/problems/zigzag-iterator/
Given two 1d vectors, implement an iterator to return their elements alternately.

Example:
Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
'''
'''
Time:O(n)
Space:O(n)
'''
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [v1, v2]
        self.p_v = 0
        self.p_e = 0
        self.total = len(v1)+len(v2)
        self.out = 0

    def next(self) -> int:
        ret = None
        while True:
            cur_v = self.v[self.p_v]
            if self.p_e<len(cur_v):
                ret = cur_v[self.p_e]
            
            self.p_v = (self.p_v+1)%len(self.v)
            if self.p_v == 0:
                self.p_e += 1
            if ret is not None:
                self.out += 1
                return ret

    def hasNext(self) -> bool:
        return self.out<self.total

    # Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
