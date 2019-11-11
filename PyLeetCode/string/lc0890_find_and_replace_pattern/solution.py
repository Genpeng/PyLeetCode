# _*_ coding: utf-8 _*_

"""
This is the solution of no. 890 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/find-and-replace-pattern/

The description of problem is as follow:
==========================================================================================================
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x
in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.

Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

Note:
1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
==========================================================================================================

Author: StrongXGP (xgp1227@gmail.com)
"""

from typing import List


class Solution1:
    def find_and_replace_pattern(self, words: List[str], pattern: str) -> List[str]:
        """
        题意解读：
        a word matches pattern <=> 在pattern和word之间存在一对一的映射 <=> pattern和word之间不能有一对多和多对一的情况

        解法一：利用两个map
        利用map存储从pattern到word之间映射关系，可以解决pattern到word之间一对多的情况，
        但是无法解决pattern和word之间多对一的情况。为了解决这个问题，可以再利用一个map，
        存储从word到pattern之间的映射关系，就可以解决word到pattern之间一对多的情况，
        从而解决pattern到word之间多对一的映射关系（对偶问题）。

        时间复杂度：O(N K)，其中N是字符串的数目，K表示字符串的长度
        空间复杂度：O(K)

        Args:
            words: List[int], a list of words
            pattern: str, a string represents a pattern

        Return:
            List[int], a list of the words that match the given pattern
        """
        if not pattern or len(pattern) == 0:
            raise Exception("[ERROR] The input pattern must not be null!!!")
        if not words:
            return []
        ans = []
        for word in words:
            if self._is_match(word, pattern):
                ans.append(word)
        return ans

    def _is_match(self, word: str, pattern: str) -> bool:
        if len(word) != len(pattern):
            return False
        m1, m2 = {}, {}
        for i in range(len(word)):
            w, p = word[i], pattern[i]
            if w not in m1:
                m1[w] = p
            if p not in m2:
                m2[p] = w
            if m1[w] != p or m2[p] != w:
                return False
        return True


class Solution2:
    def find_and_replace_pattern(self, words: List[str], pattern: str) -> List[str]:
        """
        题意解读：
        a word matches pattern <=> 在pattern和word之间存在一对一的映射 <=> pattern和word之间不能有一对多和多对一的情况

        解法二：利用一个map
        解法二的思路与解法一是一致的，只是在处理pattern和word之间多对一情况时，采用了另一种方式——查看pattern到word之间映射
        的值（value）是否唯一。

        时间复杂度：O(N K)，其中N是字符串的数目，K表示字符串的长度
        空间复杂度：O(K)

        Runtime: 28 ms, faster than 99.23% of Python3 online submissions for Find and Replace Pattern.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find and Replace Pattern.

        Args:
            words: List[int], a list of words
            pattern: str, a string represents a pattern

        Return:
            List[int], a list of the words that match the given pattern
        """
        if not pattern or len(pattern) == 0:
            raise Exception("[ERROR] The input pattern must not be null!!!")
        if not words:
            return []
        ans = []
        for word in words:
            if self._is_match(word, pattern):
                ans.append(word)
        return ans

    def _is_match(self, word: str, pattern: str) -> bool:
        if len(word) != len(pattern):
            return False
        d = {}
        for w, p in zip(word, pattern):
            if d.setdefault(p, w) != w:
                return False
        seen = [False] * 26
        for v in d.values():
            if seen[ord(v) - ord('a')]:
                return False
            seen[ord(v) - ord('a')] = True
        return True

    def _is_match_v2(self, word: str, pattern: str) -> bool:
        if len(word) != len(pattern):
            return False
        d = {}
        for w, p in zip(word, pattern):
            if d.setdefault(p, w) != w:
                return False
        return len(set(d.values())) == len(d.values())
