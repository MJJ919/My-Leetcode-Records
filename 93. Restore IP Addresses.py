'''
https://leetcode.com/problems/restore-ip-addresses/
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. 
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]
'''
'''
Time:
Space:
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(substr):
            return int(substr)<=255 if substr[0]!='0' else len(substr)==1
        
        def update(segments, pos):
            segment = s[pos+1:]
            if valid(segment):
                segments.append(segment)
                res.append('.'.join(segments))
                segments.pop()
        
        def back(pre, dot, segments):
            for pos in range(pre+1, min(pre+4,len(s)-1)):
                segment = s[pre+1:pos+1]
                if valid(segment):
                    segments.append(segment)
                    if dot-1==0:
                        update(segments, pos)
                    else:
                        back(pos, dot-1, segments)
                    segments.pop()
        
        res = []
        back(-1, 3, [])
        return res
