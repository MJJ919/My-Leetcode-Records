/*
https://leetcode.com/problems/the-skyline-problem/
*/
/*
Time:O(nlgn)
Space:O(n)
*/
class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> res = new ArrayList<>();
        List<int[]> build = new ArrayList<>();
        for (int[] building: buildings){
            build.add(new int[]{building[0], -building[2]});
            build.add(new int[]{building[1], building[2]});
        }
        Collections.sort(build, (a, b) -> a[0]==b[0]? a[1]-b[1]: a[0]-b[0]);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b-a);
        pq.offer(0);
        int pre = 0;
        for (int[] b:build){
            if (b[1]<0) pq.offer(-b[1]);
            else pq.remove(b[1]);
            if (pre!=pq.peek()){
                res.add(List.of(b[0], pq.peek()));
                pre = pq.peek();
            }
        }
        return res;
    }
}
