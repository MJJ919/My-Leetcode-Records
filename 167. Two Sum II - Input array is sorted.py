'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = defaultdict(int)
        for i, ch in enumerate(numbers):
            if target-ch not in d:
                d[ch] = i+1
            else:
                return [d[target-ch], i+1]

'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def twoSum(self, numbers, target):
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
