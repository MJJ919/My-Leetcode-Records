'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3]
'''
'''
Method below uses pop.
Time:O(n^2)
Space:O(1)
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, count = 1, 1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1
            i += 1
        return len(nums)
        
'''
Method below uses 2 pointers.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def removeDuplicates(self, nums):
        a = 0
        for i in nums:
            if a<=1 or nums[a-2]!=i:
                nums[a]=i
                a+=1
        return a
