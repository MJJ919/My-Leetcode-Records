/*
https://leetcode.com/problems/basic-calculator-iii/
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, '+', '-', '*', '/' operators, 
and open '(' and closing parentheses ')'. The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Example 1:
Input: s = "1+1"
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
            if (Character.isDigit(ch))  num = num*10 + (ch - '0');
            if (ch == '(')  num = calculate(s);
            if (i==s.length() || ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')'){
                if (ope=='-')   stack.add(-num);
                else if (ope=='*')   stack.add(stack.pop()*num);
                else if (ope=='/')   stack.add(stack.pop()/num);
                else    stack.add(num);
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
