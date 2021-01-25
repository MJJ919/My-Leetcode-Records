'''
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''
'''
Time:O(n**2)
Space:O(n)
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        ordered = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(ordered,num)
            if idx == len(ordered):
                ordered.append(num)
            else:
                ordered.insert(idx,num)
            res.append(idx)
        return reversed(res)
        
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res, index = [0 for _ in range(len(nums))], []
        for idx, num in enumerate(nums):
            index.append((idx,num))
        
        def merge(left, right):
            ordered, add = [], 0
            i, j = 0,0
            while i<len(left) and j<len(right):
                if left[i][1]>right[j][1]:
                    ordered.append(right[j])
                    add += 1
                    j += 1
                else:
                    ordered.append(left[i])
                    res[left[i][0]] += add
                    i += 1
            while j<len(right):
                ordered.append(right[j])
                j += 1            
            while i<len(left):
                ordered.append(left[i])
                res[left[i][0]] += add
                i += 1
            return ordered

            
        def divide(l):
            if len(l)==1:
                return l
            mid = len(l)//2
            left = divide(l[0:mid])
            right = divide(l[mid:len(l)])
            return merge(left, right)
        
        divide(index)
        return res
