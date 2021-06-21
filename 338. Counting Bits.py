'''
https://leetcode.com/problems/counting-bits/
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num+1):
            res.append(res[i//2]+i%2)
        return res
        
'''
Time:O(nk)
Space:O(n)
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            count = 0
            while i!=0:
                if i&1:
                    count += 1
                i = i>>1
            res.append(count)
        return res
        
