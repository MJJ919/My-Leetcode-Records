'''
Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j 
in the array such that nums[i] = nums[j] and 
the absolute difference between i and j is at most k.
'''

'''
Method below uses hashtable.
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i,ch in enumerate(nums):
            if ch in dict and i-dict[ch]<=k:
                return True
            dict[ch] = i
        return False
  
