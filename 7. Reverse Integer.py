class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
       
        if x < 0:
            reverse = int("-"+str(-x)[::-1])    
        else:
                reverse = int(str(x)[::-1])
        if reverse < -2**31 or reverse > 2**31-1:
            return 0
        else:
            return reverse
