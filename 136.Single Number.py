'''
https://leetcode.com/problems/single-number/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1
'''
'''
Bit manipulation.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

'''
Time:
Space:
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
