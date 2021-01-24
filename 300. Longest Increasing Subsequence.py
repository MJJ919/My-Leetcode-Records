'''
https://leetcode.com/problems/longest-increasing-subsequence/
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''
'''
Time:O(n**2)
Space:O(n)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:    return 0
        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        res = 1
        for i in range(1,n):
            maxval = 0
            for j in range(0,i):
                if nums[i]>nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval+1
            res = max(dp[i],res)
        return res
        
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def find(dp, num):
            i, j = 0, len(dp)-1
            while i<=j:
                mid = (i+j)//2
                if dp[mid]>num:
                    j = mid-1
                elif dp[mid]<num:
                    i = mid+1
                else:
                    return mid
            return i
        
        n = len(nums)
        dp = []
        for num in nums:
            loc = find(dp, num)
            if loc == len(dp):
                dp.append(num)
            else:
                dp[loc] = num
        return len(dp)
