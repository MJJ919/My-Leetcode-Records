/*
https://leetcode.com/problems/design-a-stack-with-increment-operation/
Design a stack which supports the following operations.

Implement the CustomStack class:
CustomStack(int maxSize) Initializes the object with maxSize which is the maximum 
number of elements in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn't reached the maxSize.
int pop() Pops and returns the top of stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. 
If there are less than k elements in the stack, just increment all the elements in the stack.
*/
/*
Time:O(1)
Space:O(n)
*/
class CustomStack {
    int n;
    int[] inc;
    Stack<Integer> s = new Stack<>();
    public CustomStack(int maxSize) {
        n = maxSize;
        inc = new int[n];
    }
    
    public void push(int x) {
        if (s.size()<n)
            s.add(x);
    }
    
    public int pop() {
        int pos = s.size()-1;
        if (pos<0)  return -1;
        if (pos>0) inc[pos-1] += inc[pos];
        int num = s.pop() + inc[pos];
        inc[pos] = 0;
        return num;
    }
    
    public void increment(int k, int val) {
        int pos = Math.min(k-1, s.size()-1);
        if (pos>=0)
            inc[pos] += val;
    }
}
