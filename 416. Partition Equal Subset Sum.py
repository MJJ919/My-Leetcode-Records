'''
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
'''
'''
Time:O(n*m)
Space:O(n*m)
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:  return False
        tar = sum(nums)//2
        dp = [[False for _ in range(tar+1)]for _ in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, tar+1):
                cur = nums[i-1]
                if cur>j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-cur]
        return dp[-1][-1]
        
