'''
https://leetcode.com/problems/longest-absolute-file-path/
'''
'''
Time:O(n)
Space:O(n)
'''
#backlash isnot counted in len() function.
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res, d = 0, {-1:0}
        for i in input.split('\n'):
            depth = i.count('\t')
            d[depth] = d[depth-1]+len(i)-depth
            if '.' in i:
                res = max(res, d[depth]+depth)
        return res
