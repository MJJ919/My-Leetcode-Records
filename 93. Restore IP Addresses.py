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
        def valid(string):
            return 255>=int(string) if string[0]!='0' else len(string)==1
        
        def add(pos, path):
            if valid(s[pos:]):
                path.append(s[pos:])
                res.append('.'.join(path))
                path.pop()
                
        def bt(path, pos, dot):
            for end in range(pos+1, min(pos+4, len(s))):
                string = s[pos:end]
                if valid(string):
                    path.append(string)
                    if dot==1:
                        add(end, path)
                    else:
                        bt(path, end, dot-1)
                    path.pop()
            
        res = []
        bt([], 0, 3)
        return res
