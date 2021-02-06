'''
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
You are given an integer array nums. 
The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        min_value = [0 for _ in range(n)]
        max_value = [0 for _ in range(n)]
        min_value[0] = nums[0]
        max_value[0] = nums[0]
        
        for i in range(1, n):
            min_value[i] = min(min_value[i-1]+nums[i], nums[i])
            max_value[i] = max(max_value[i-1]+nums[i], nums[i])
        
        return max(abs(min(min_value)), max(max_value))
