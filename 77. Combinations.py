'''
https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
'''
Time:O(n*2^n)
Space:O(n*2^n)
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def back(start, subset):
            if len(subset)==k:
                res.append(subset[:])
            for i in range(start, n+1):
                subset.append(i)
                back(i+1, subset)
                subset.pop()
        res = []
        back(1, [])
        return res
                
        res = []
        back(1, [])
        return res
