# _*_ coding: utf-8 _*_

"""
This is the solution of no. 20 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/valid-parentheses/

The description of problem is as follow:
==========================================================================================================
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/09
"""


class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or c != stack.pop():
                return False
        return not stack


def main():
    print((Solution()).is_valid("()()()"))


if __name__ == '__main__':
    main()
