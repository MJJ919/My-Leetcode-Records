'''
https://leetcode.com/problems/combination-sum/
Similar question: 40,216.
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

'''
Method below uses backtracking.
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def sum(start,comb,remain):
            if remain == 0:
                result.append(list(comb))
            elif remain<0:
                return
            
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                sum(i,comb,remain-candidates[i])
                comb.pop()
        sum(0,[],target)      
        return result
