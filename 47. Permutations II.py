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
backtracking.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def back(counter,cur):
            if len(cur)==n:
                res.append(cur[:])
                return
            for i in counter:
                if counter[i]>0:
                    cur.append(i)
                    counter[i] -= 1
                    back(counter, cur)
                    cur.pop()
                    counter[i] += 1
        res, n = [], len(nums)
        back(Counter(nums),[])
        return res
