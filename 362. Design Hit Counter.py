'''
https://leetcode.com/problems/design-hit-counter/
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.
'''
'''
Time: HIT: O(1) GETHITS: O(n)
Space:O(n)
'''
class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = [] 

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.l.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        hit = 0
        for i in self.l:
            if i<=timestamp and i>timestamp-300:
                hit += 1
        return hit
        
'''
Time:O(1) O(n)
Space:O(n)
'''
class HitCounter(object):

    def __init__(self):
        self.q = deque() 

    def hit(self, timestamp):
        self.q.append(timestamp)

    def getHits(self, timestamp):
        while self.q and self.q[0]+300<=timestamp:
            self.q.popleft()
        return len(self.q)
