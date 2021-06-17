'''
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
We are given an array nums of positive integers, and two positive integers left and right (left <= right).
Return the number of (contiguous, non-empty) subarrays such that the value 
of the maximum array element in that subarray is at least left and at most right.

Example:
Input: 
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(n):
            res = 0
            dp = 0
            for idx, num in enumerate(nums):
                if num<=n:
                    dp += 1
                    res += dp
                else:
                    dp = 0
            return res
        return count(right) - count(left-1)
      
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        pos = -1
        dp = 0
        for idx, num in enumerate(nums):
            if num<left:
                res += dp
            elif num>right:
                pos = idx
                dp = 0
            else:
                dp = idx-pos
                res += dp
        return res
