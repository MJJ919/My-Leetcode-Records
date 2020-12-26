'''
https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses 
have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = now = 0
        for i in nums:
            pre, now = now, max(pre+i, now)
        return now            

'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def rob(self, nums):
        if not nums:    return 0
        if len(nums)<3: return max(nums)
        a = []
        a.append(nums[0])
        a.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            a.append(max(a[i-1], a[i-2]+nums[i]))
        return a[-1]
