'''
274 gives an unsorted list while 275 gives a sorted one.
https://leetcode.com/problems/h-index/
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
According to the definition of h-index on Wikipedia: 
"A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:
Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l,r = 0,len(citations)-1
        citations.sort(reverse=True)
        while l <= r:
            mid = (l+r)//2
            if citations[mid] >= mid+1:
                l = mid+1
            else:
                r = mid-1
        return l
      
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        for i,ch in enumerate(citations):
            if ch>=len(citations)-i:
                return len(citations)-i
        return 0

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i = 0
        while i<len(citations):
            if citations[len(citations)-i-1]>i:
                i += 1
            else:   break
        return i
