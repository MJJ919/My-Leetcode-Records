'''
https://leetcode.com/problems/find-the-duplicate-number/
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

'''
Modify the array.
Time:O(nlgn)
Space:O(1)
'''
class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                return nums[i]
        return False
