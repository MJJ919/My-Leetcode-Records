'''
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
Follow up: Could you implement the O(n) solution? 

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        res = 0
        for num in n:
            if num-1 not in n:
                cur = num
                count = 1
                while cur+1 in n:
                    cur += 1
                    count += 1
                res = max(count, res)
        return res
        
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:    return 0
        nums.sort()
        long = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                if nums[i] == nums[i-1]+1:
                    cur += 1
                else:
                    long = max(long,cur)
                    cur = 1
        return max(cur,long)
    
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]
        d = {}
        def find(num):
            if parent[num] != num:
                parent[num] = find(parent[num])
            return parent[num]
        
        def union(n1, n2):
            r1 = find(n1)
            r2 = find(n2)
            if r1 == r2:    return
            if size[r1]>size[r2]:
                size[r1] += size[r2]
                parent[r2] = r1
            else:
                size[r2] += size[r1]
                parent[r1] = r2
                
        for i in range(n):
            if nums[i] in d:
                continue
            d[nums[i]] = i
            if nums[i]-1 in d:
                union(i, d[nums[i]-1])
            if nums[i]+1 in d:
                union(i, d[nums[i]+1])
        return max(size) if size else 0
