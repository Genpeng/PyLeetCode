# _*_ coding: utf-8 _*_

"""
This is the solution of no. 844 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/backspace-string-compare/

The description of problem is as follow:
==========================================================================================================
Given two strings S and T, return if they are equal when both are typed into empty text editors.
`#` means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
- 1 <= S.length <= 200
- 1 <= T.length <= 200
- S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/10
"""


class Solution1:
    def backspace_compare(self, S, T):
        return self._restore(S) == self._restore(T)

    def _restore(self, s):
        if s is None:
            raise Exception("[INFO] The input string is None!!!")
        stack = []
        for c in s:
            if c != '#':
                stack.append(c)
            elif len(stack) != 0:
                stack.pop()
        return ''.join(stack)


class Solution2:
    def backspace_compare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        s_skip, t_skip = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    i -= 1
                    s_skip += 1
                elif s_skip > 0:
                    i -= 1
                    s_skip -= 1
                else:
                    break

            while j >= 0:
                if T[j] == '#':
                    j -= 1
                    t_skip += 1
                elif t_skip > 0:
                    j -= 1
                    t_skip -= 1
                else:
                    break

            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False

            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True


def main():
    S, T = "ab#c", "ad#c"
    print((Solution2()).backspace_compare(S, T))


if __name__ == '__main__':
    main()
