'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = {}
        for i,ch in enumerate(numbers):
            if ch in a:
                return(a[ch], i+1)
            a[target-ch]=i+1

'''
Method below uses two pointers.
'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i<j:
            sum = numbers[i]+numbers[j]
            if sum == target:
                return (i+1,j+1)
            if sum > target:
                j = j-1
            if sum < target:
                i = i+1
        
