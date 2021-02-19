'''
https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        counter = Counter(nums)
        for num, freq in counter.items():
            bucket[freq].append(num)
        l = []
        for bt in bucket:
            if bt:
                for num in bt:
                    l.append(num)
        return l[-k:]
'''
Time:O(Nlogk)
Space:O(N+k)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)
