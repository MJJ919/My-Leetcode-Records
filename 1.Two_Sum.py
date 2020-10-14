class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        compliments = {}
        for i, num in enumerate(nums):
            if target-num not in compliments:
                compliments[num] = i
            else:
                return [compliments[target-num], i]
                
