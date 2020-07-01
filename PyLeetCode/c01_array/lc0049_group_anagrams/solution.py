# _*_ coding: utf-8 _*_

"""
This is the solution of no. 49 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/group-anagrams/

The description of problem is as follow:
==========================================================================================================
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],

Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
- All inputs will be in lowercase.
- The order of your output does not matter.
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
Date:   2019/04/30
"""

from collections import defaultdict


class Solution1:
    def group_anagrams(self, strs: list) -> list:
        """
        解法一：哈希表，key为排序后的字符串
        时间复杂度：O(N * k * log(K))，其中，N表示列表的大小，K表示列表中最长字符串的长度
        空间复杂度：O(N)

        :param strs: list[str], list of strings
        :return: list[list[str]], list of grouped anagrams
        """
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


class Solution2:
    def group_anagrams(self, strs: list) -> list:
        """
        解法二：哈希表，key为字符频次的元组
        时间复杂度：O(N * k)，其中，N表示列表的大小，K表示列表中最长字符串的长度
        空间复杂度：O(N)

        :param strs: list[str], list of strings
        :return: list[list[str]], list of grouped anagrams
        """
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print((Solution2()).group_anagrams(strs))


if __name__ == '__main__':
    main()
