'''
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

Example 1:
Input: data = [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        s = sum(data)
        cursum = sum(data[:s])
        res = s - cursum
        for i in range(1, len(data) - s + 1):
            cursum = cursum - data[i-1] + data[i+s-1]
            res = min(res, s - cursum)
        return res
