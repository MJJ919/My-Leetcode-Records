'''
https://leetcode.com/problems/missing-ranges/
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. 
That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
 
Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        res = []
        nums = [lower-1] + nums + [upper+1]
        for i in range(1, len(nums)):
            if nums[i-1]+1 != nums[i]:
                self.getrange(res, nums[i-1], nums[i])
        return res
    
    def getrange(self, res, start, end):
        if start+2 == end:
            res.append(str(start+1))
        else:
            res.append(str(start+1)+"->"+str(end-1))

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        if not nums:
            if lower==upper:    res.append(str(lower))
            else:   res.append(str(lower)+'->'+str(upper))
            return res
        if lower != nums[0]:    nums = [lower-1] + nums
        if upper != nums[-1]:   nums = nums + [upper+1]
        print(nums)
        for i in range(1, len(nums)):
            string = ''
            if nums[i]==nums[i-1]+2:
                string+=str(nums[i-1]+1)
            elif nums[i]>nums[i-1]+2:
                string+= str(nums[i-1]+1)+'->'+str(nums[i]-1)
            if string:  res.append(string)
        return res    
