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
        res = [0]*(length+1)
        for i in updates:
            res[i[0]] += i[2]
            res[i[1]+1] -= i[2]
        temp = 0
        for j in range(length):
            temp += res[j]
            res[j] = temp
        res.pop()
        return res
