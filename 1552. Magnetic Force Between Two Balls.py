'''
https://leetcode.com/problems/magnetic-force-between-two-balls/
In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. 
Rick has n empty baskets, the ith basket is at position[i], 
Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
Given the integer array position and the integer m. Return the required force.

Example 1:
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        def guess(dis):
            count = 1
            cur = pos[0]
            for i in range(1, len(pos)):
                if pos[i]-cur>=dis:
                    count += 1
                    cur = pos[i]
            return count
        
        pos.sort()            
        left = 0
        right = pos[-1]-pos[0]
        while left<=right:
            mid = left + (right-left)//2
            if guess(mid)<m:
                right = mid-1
            else:
                left = mid+1
        return right
