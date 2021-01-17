'''
https://leetcode.com/problems/remove-element/
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

'''
Method below uses 2 pointers.
Time:O(n)
Space:O(1)
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i += 1
        return i

class Solution(object):
    def removeElement(self, nums, val):
        i,j=0,len(nums)
        while i<j:
            if nums[i]==val:
                nums[i]=nums[j-1]
                j -= 1
            else:
                i += 1
        return j
    
'''
Method below doesn't use pointers
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)
