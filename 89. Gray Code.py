'''
https://leetcode.com/problems/gray-code/
The gray code is a binary numeral system where two successive values differ in only one bit.
Given an integer n representing the total number of bits in the code, return any sequence of gray code.
A gray code sequence must begin with 0.
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]
        if n==1:    return res
        for i in range(2,n+1):
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] | 1<<i-1)
        return res
