'''
https://leetcode.com/problems/jump-game-vi/
You are given a 0-indexed integer array nums and an integer k.
You are initially standing at index 0. In one move, you can jump at most k steps forward 
without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). 
Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

Example 1:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        q = deque()
        q.append(0)
        for i in range(1, len(nums)):
            while q and q[0]<i-k:
                q.popleft()
            dp[i] = nums[i]+dp[q[0]]
            while q and dp[q[-1]]<dp[i]:
                q.pop()
            q.append(i)
        return dp[q[-1]]
