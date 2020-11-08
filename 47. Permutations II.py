'''
https://leetcode.com/problems/permutations-ii/
Example 1:
Input: nums = [1,1,2]
Output:[[1,1,2],[1,2,1],[2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''

'''
Method below uses backtracking.
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(comb,counter):
            if len(comb) == len(nums):
                result.append(list(comb))
                return 
            for num in counter:
                if counter[num]>0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb,counter)
                    comb.pop()
                    counter[num] += 1
        
        backtrack([],Counter(nums))
        
        return result
