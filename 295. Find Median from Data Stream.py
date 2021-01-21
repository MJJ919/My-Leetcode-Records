'''
https://leetcode.com/problems/find-median-from-data-stream/
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.
For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
'''
'''
Time:O(lgn)
Space:O(n)
'''
class MedianFinder:
    def __init__(self):
        self.s = []
        self.b = []
        
    def addNum(self, num: int) -> None:
        if not self.b or self.b[0]<=num:
            heapq.heappush(self.b, num)
        else:
            heapq.heappush(self.s, -num)
        if len(self.b)>len(self.s)+1:
            heapq.heappush(self.s, -heapq.heappop(self.b))
        elif len(self.b)<len(self.s):
            heapq.heappush(self.b, -heapq.heappop(self.s))

    def findMedian(self) -> float:
        if len(self.b)==len(self.s):
            return -self.s[0]/2+self.b[0]/2
        else:
            return self.b[0]
            
'''
Pretty slow.
'''
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.len = 0
    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()
        
    def findMedian(self) -> float:
        n = len(self.l)
        if n%2 == 1:
            return self.l[(n//2)]
        else:
            return float((self.l[n//2]+self.l[(n-1)//2])/2)
