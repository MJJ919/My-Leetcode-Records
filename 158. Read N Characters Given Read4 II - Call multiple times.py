'''
https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
'''
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = deque()
    def read(self, buf: List[str], n: int) -> int:
        buf4 = [""]*4
        idx = 0
        while self.q and n:
            buf[idx] = self.q.popleft()
            idx += 1
            n -= 1
        
        while n>0:
            read = read4(buf4)
            if not read:
                return idx
            
            if read>n:
                self.q+=buf4[n:read]
            
            for i in range(min(n,read)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx
