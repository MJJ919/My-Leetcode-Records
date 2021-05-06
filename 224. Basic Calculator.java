/*
https://leetcode.com/problems/basic-calculator/
Given a string s representing an expression, implement a basic calculator to evaluate it.
Example 1:
Input: s = "1 + 1"
Output: 2
*/
/*
Time:O(n)
Space:O(n)
*/
class Solution {
    int i = 0;
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        int num = 0;
        char ope = '+';
        while (i<s.length()){
            char ch = s.charAt(i++);
            if (Character.isDigit(ch))   num = num*10 + (ch - '0');
            if (ch=='(')    num = calculate(s);
            if (i==s.length() || ch == '+' || ch == '-' || ch == ')'){
                if (ope=='+')  stack.push(num);
                else    stack.push(-num);
                ope = ch;
                num = 0;
        }
            if (ch==')')    break;
    }
        int res = 0;
        while (!stack.isEmpty()){
            res += stack.pop();
        }
        return res;
    }
}
