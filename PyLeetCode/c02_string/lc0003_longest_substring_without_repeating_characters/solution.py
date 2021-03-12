# _*_ coding: utf-8 _*_

"""
This is the solution of no. 3 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/longest-substring-without-repeating-characters/

The description of problem is as follow:
==========================================================================================================
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
 
Constraints:
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.
==========================================================================================================

Difficulty: Medium
Tags: string;two pointers;hash table;sliding window;

Author: Genpeng Xu (xgp1227atgmail.com)
"""


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: Sliding Window (v1)

        Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            s: str, the input string

        Returns:
            int, the length of the longest substring without repeating characters
        """
        L = len(s)
        if L <= 1:
            return L
        li = 0
        window = set()
        max_len = 0
        for ri, c in enumerate(s):
            while c in window:
                window.remove(s[li])
                li += 1
            window.add(c)
            max_len = max(max_len, ri - li + 1)
        return max_len


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: Sliding Window (v2)

        Complexity Analysis:
        Time Complexity: O(N)
        Space Complexity: O(1)

        Args:
            s: str, the input string

        Returns:
            int, the length of the longest substring without repeating characters
        """
        L = len(s)
        if L <= 1:
            return L
        char_2_idx = {}
        max_len = 0
        li = 0
        for ri, c in enumerate(s):
            if c in char_2_idx and char_2_idx.get(c) >= li:
                li = char_2_idx.get(c) + 1
            else:
                max_len = max(max_len, ri - li + 1)
            char_2_idx[c] = ri
        return max_len

