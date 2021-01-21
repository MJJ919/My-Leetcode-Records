'''
https://leetcode.com/problems/data-stream-as-disjoint-intervals/
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:
[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
'''
'''
Time:O(nlgn)
Space:O(n)
'''
'''
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.seen = set()
        self.findhead = {}
        self.range = {}

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            if val-1 in self.findhead:
                head = self.findhead[val-1]
                self.findhead[val] = head
                self.range[head][1] += 1
            else:
                head = val
                self.findhead[val] = val
                self.range[val] = [val,val]
                
            if val+1 in self.findhead:
                self.range[head][1] = self.range[val+1][1]
                self.findhead[self.range[val+1][1]] = head
                self.range[val+1] = None

    def getIntervals(self) -> List[List[int]]:
        return sorted([self.range[i] for i in self.range if self.range[i] is not None], key = lambda x:x[0])
