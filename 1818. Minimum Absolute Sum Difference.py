'''
https://leetcode.com/problems/minimum-absolute-sum-difference/
You are given two positive integer arrays nums1 and nums2, both of length n.
The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).
You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

|x| is defined as:
x if x >= 0, or
-x if x < 0.

Example 1:
Input: nums1 = [1,7,5], nums2 = [2,3,5]
Output: 3
Explanation: There are two possible optimal solutions:
- Replace the second element with the first: [1,7,5] => [1,1,5], or
- Replace the second element with the third: [1,7,5] => [1,5,5].
Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.
Example 2:

Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
Output: 0
Explanation: nums1 is equal to nums2 so no replacement is needed. This will result in an 
absolute sum difference of 0.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        diff_sum = 0
        diff = []
        for i in range(len(nums1)):
            minus = abs(nums1[i]-nums2[i])
            diff_sum += minus
            diff.append(minus)
        nums1.sort()
        change = 0
        for j in range(len(nums1)):
            idx = bisect.bisect_left(nums1, nums2[j])
            if idx>0:
                change = max(change, diff[j]-nums2[j]+nums1[idx-1])
            if idx<len(nums1):
                change = max(change, diff[j]-nums1[idx]+nums2[j])
        return (diff_sum - change)%(10**9+7)
