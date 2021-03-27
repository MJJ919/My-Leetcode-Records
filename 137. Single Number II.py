'''
https://leetcode.com/problems/single-number-ii/
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
Example 1:
Input: nums = [2,2,3,2]
Output: 3
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = twice = 0
        for num in nums:
            once = ~twice & (once^num)
            twice = ~once & (twice^num)
        return once
        
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums))//2
