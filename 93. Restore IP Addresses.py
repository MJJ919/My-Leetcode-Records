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
        def back(s, cur):
            if output(s,cur):
                for i in range(0, len(s)):
                    if valid(s[:i+1]):
                        cur.append(s[:i+1])
                        back(s[i+1:], cur)
                        cur.pop()
                        
        def output(s, cur):
            if len(cur)>4 and s:
                return False
            elif len(cur)==4 and not s:
                res.append('.'.join(cur))
                return False
            return True
                
        def valid(s):
            return int(s)<256 if s[0]!='0' else len(s)==1
        res = []
        back(s, [])
        return res
