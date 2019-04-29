# _*_ coding: utf-8 _*_

"""
This is the solution of no. 242 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/valid-anagram/

The description of problem is as follow:
==========================================================================================================
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
- You may assume the string contains only lowercase alphabets.

Follow up:
- What if the inputs contain unicode characters? How would you adapt your solution to such case?
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/29
"""


class Solution1:
    def is_anagram(self, s: str, t: str) -> bool:
        """
        解法一：比较排序后的字符串
        时间复杂度：O(n * log(n))
        空间复杂度：O(n)

        :param s: str, one of the two input strings
        :param t: str, the other input string
        :return: boolean, true if t is an anagram of s
        """
        return sorted(s) == sorted(t)


class Solution2:
    def is_anagram(self, s: str, t: str) -> bool:
        """
        解法二：哈希表
        时间复杂度：O(n)
        空间复杂度：O(n)

        :param s: str, one of the two input strings
        :param t: str, the other input string
        :return: boolean, true if t is an anagram of s
        """
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        for c in t:
            if freq[ord(c) - ord('a')] == 0:
                return False
            freq[ord(c) - ord('a')] -= 1
        return True


def main():
    s = 'anagram'
    t = 'nagaram'
    print((Solution2()).is_anagram(s, t))


if __name__ == '__main__':
    main()
