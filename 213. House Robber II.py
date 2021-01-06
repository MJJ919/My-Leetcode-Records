'''
https://leetcode.com/problems/house-robber-ii/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums) if nums else 0
        pre1 = now1 = 0
        pre2 = now2 = 0
        for i in range(1,len(nums)):
            pre1, now1 = now1, max(now1, pre1+nums[i])
        for i in range(0, len(nums)-1):
            pre2, now2 = now2, max(now2, pre2+nums[i])
        return max(now1, now2)
