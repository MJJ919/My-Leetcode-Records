'''
https://leetcode.com/problems/contiguous-array/
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        prefix = 0
        d = defaultdict(int)
        d[0] = -1
        for idx, num in enumerate(nums):
            if num==0:
                nums[idx] = -1
        for idx, num in enumerate(nums):        
            prefix += num
            if prefix in d:
                res = max(res, idx-d[prefix])
            else:
                d[prefix] = idx
        return res
