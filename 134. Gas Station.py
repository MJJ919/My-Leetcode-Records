'''
https://leetcode.com/problems/gas-station/
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:
If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

Example 1:
Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output: 3

Example 2:
Input: 
gas  = [2,3,4]
cost = [3,4,3]
Output: -1
'''
'''
Time:O(n)
Space:O91)
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank,minimun,minindex = 0,gas[0]-cost[0],0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if minimun>tank:
                minindex = i
                minimun = tank
        if tank<0:
            return -1
        return (minindex+1)%len(gas)
