'''
https://leetcode.com/problems/combination-sum-iii/
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def back(start, target, subset):
            if target<0 or len(subset)>k:
                return
            elif target==0 and len(subset)==k:
                res.append(subset[:])
            for num in range(start,10):
                subset.append(num)
                back(num+1, target-num, subset)
                subset.pop()
        
        res = []
        back(1, n, [])
        return res
        
'''
Method below uses the code in #40.
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        nums=[1,2,3,4,5,6,7,8,9]
        self.sum(nums,0,[],result,k,n)
        return result
    
    def sum(self,nums,start,path,result,k,target):
        if target==0 and k==0:
            result.append(path)
        for i in range(start,len(nums)):
            if target<0 or k<=0:
                break
            self.sum(nums,i+1,path+[nums[i]],result,k-1,target-nums[i])
