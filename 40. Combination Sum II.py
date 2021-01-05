'''
https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
 
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''
'''
Time:O()
Space:O()
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(target, first, counter, cur):
            if target == 0:
                res.append(cur[:])
                return
            elif target < 0:
                return 
            for i in range(first, len(counter)):
                num, freq = counter[i]
                if freq > 0:
                    cur.append(num)
                    counter[i] = (num, freq-1)
                    back(target-num, i, counter, cur)
                    cur.pop()
                    counter[i] = (num, freq)
        res = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        back(target, 0, counter, [])
        return res
