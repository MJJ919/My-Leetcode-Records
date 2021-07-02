'''
https://leetcode.com/problems/find-k-closest-elements/
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        for num in arr:
            if len(res)<k:
                heapq.heappush(res, num)
                continue
            else:
                temp = heapq.heappop(res)
                if abs(temp - x) > abs(num - x):
                    heapq.heappush(res, num)
                else:
                    heapq.heappush(res, temp)
        return sorted(res)
