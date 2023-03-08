# _*_ coding: utf-8 _*_

"""
This is the solution of no. 46 problem in the LeetCode,
where the website of the problem is as follow:
https://leetcode.com/problems/permutations/

The description of problem is as follow:
==========================================================================================================
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.
==========================================================================================================

Difficulty: Medium
Tags: array;backtracking;

Author: Genpeng Xu (xgp1227atgmail.com)
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        if not nums:
            return perms
        L = len(nums)
        path, seen = [], [False] * L
        self.dfs(nums, L, 0, path, seen, perms)
        return perms

    def dfs(self, nums: List[int], L: int, depth: int, path: List[int], seen: List[bool], perms: List[List[int]]) -> None:
        if depth == L:
            perms.append(path)
            return
        for i in range(L):
            if seen[i]:
                continue
            path.append(nums[i])
            seen[i] = True
            self.dfs(nums, L, depth+1, path, seen, perms)
            seen[i] = False
            path.pop()
