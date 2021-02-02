'''
https://leetcode.com/problems/palindrome-permutation-ii/
Given a string s, return all the palindromic permutations (without duplicates) of it. 
Return an empty list if no palindromic permutation could be form.

Example 1:
Input: "aabb"
Output: ["abba", "baab"]

Example 2:
Input: "abc"
Output: []
'''
'''
Time:O((n/2)!)
Space:O(n)
'''
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        res = []
        counter = Counter(s)
        odd = [key for key, value in counter.items() if value % 2 != 0]
        if len(odd) > 1:
            return res        
            
        def builder(string):
            if len(string) == len(s):
                res.append(string)
                return 
            for key, value in counter.items():
                if value>0:
                    counter[key] -= 2
                    builder(key+string+key)
                    counter[key] += 2
        string = ''
        if odd:
            counter[odd[0]] -= 1
            builder(odd[0])
        else:
            builder(string)
        return res
