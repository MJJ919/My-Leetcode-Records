'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
'''

# ^XOR stands for exclusively or
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
        
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = []
        for i in nums:
            if i not in nums1:
                nums1.append(i)
            else:
                nums1.remove(i)
        return nums1[0]
  

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
        
