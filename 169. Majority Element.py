'''
https://leetcode.com/problems/majority-element/
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''

'''
The method below uses hashmap.
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = defaultdict(int)
        n = len(nums)
        for i in nums:
            dict[i] = dict[i] + 1
            if dict[i] > n/2:
                return i

'''
The method below uses sorting.
Time:O(nlgn)
Space:O(1)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m = len(nums)/2
        return nums[m]
                
'''
The method below uses Boyer-Moore Voting Algorithm.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i
            count += (1 if i == candidate else -1)
        return candidate
