'''
https://leetcode.com/problems/factor-combinations/
Write a function that takes an integer n and return all possible combinations of its factors.
Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.

Example 2:
Input: 37
Output:[]

Example 3:
Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
'''
'''
'''
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def back(start, subset, target):
            if len(subset)>0:
                res.append(subset+[target])
            for num in range(start, int(math.sqrt(target))+1):
                if target%num==0:
                    back(num, subset+[num], target//num)
                    
        res = []
        back(2, [], n)
        return res
