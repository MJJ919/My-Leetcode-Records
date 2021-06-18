'''
https://leetcode.com/problems/range-sum-query-mutable/
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

Example:
Given nums = [1, 3, 5]
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
'''
'''
Time:O(n)
Space:O(sqrt(n))
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        ran = math.sqrt(len(nums))
        self.seg = math.ceil(len(nums)/ran)
        self.d = [0 for _ in range(self.seg)]
        for i in range(len(nums)):
            self.d[i//self.seg] += nums[i]
        

    def update(self, i: int, val: int) -> None:
        self.d[i//self.seg] += val-self.nums[i]
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        s = 0
        start = i//self.seg
        end = j//self.seg
        if start == end:
            for idx in range(i, j+1):
                s += self.nums[idx]
        else:
            for idx in range(i, (start+1)*self.seg):
                s += self.nums[idx]
            for idx in range(start+1, end):
                s += self.d[idx]
            for idx in range(end*self.seg, j+1):
                s += self.nums[idx]
        return s
