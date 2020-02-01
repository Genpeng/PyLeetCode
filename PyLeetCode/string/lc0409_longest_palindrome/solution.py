# _*_ coding: utf-8 _*_

"""
This is the solution of no. 409 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/longest-palindrome/

The description of problem is as follow:
==========================================================================================================
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes
that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
- Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7
Explanation:
- One longest palindrome that can be built is "dccaccd", whose length is 7.
==========================================================================================================

Author: Genpeng Xu (xgp1227atgmail.com)
"""

import collections


class Solution:
    def longest_palindrome(self, s: str) -> int:
        """
        ## 解法1 ##
        解题思路：
        统计字符串中出现次数为奇数的字符（或者反过来，统计出现次数为偶数的字符），此解法统计出现次数为奇数的字符的数目
        时间复杂度：O(n)
        空间复杂度：O(1)

        Arguments:
            s: str, the input string

        Return:
            int, the length of the longest palindromes
        """
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)

    def longest_palindrome_v2(self, s: str) -> int:
        """
        ## 解法1 ##
        解题思路：
        统计字符串中出现次数为奇数的字符（或者反过来，统计出现次数为偶数的字符），此解法统计出现次数为偶数的字符的长度
        时间复杂度：O(n)
        空间复杂度：O(1)

        Runtime: 28 ms, faster than 83.02% of Python3 online submissions for Longest Palindrome.
        Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.

        Arguments:
            s: str, the input string

        Return:
            int, the length of the longest palindromes
        """
        counts = [0] * 128
        l = 0
        for c in s:
            counts[ord(c)] += 1
            if counts[ord(c)] & 1 == 0:
                l += 2
        return l + 1 if l < len(s) else l

    def longest_palindrome_v3(self, s: str) -> int:
        """
        ## 解法1 ##
        解题思路：
        统计字符串中出现次数为奇数的字符（或者反过来，统计出现次数为偶数的字符），此解法统计出现次数为偶数的字符的长度
        时间复杂度：O(n)
        空间复杂度：O(1)

        Runtime: 36 ms, faster than 24.49% of Python3 online submissions for Longest Palindrome.
        Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.

        Arguments:
            s: str, the input string

        Return:
            int, the length of the longest palindromes
        """
        counts, l = {}, 0
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            if counts[c] & 1 == 0:
                l += 2
        return l + 1 if l < len(s) else l

    def longest_palindrome_v4(self, s: str) -> int:
        """
        ## 解法1 ##
        解题思路：
        统计字符串中出现次数为奇数的字符（或者反过来，统计出现次数为偶数的字符），此解法统计出现次数为偶数的字符的长度
        时间复杂度：O(n)
        空间复杂度：O(1)

        Runtime: 24 ms, faster than 94.93% of Python3 online submissions for Longest Palindrome.
        Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.

        Arguments:
            s: str, the input string

        Return:
            int, the length of the longest palindromes
        """
        evens = sum(v & ~1 for v in collections.Counter(s).values())
        return evens + (evens < len(s))


if __name__ == "__main__":
    s = "abccccdd"
    solution = Solution()
    print(solution.longest_palindrome_v1(s))
