'''
https://leetcode.com/problems/burst-balloons/
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. 
You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.
'''
'''
Time:O(n**3)
Space:O(n**2)
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1]+nums+[1]
        dp = [[0 for _ in range(n+2)]for _ in range(n+2)]
        for length in range(1,n+1):
            for left in range(1, n-length+2):
                right = left+length-1
                dp[left][right] = max(dp[left][i-1]+nums[right+1]*nums[i]*nums[left-1]+dp[i+1][right] for i in range(left, right+1))
        return dp[1][n]
