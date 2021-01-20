'''
https://leetcode.com/problems/jump-game-ii/
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        maxpos = nums[0]
        maxstep = nums[0]
        jump = 1
        for i in range(len(nums)):
            if maxpos<i:
                jump += 1
                maxpos = maxstep
            maxstep = max(maxstep, nums[i]+i)
        return jump
