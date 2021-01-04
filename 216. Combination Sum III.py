'''
https://leetcode.com/problems/combination-sum-iii/
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def back(start,cur):
            if len(cur)==k and sum(cur)==n:
                res.append(cur[:])
                return
            elif sum(cur)>n or len(cur)>k:
                return 
            for i in range(start,10):
                cur.append(i)
                back(i+1,cur)
                cur.pop()
        
        res=[]
        back(1,[])
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
