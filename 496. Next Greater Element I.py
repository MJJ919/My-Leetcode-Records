'''
https://leetcode.com/problems/next-greater-element-i/
You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, return -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = deque()
        d = defaultdict(int)
        res = []
        for i in range(len(nums2)-1, -1, -1):
            while s and s[-1]<=nums2[i]:
                s.pop()
            if not s:
                d[nums2[i]] = -1
            else:
                d[nums2[i]] = s[-1]
            s.append(nums2[i])
        for num in nums1:
            res.append(d[num])
        return res
