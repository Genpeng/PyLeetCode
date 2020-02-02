# _*_ coding: utf-8 _*_

"""
This is the solution of no. 557 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/reverse-words-in-a-string-iii/

The description of problem is as follow:
==========================================================================================================
Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
==========================================================================================================

Author: Genpeng Xu (xgp1227atgmail.com)
"""


class Solution:
    def reverse_words(self, s: str) -> str:
        """
        # 解法一
        解题思路：
        split -> reverse -> join

        Arguments:
            s: str, the input string

        Return:
            str, the modified string
        """
        return " ".join([x[::-1] for x in s.split()])  # list comprehension


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    solution = Solution()
    assert "s'teL ekat edoCteeL tsetnoc" == solution.reverse_words(s)
