'''
https://leetcode.com/problems/permutation-sequence/
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        
        fac, num = [1], ['1']
        for i in range(1, n):
            fac.append(fac[i-1]*i)
            num.append(str(i+1))
        k = k-1  
        for i in range(n-1, -1, -1):
            pos = k//fac[i]
            res.append(num[pos])
            k = k%fac[i]
            del num[pos]
        
        return ''.join(res)
