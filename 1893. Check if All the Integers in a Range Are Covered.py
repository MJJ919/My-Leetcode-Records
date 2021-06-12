'''
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
You are given a 2D integer array ranges and two integers left and right. 
Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. 
Return false otherwise.
An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

Example 1:
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        print(ranges)
        for r in ranges:
            if left>=r[0] and left<=right:
                left = r[1]+1
        print(left)
        return left>right
