'''
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
Return the length of the shortest, non-empty, contiguous subarray of nums with sum at least k.
If there is no non-empty subarray with sum at least k, return -1.

Example 1:
Input: nums = [1], k = 1
Output: 1
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        d = deque()
        prefix = [0]
        res = float('inf')
        for num in nums:
            prefix.append(prefix[-1]+num)
        for idx in range(len(prefix)):
            while d and prefix[d[-1]]>=prefix[idx]:
                d.pop()
            while d and prefix[idx]-prefix[d[0]]>=k:
                res = min(res, idx-d.popleft())
            d.append(idx)
        return res if res!=float('inf') else -1
