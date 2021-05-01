'''
https://leetcode.com/problems/powerful-integers/
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.
An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.
You may return the answer in any order. In your answer, each value should occur at most once.

Example 1:
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
'''
'''
Time:O(n*m)
Space:O(n*m)
'''
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        m = bound if x==1 else int(math.log(bound, x))
        n = bound if y==1 else int(math.log(bound, y))
        res = set()
        for i in range(m+1):
            for j in range(n+1):
                s = x**i+y**j
                if s<=bound:
                    res.add(s)
                if y==1:    break
            if x==1:    break
        return list(res)
