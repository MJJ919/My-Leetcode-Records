'''

The frequency of an element is the number of times it occurs in an array.
You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
Return the maximum possible frequency of an element after performing at most k operations.

Example 1:
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
'''
'''
Time:O(n**2)
Space:O(1)
'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        res = 1
        i = 0
        s = k
        nums.sort()
        for j in range(len(nums)):
            s += nums[j]
            while s<nums[j]*(j-i+1):
                s -= nums[i]
                i += 1
            res = max(res, j-i+1)
        return res
