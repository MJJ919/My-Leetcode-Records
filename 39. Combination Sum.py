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
Time:
Space:
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def back(start,cur):
            n = sum(cur)
            if n==target and cur not in res:
                res.append(cur[:])
                return
            else:
                if n>target:
                    return
            for i in range(start, length):
                cur.append(candidates[i])
                back(i+1,cur)
                cur.pop()
        candidates.sort()
        res, length = [], len(candidates)
        back(0, [])
        return res
