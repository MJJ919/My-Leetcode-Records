'''
My method is a little bit awkward.
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    i += 1
                elif target <= nums[i]:
                    return i
                
