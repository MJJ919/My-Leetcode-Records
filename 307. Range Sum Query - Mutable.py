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
Space:O(1)
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i]=val

    def sumRange(self, i: int, j: int) -> int:
        s = 0
        for n in range(i, j+1):
            s += self.nums[n]
        return s
