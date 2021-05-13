'''
https://leetcode.com/problems/ambiguous-coordinates/
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  
Then, we removed all commas, decimal points, and spaces, and ended up with the string s.  
Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", 
or any other number that can be represented with less digits.  
Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  
Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
'''
'''
Time:O(n**3)
Space:O(n**3)
'''
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag):
            for i in range(1, len(frag)+1):
                left = frag[:i]
                right = frag[i:]
                if (not left.startswith('0') or left=='0') and (not right.endswith('0')):
                    yield left+('.' if i!=len(frag) else '')+right
        
        s = s[1:-1]
        return ['({}, {})'.format(*cand)
               for i in range(1, len(s))
               for cand in itertools.product(make(s[:i]), make(s[i:]))]
