'''
https://leetcode.com/problems/permutations-ii/
Example 1:
Input: nums = [1,1,2]
Output:[[1,1,2],[1,2,1],[2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def back(subset):
            if len(subset)==len(nums):
                res.append(subset[:])
            for num, freq in counter.items():
                if freq>0:
                    subset.append(num)
                    counter[num] -= 1
                    back(subset)
                    subset.pop()
                    counter[num] += 1
        
        counter = Counter(nums)
        res = []
        back([])
        return res
