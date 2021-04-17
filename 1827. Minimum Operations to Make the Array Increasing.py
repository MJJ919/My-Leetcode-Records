'''
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.
An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

Example 1:
Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums)<=1:    return 0
        res = 0
        for idx, num in enumerate(nums):
            if idx == 0: continue
            if nums[idx-1]>=num:
                temp = nums[idx-1]+1
                res += temp-num
                nums[idx] = temp
        return res
