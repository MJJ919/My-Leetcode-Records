'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

'''
Method below uses set function.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))!=len(nums)
        
 '''
 Method below uses hashtable.
 '''
 
 class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 1
        return False
        
'''
Method below uses sorted.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        for i in (range(len(nums)-1)):
            if nums[i] == nums[i+1]:
                return True
        return False
