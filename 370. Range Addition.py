'''
https://leetcode.com/problems/range-addition/
Assume you have an array of length n initialized with all 0's and are given k update operations.
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray 
A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.
'''
'''
Time:O(n+k)
Space:O(1)
'''
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0 for _ in range(length+1)]
        for update in updates:
            start = update[0]
            end = update[1]
            res[start] += update[2]
            res[end+1] -= update[2]
        for i in range(1, length+1):
            res[i] += res[i-1]
        res.pop()
        return res
