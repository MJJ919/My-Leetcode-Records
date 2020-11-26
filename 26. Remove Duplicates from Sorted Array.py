'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

'''
Method below uses 2 pointers.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i += 1
                nums[i]=nums[j]
        return i+1
