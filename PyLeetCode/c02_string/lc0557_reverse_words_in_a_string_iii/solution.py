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
        # 解法1（写法1）
        解题思路：
        Split the string into words, reverse each word, then join them back together.
        时间复杂度：O(n)
        空间复杂度：O(1)

        Arguments:
            s: str, the input string

        Return:
            str, the modified string
        """
        # return " ".join(x[::-1] for x in s.split())  # generator expression
        return " ".join([x[::-1] for x in s.split()])  # list comprehension expression (faster)

    def reverse_words_v2(self, s: str) -> str:
        """
        # 解法1（写法2）
        解题思路：
        Split the string into words, reverse the order of the words, then reverse the entire string.
        时间复杂度：O(n)
        空间复杂度：O(1)

        Arguments:
            s: str, the input string

        Return:
            str, the modified string
        """
        return " ".join(s.split()[::-1])[::-1]


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    solution = Solution()
    assert "s'teL ekat edoCteeL tsetnoc" == solution.reverse_words_v2(s)
