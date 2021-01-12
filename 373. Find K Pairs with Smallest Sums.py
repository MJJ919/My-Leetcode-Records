'''
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l = []
        k = min(k, len(nums1)*len(nums2))
        for i in nums1:
            for j in nums2:
                l.append([i,j])
        l.sort(key=sum)
        return l[:k]
 
'''

'''
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, ([i,j] for i in nums1 for j in nums2), key=sum)
