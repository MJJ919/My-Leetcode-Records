'''
https://leetcode.com/problems/search-suggestions-system/
Given an array of strings products and a string searchWord. 
We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord. 
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
'''
'''
Time:O(m*nlgn)
Space:O(m*n)
'''
class Solution:
    def suggestedProducts(self, products: List[str], s: str) -> List[List[str]]:
        res = []
        products.sort()
        for i in range(len(s)):
            pos = bisect.bisect_left(products, s[:i+1])
            res.append([p for p in products[pos:pos+3] if p.startswith(s[:i+1])])
        return res
        
'''
Time:O(m*n)
Space:O(m*n)
'''
class Solution:
    def suggestedProducts(self, products: List[str], s: str) -> List[List[str]]:
        res = []
        products.sort()
        def find(lists, target):
            res = []
            for l in lists:
                if l.startswith(target):
                    res.append(l)
                if len(res)==3:
                    break
            return res      
        
        for i in range(len(s)):
            if not res or len(res[-1])==3:
                res.append(find(products, s[:i+1]))
            else:
                res.append(find(res[-1], s[:i+1]))        
        return res
