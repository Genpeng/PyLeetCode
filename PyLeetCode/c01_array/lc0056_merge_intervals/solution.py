# _*_ coding: utf-8 _*_

"""
This is the solution of no. 56 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.cn/problems/merge-intervals/

The description of problem is as follow:
==========================================================================================================
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 104
- intervals[i].length == 2
- 0 <= starti <= endi <= 104
==========================================================================================================

Difficulty: Medium
Tags: array;

Author: Genpeng Xu (xgp1227atgmail.com)
"""

from typing import List


class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        思路：
        将区间列表按照区间的起始位置进行排序，则需要合并的区间（有交集的）一定是连续的

        时间复杂度：O(Nlog(N))
        空间复杂度：O(N)

        备注：
        - Python 的 `sorted` 函数采用的是 Timsort 算法，时间复杂度为 O(Nlog(N))，
          空间复杂度为 O(N)

        输入限制：
        - 1 <= L <= 10^4
        - 0 <= start_index <= end_index <= 10^4

        Args:
            intervals: List[List[int]], an array of intervals

        Returns:
            List[List[int]], an array of the non-overlapping intervals
            by merging all overlapping intervals
        """
        L = len(intervals)
        if L < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0], reverse=False)
        result = []
        for i in range(L):
            if (i == 0) or (intervals[i][0] > result[-1][1]):
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        return result