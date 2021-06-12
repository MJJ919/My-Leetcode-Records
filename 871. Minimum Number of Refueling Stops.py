'''
https://leetcode.com/problems/minimum-number-of-refueling-stops/
A car travels from a starting position to a destination which is target miles east of the starting position.
Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position,
and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  
It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
What is the least number of refueling stops the car must make in order to reach its destination?  
If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  
If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution {
    public int minRefuelStops(int target, int tank, int[][] stations) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int res = 0;
        int prev = 0;
        for (int i=0; i<stations.length; i++){
            int pos = stations[i][0], gas = stations[i][1];
            tank -= pos - prev;
            while (!pq.isEmpty() && tank<0){
                tank += pq.poll();
                res++;
            }
            if (tank<0) return -1;
            pq.offer(gas);
            prev = pos;
        }
        tank -= target - prev;
        while (!pq.isEmpty() && tank<0){
            tank += pq.poll();
            res++;
            }
        if (tank<0) return -1;
        return res;
    }
}

'''
Time:(n**2)
Space:O(n)
'''
class Solution:
    def minRefuelStops(self, target: int, tank: int, stations: List[List[int]]) -> int:
        dp = [tank] + [0 for _ in range(len(stations))]
        for loc, [pos, gas] in enumerate(stations):
            for i in range(loc, -1, -1):
                if dp[i]>=pos:
                    dp[i+1] = max(dp[i+1], dp[i]+gas)
        for stop, gas in enumerate(dp):
            if gas>=target:
                return stop
        return -1
